# %% [markdown]
# # 02 - Praproses Data
# Filter, buang kolom bocor, ubah teks jadi angka, ekstrak konsentrasi.

# %%
import pandas as pd
import numpy as np
import re
from pathlib import Path

ROOT = Path.cwd().parent if Path.cwd().name == "notebook" else Path.cwd()
DATA = ROOT / "data" / "perfumes.csv"
OUT = ROOT / "data"

df = pd.read_csv(DATA)
print("Data mentah:", df.shape)

import warnings
warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)

# %%
# Tahap 1, filter vote_count minimal 500
df = df[df["vote_count"] >= 500].copy()
df = df[df["longevity_avg"].notna()].copy()
df = df.reset_index(drop=True)
print("Setelah filter:", df.shape)

# %%
# Tahap 2, buang kolom yang membocorkan jawaban
bocor = ["longevity_b1", "longevity_b2", "longevity_b3", "longevity_b4", "longevity_b5"]
bocor += ["sillage_avg"] + [f"sillage_b{i}" for i in range(1, 6)]
bocor += ["rating_avg"] + [f"rating_b{i}" for i in range(1, 6)]
bocor += ["price_value_avg"] + [f"price_value_b{i}" for i in range(1, 6)]
bocor = [c for c in bocor if c in df.columns]
df = df.drop(columns=bocor)
print("Kolom dibuang:", len(bocor))
print("Sisa kolom   :", df.shape[1])

# %%
# Tahap 3, isi nilai hilang kolom year dengan median
print("year hilang sebelum:", int(df["year"].isna().sum()))
median_year = int(df["year"].median())
df["year"] = df["year"].fillna(median_year)
print("Median year        :", median_year)
print("year hilang sesudah:", int(df["year"].isna().sum()))

# %%
# Tahap 4, ekstraksi tingkat konsentrasi dari nama dan deskripsi


def ambil_konsentrasi(teks):
    t = str(teks).lower()
    if re.search(r"extrait", t):
        return "Extrait", 5
    if re.search(r"eau de parfum|\bedp\b|\beaudeparfum\b", t):
        return "EDP", 4
    if re.search(r"eau de toilette|\bedt\b", t):
        return "EDT", 3
    if re.search(r"eau de cologne|\bedc\b|\bcologne\b", t):
        return "EDC", 2
    if re.search(r"eau fraiche|eau fraîche|eau de fraiche", t):
        return "Eau Fraiche", 1
    return "Tidak diketahui", 0


hasil = df.apply(lambda r: ambil_konsentrasi(f"{r['name']} {r['description']}"), axis=1)
df["concentration"] = [h[0] for h in hasil]
df["concentration_score"] = [h[1] for h in hasil]
df["conc_known"] = (df["concentration_score"] > 0).astype(int)

print("Cakupan konsentrasi:", round(df["conc_known"].mean() * 100, 2), "%")
print(df["concentration"].value_counts().to_string())

# %%
# Tahap 5, ubah accords menjadi kolom angka
def pecah_teks(s):
    if pd.isna(s):
        return {}
    out = {}
    for bagian in str(s).split("|"):
        if ":" in bagian:
            nama, bobot = bagian.split(":", 1)
            try:
                out[nama.strip()] = float(bobot)
            except ValueError:
                pass
    return out


df["_acc"] = df["accords"].apply(pecah_teks)
df["n_accords"] = df["_acc"].apply(len)

daftar_accord = sorted({k for d in df["_acc"] for k in d})
print("Jumlah jenis accord:", len(daftar_accord))

for a in daftar_accord:
    df[f"ac_{a.replace(' ', '_')}"] = df["_acc"].apply(lambda d: d.get(a, 0))

print("Kolom accord dibuat:", len(daftar_accord))

# %%
# Tahap 6, ubah base notes menjadi kolom angka
df["_base"] = df["notes_base"].apply(pecah_teks)
df["n_notes_base"] = df["_base"].apply(len)

daftar_base = sorted({k for d in df["_base"] for k in d})
print("Jumlah jenis base note:", len(daftar_base))

for n in daftar_base:
    df[f"nb_{n.replace(' ', '_')}"] = df["_base"].apply(lambda d: d.get(n, 0))

print("Kolom base note dibuat:", len(daftar_base))

# %%
# Tahap 7, jumlah notes per lapis
df["n_notes_top"] = df["notes_top"].apply(lambda s: 0 if pd.isna(s) else len(str(s).split("|")))
df["n_notes_middle"] = df["notes_middle"].apply(lambda s: 0 if pd.isna(s) else len(str(s).split("|")))

# %%
# Tahap 8, kolom pendukung lain
df["log_votes"] = np.log1p(df["vote_count"])
df["is_unisex"] = df["gender"].astype(str).str.lower().str.contains("unisex").astype(int)
df["is_female"] = df["gender"].astype(str).str.lower().str.contains("female").astype(int)
df["is_male"] = df["gender"].astype(str).str.lower().str.contains("male").astype(int)

kolom_numerik = ["year", "vote_count", "log_votes", "have", "want",
                 "winter", "spring", "summer", "autumn", "day", "night",
                 "is_unisex", "is_female", "is_male",
                 "concentration_score", "conc_known",
                 "n_accords", "n_notes_top", "n_notes_middle", "n_notes_base"]

df[kolom_numerik] = df[kolom_numerik].fillna(0)

# %%
# Tahap 9, susun matriks fitur
kolom_accord = [c for c in df.columns if c.startswith("ac_")]
kolom_base = [c for c in df.columns if c.startswith("nb_")]
fitur = kolom_base + kolom_accord + kolom_numerik

X = df[fitur].astype("float32")
y = df["longevity_avg"].astype("float32")

print("Jumlah fitur total :", X.shape[1])
print("  base notes       :", len(kolom_base))
print("  accords          :", len(kolom_accord))
print("  numerik          :", len(kolom_numerik))
print("Jumlah baris       :", X.shape[0])

# %%
# Tahap 10, simpan hasil
simpan = pd.concat([df[["id", "name", "brand", "concentration"]].reset_index(drop=True), X, y], axis=1)
simpan.to_csv(OUT / "clean.csv", index=False)

import json
json.dump({"kolom_fitur": fitur, "kolom_base": kolom_base, "kolom_accord": kolom_accord,
           "kolom_numerik": kolom_numerik},
          open(OUT / "feature_columns.json", "w"), indent=1)

print("Tersimpan: data/clean.csv", simpan.shape)
print("Tersimpan: data/feature_columns.json")

# %%
print("Cek nilai hilang pada X:", int(X.isna().sum().sum()))
print("Sebaran target:")
print(y.describe().round(3).to_string())
