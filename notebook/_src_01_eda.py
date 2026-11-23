# %% [markdown]
# # 01 - Exploratory Data Analysis
# Dataset: Fragrantica Perfumes
# Target: longevity_avg (skala 1-5)

# %%
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 60)

ROOT = Path.cwd().parent if Path.cwd().name == "notebook" else Path.cwd()
DATA = ROOT / "data" / "perfumes.csv"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)
print("ROOT :", ROOT)
print("DATA :", DATA.exists())

# %%
df = pd.read_csv(DATA)
print("Baris :", df.shape[0])
print("Kolom :", df.shape[1])

# %%
print("Daftar kolom:")
for i, c in enumerate(df.columns, 1):
    print(f"{i:2d}. {c}")

# %%
print("Tipe data:")
print(df.dtypes.to_string())

# %%
# Nilai hilang per kolom, hanya yang ada isinya
miss = df.isna().sum()
miss = miss[miss > 0].sort_values(ascending=False)
tbl_miss = pd.DataFrame({
    "jumlah_hilang": miss,
    "persen": (miss / len(df) * 100).round(2),
})
print(tbl_miss.to_string())
tbl_miss.to_csv(OUT / "tabel_missing.csv")

# %%
print("Baris duplikat (semua kolom):", df.duplicated().sum())
print("ID duplikat                 :", df["id"].duplicated().sum())
print("slug duplikat               :", df["slug"].duplicated().sum())

# %%
print("Statistik target longevity_avg:")
print(df["longevity_avg"].describe().round(3).to_string())

# %%
# Cek nilai 0 pada target, itu bukan nilai asli
nol = df["longevity_avg"] == 0
print("Baris longevity = 0        :", int(nol.sum()))
print("Dari situ vote_count = 0   :", int((nol & (df["vote_count"] == 0)).sum()))
print("Persen dari seluruh data   :", round(nol.mean() * 100, 2), "%")
print("Nilai minimum selain 0     :", round(df.loc[~nol, "longevity_avg"].min(), 2))

# %%
# Tabel ambang vote_count, dasar pemilihan ambang 500
baris = []
for amb in [0, 20, 100, 500, 1000, 2000, 5000]:
    sub = df[(df["vote_count"] >= amb) & (df["longevity_avg"].notna())]
    baris.append({
        "ambang_vote": amb,
        "jumlah_baris": len(sub),
        "persen_data": round(len(sub) / len(df) * 100, 2),
        "std_target": round(sub["longevity_avg"].std(), 3),
        "mean_target": round(sub["longevity_avg"].mean(), 3),
    })
tbl_vote = pd.DataFrame(baris)
print(tbl_vote.to_string(index=False))
tbl_vote.to_csv(OUT / "tabel_ambang_vote.csv", index=False)

# %%
# Histogram target pada data terfilter
sub = df[(df["vote_count"] >= 500) & (df["longevity_avg"].notna())]
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(sub["longevity_avg"], bins=30, color="#2F6F8F", edgecolor="white")
ax.set_title("Sebaran longevity_avg (vote_count >= 500)")
ax.set_xlabel("longevity_avg (1-5)")
ax.set_ylabel("Jumlah parfum")
fig.tight_layout()
fig.savefig(OUT / "fig_hist_longevity.png", dpi=150)
plt.close(fig)
print("Tersimpan:", OUT / "fig_hist_longevity.png")
print("Skewness:", round(sub["longevity_avg"].skew(), 3))

# %%
# Korelasi antar kolom numerik utama, dihitung pada data terfilter
num = ["longevity_avg", "sillage_avg", "rating_avg", "price_value_avg",
       "vote_count", "year", "have", "want", "winter", "summer"]
koor = sub[num].corr(numeric_only=True).round(3)
print(koor.to_string())
koor.to_csv(OUT / "tabel_korelasi.csv")

fig, ax = plt.subplots(figsize=(7.5, 6))
im = ax.imshow(koor.values, cmap="RdBu_r", vmin=-1, vmax=1)
ax.set_xticks(range(len(num))); ax.set_xticklabels(num, rotation=45, ha="right", fontsize=8)
ax.set_yticks(range(len(num))); ax.set_yticklabels(num, fontsize=8)
for i in range(len(num)):
    for j in range(len(num)):
        ax.text(j, i, koor.values[i, j], ha="center", va="center", fontsize=7)
fig.colorbar(im, ax=ax, shrink=0.8)
fig.tight_layout()
fig.savefig(OUT / "fig_korelasi.png", dpi=150)
plt.close(fig)
print("Tersimpan:", OUT / "fig_korelasi.png")

# %%
# Bentuk data teks yang harus diubah jadi angka
print("Contoh accords   :", df["accords"].dropna().iloc[0])
print("Contoh notes_top :", df["notes_top"].dropna().iloc[0])
print("Contoh notes_base:", df["notes_base"].dropna().iloc[0])

# %%
print("Jumlah jenis accord unik :", df["accords"].dropna().str.split("|").explode().str.split(":").str[0].nunique())
print("Jumlah parfum tanpa accords :", int(df["accords"].isna().sum()))
print("Jumlah parfum tanpa notes_base :", int(df["notes_base"].isna().sum()))

# %%
# Kesimpulan EDA
print("RINGKASAN")
print("-" * 50)
print(f"Data mentah            : {len(df):,} baris")
print(f"Tanpa vote             : {int((df['vote_count'] == 0).sum()):,} baris")
print(f"Target bernilai 0 palsu: {int(nol.sum()):,} baris")
print(f"Setelah filter >= 500  : {len(sub):,} baris")
print(f"std target sesudahnya  : {sub['longevity_avg'].std():.3f}")
print(f"Korelasi sillage       : {koor.loc['longevity_avg', 'sillage_avg']:.3f} (bocor)")
