# %% [markdown]
# # Latih Model Sesuai Judul
# Fitur yang dipakai hanya: fragrance notes, accords, dan tingkat konsentrasi.
# Tahun dan gender dikeluarkan karena tidak ada di judul dan kontribusinya kecil.

# %%
import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

BASE = Path.cwd()
OUT = BASE / "output"
MODEL = BASE / "model"
OUT.mkdir(exist_ok=True)
MODEL.mkdir(exist_ok=True)

clean = pd.read_csv(BASE / "clean.csv")
semua = json.load(open(BASE / "feature_columns.json"))

note = [c for c in semua if c.startswith("note_")]
accord = [c for c in semua if c.startswith("accord_")]
fitur = note + accord + ["concentration_level"]

print("note   :", len(note))
print("accord :", len(accord))
print("total fitur:", len(fitur))

# %%
y = clean["longevity_avg"]
X = clean[fitur].astype("float32")

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Latih:", X_train.shape, "| Uji:", X_test.shape)

X_train.to_csv(BASE / "X_train.csv", index=False)
X_test.to_csv(BASE / "X_test.csv", index=False)
y_train.to_frame().to_csv(BASE / "y_train.csv", index=False)
y_test.to_frame().to_csv(BASE / "y_test.csv", index=False)
json.dump(fitur, open(BASE / "feature_columns.json", "w"), indent=1)

# %%
def metrik(nama, y_true, y_pred, y_tr_pred=None):
    mse = mean_squared_error(y_true, y_pred)
    return {
        "Model": nama,
        "MAE": round(mean_absolute_error(y_true, y_pred), 4),
        "MSE": round(mse, 4),
        "RMSE": round(np.sqrt(mse), 4),
        "R2": round(r2_score(y_true, y_pred), 4),
        "R2_latih": round(r2_score(y_train, y_tr_pred), 4) if y_tr_pred is not None else None,
    }

hasil = []
model_terlatih = {}

# %%
dummy = DummyRegressor(strategy="mean").fit(X_train, y_train)
hasil.append(metrik("Baseline (rata-rata)", y_test, dummy.predict(X_test), dummy.predict(X_train)))

# %%
grid = GridSearchCV(Ridge(), {"alpha": [0.01, 0.1, 1, 10, 100]},
                    cv=3, scoring="neg_mean_absolute_error", n_jobs=1)
grid.fit(X_train, y_train)
ridge = grid.best_estimator_
model_terlatih["Ridge"] = ridge
print("alpha Ridge terbaik:", grid.best_params_["alpha"])
hasil.append(metrik("Ridge", y_test, ridge.predict(X_test), ridge.predict(X_train)))

# %%
rf = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1).fit(X_train, y_train)
model_terlatih["Random Forest"] = rf
hasil.append(metrik("Random Forest", y_test, rf.predict(X_test), rf.predict(X_train)))

# %%
gb = GradientBoostingRegressor(n_estimators=200, learning_rate=0.05, max_depth=3,
                               random_state=42).fit(X_train, y_train)
model_terlatih["Gradient Boosting"] = gb
hasil.append(metrik("Gradient Boosting", y_test, gb.predict(X_test), gb.predict(X_train)))

# %%
tabel = pd.DataFrame(hasil)
tabel["selisih_R2"] = (tabel["R2_latih"] - tabel["R2"]).round(4)
print(tabel.to_string(index=False))
tabel.to_csv(OUT / "tabel_perbandingan_model.csv", index=False)

# %%
penting = pd.DataFrame({"fitur": fitur, "importance": rf.feature_importances_}).sort_values("importance", ascending=False)
print(penting.head(12).to_string(index=False))
penting.to_csv(OUT / "feature_importance.csv", index=False)

atas = penting.head(15).iloc[::-1]
fig, ax = plt.subplots(figsize=(7, 5))
ax.barh(atas["fitur"], atas["importance"], color="#2F6F8F")
ax.set_xlabel("Tingkat kepentingan")
ax.set_title("15 fitur paling berpengaruh")
fig.tight_layout()
fig.savefig(OUT / "feature_importance.png", dpi=150)
plt.close(fig)

# %%
calon = tabel[(tabel["Model"] != "Baseline (rata-rata)") & (tabel["selisih_R2"] < 0.10)]
nama_aplikasi = calon.sort_values("MAE").iloc[0]["Model"]
model_aplikasi = model_terlatih[nama_aplikasi]
print("Model untuk aplikasi:", nama_aplikasi)

pred = model_aplikasi.predict(X_test)
fig, ax = plt.subplots(figsize=(5.5, 5))
ax.scatter(y_test, pred, s=8, alpha=0.35, color="#2F6F8F")
ax.plot([1, 5], [1, 5], color="#B08D57", linewidth=1.5, linestyle="--")
ax.set_xlabel("Nilai asli")
ax.set_ylabel("Nilai prediksi")
ax.set_title(f"Prediksi vs aktual ({nama_aplikasi})")
ax.set_xlim(1, 5); ax.set_ylim(1, 5)
fig.tight_layout()
fig.savefig(OUT / "prediksi_vs_aktual.png", dpi=150)
plt.close(fig)
print("rentang prediksi:", round(float(pred.min()), 3), "sampai", round(float(pred.max()), 3))

# %%
joblib.dump(model_aplikasi, MODEL / "model_aplikasi.pkl")
json.dump({
    "model": nama_aplikasi,
    "fitur": fitur,
    "kolom_note": note,
    "kolom_accord": accord,
    "n_note": len(note),
    "n_accord": len(accord),
    "metrik": tabel.set_index("Model").to_dict(orient="index"),
    "skala": "nilai 0 sampai 1, bobot suara pengguna Fragrantica",
}, open(MODEL / "model_info.json", "w"), indent=1)
print("Tersimpan model:", MODEL / "model_aplikasi.pkl")

# %%
# Katalog parfum untuk aplikasi
katalog = []
for i, r in clean.iterrows():
    notes = {c.replace("note_", ""): round(float(r[c]), 3) for c in note if r[c] > 0}
    accords = {c.replace("accord_", ""): round(float(r[c]), 3) for c in accord if r[c] > 0}
    if not notes and not accords:
        continue
    katalog.append({
        "id": int(i),
        "brand": str(r["brand"]),
        "nama": str(r["name"]),
        "konsentrasi": str(r["concentration"]),
        "level": int(r["concentration_level"]),
        "notes": notes,
        "accords": accords,
    })

json.dump(katalog, open(BASE / "katalog_parfum.json", "w"), ensure_ascii=False)
print("Katalog:", len(katalog), "parfum")
print("dengan konsentrasi terisi:", sum(1 for k in katalog if k["level"] > 0))
print("Contoh:", katalog[0])
