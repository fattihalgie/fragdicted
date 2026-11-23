# %% [markdown]
# # 04 - Pemodelan dan Evaluasi
# Ridge, Random Forest, Gradient Boosting, dibandingkan dengan baseline.

# %%
import pandas as pd
import numpy as np
import json
import joblib
from pathlib import Path

from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

ROOT = Path.cwd().parent if Path.cwd().name == "notebook" else Path.cwd()
DATA = ROOT / "data"
OUT = ROOT / "output"
MODEL = ROOT / "model"
OUT.mkdir(exist_ok=True)
MODEL.mkdir(exist_ok=True)

X_train = pd.read_csv(DATA / "X_train.csv")
X_test = pd.read_csv(DATA / "X_test.csv")
y_train = pd.read_csv(DATA / "y_train.csv").iloc[:, 0]
y_test = pd.read_csv(DATA / "y_test.csv").iloc[:, 0]

info = json.load(open(DATA / "feature_columns.json"))

# Fitur komposisi: notes, accords, konsentrasi, dan jumlah bahannya.
# Fitur popularitas seperti vote_count dan want sengaja tidak dipakai, karena
# parfum baru belum punya data itu sehingga model tidak akan berguna.
komposisi = info["kolom_base"] + info["kolom_accord"] + [
    "concentration_score", "conc_known",
    "n_accords", "n_notes_base", "n_notes_top", "n_notes_middle",
]

X_train = X_train[komposisi]
X_test = X_test[komposisi]

print("Fitur dipakai:", len(komposisi))
print("Latih:", X_train.shape, "| Uji:", X_test.shape)

# %%
def hitung_metrik(nama, y_true, y_pred, y_train_pred=None):
    baris = {
        "model": nama,
        "MAE": round(mean_absolute_error(y_true, y_pred), 4),
        "MSE": round(mean_squared_error(y_true, y_pred), 4),
        "RMSE": round(mean_squared_error(y_true, y_pred) ** 0.5, 4),
        "R2_test": round(r2_score(y_true, y_pred), 4),
    }
    baris["R2_train"] = round(r2_score(y_train, y_train_pred), 4) if y_train_pred is not None else None
    return baris


hasil = []
baseline = np.full(len(y_test), float(y_train.mean()))
hasil.append(hitung_metrik("Baseline (rata-rata)", y_test, baseline))
print(hasil[-1])

# %%
# Model 1, Ridge dengan pencarian alpha
from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(
    Ridge(),
    {"alpha": [0.01, 0.1, 1, 10, 100]},
    cv=3,
    scoring="neg_mean_absolute_error",
    n_jobs=-1,
)
grid.fit(X_train, y_train)
ridge = grid.best_estimator_
print("Alpha terbaik:", grid.best_params_["alpha"])

hasil.append(hitung_metrik("Ridge", y_test, ridge.predict(X_test), ridge.predict(X_train)))
print(hasil[-1])

# %%
# Model 2, Random Forest
rf = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
hasil.append(hitung_metrik("Random Forest", y_test, rf.predict(X_test), rf.predict(X_train)))
print(hasil[-1])

# %%
# Model 3, Gradient Boosting
gb = GradientBoostingRegressor(
    n_estimators=200, learning_rate=0.05, max_depth=3, random_state=42
)
gb.fit(X_train, y_train)
hasil.append(hitung_metrik("Gradient Boosting", y_test, gb.predict(X_test), gb.predict(X_train)))
print(hasil[-1])

# %%
tabel = pd.DataFrame(hasil)
print(tabel.to_string(index=False))
tabel.to_csv(OUT / "tabel_perbandingan_model.csv", index=False)

# %%
# Analisis overfitting
tabel["selisih_R2"] = (tabel["R2_train"] - tabel["R2_test"]).round(4)
print(tabel[["model", "R2_train", "R2_test", "selisih_R2"]].to_string(index=False))

# %%
# Kepentingan fitur dari Random Forest
penting = pd.DataFrame({
    "fitur": X_train.columns,
    "importance": rf.feature_importances_,
}).sort_values("importance", ascending=False)

print(penting.head(15).to_string(index=False))
penting.to_csv(OUT / "feature_importance.csv", index=False)

# %%
# Simpan model terbaik berdasarkan MAE terkecil, selain baseline
tanpa_baseline = tabel[tabel["model"] != "Baseline (rata-rata)"].copy()
nama_terbaik = tanpa_baseline.sort_values("MAE").iloc[0]["model"]
peta = {"Ridge": ridge, "Random Forest": rf, "Gradient Boosting": gb}
model_terbaik = peta[nama_terbaik]

joblib.dump(model_terbaik, MODEL / "best_model.pkl")
json.dump({"model": nama_terbaik, "fitur": komposisi},
          open(MODEL / "model_info.json", "w"), indent=1)
print("Model terbaik:", nama_terbaik)
print("Jumlah fitur :", len(komposisi))
print("Tersimpan:", MODEL / "best_model.pkl")

# %%
# Cek prediksi satu contoh
contoh = X_test.iloc[[0]]
print("Prediksi :", round(float(model_terbaik.predict(contoh)[0]), 3))
print("Aktual   :", round(float(y_test.iloc[0]), 3))
