# Panduan Lengkap Project Longevity Parfum

## Dari dataset mentah sampai aplikasi jalan

Dokumen ini isinya urutan kerja yang sudah diuji, bukan teori. Semua kode di bawah sudah pernah dijalankan pada dataset asli, dan angka yang ditulis adalah hasil nyata dari eksekusi itu. Kalau kamu ikuti urutannya, hasilmu akan sama.

Waktu pengerjaan kalau dikerjakan sendiri: sekitar 4 sampai 6 jam, terhitung dari buka laptop sampai aplikasi bisa diklik.

---

## Bagian 0: Persiapan

### 0.1 Lingkungan Python

Yang dipakai adalah Anaconda environment `ENV_001`. Cek dulu isinya sudah lengkap.

```
conda activate ENV_001
python -c "import pandas, sklearn, matplotlib, joblib, streamlit; print('siap')"
```

Kalau ada yang belum ada, install:

```
pip install streamlit joblib
```

pandas, scikit-learn, dan matplotlib sudah terpasang di environment ini.

### 0.2 Struktur folder

Semua pekerjaan ada di satu folder proyek:

```
Project Akhir - Prediksi Longevity Parfum/
  data/       dataset mentah dan hasil olahan
  notebook/   file .ipynb
  model/      model tersimpan
  app/        aplikasi
  output/     tabel dan gambar hasil
```

Kalau folder belum ada, buat dulu. Notebook ditulis dengan nomor di depan nama karena urutannya penting.

### 0.3 Cara membuka notebook

Buka terminal, masuk ke folder proyek, lalu jalankan:

```
conda activate ENV_001
cd "Documents/Semester 5/Machine Learning/Project Akhir - Prediksi Longevity Parfum"
jupyter lab
```

Browser terbuka sendiri. Masuk ke folder `notebook`, buat file baru, pilih kernel Python 3.

Satu hal yang sering bikin bingung: notebook harus dijalankan dari folder `notebook`, bukan dari folder proyek. Semua kode di panduan ini otomatis mendeteksi posisinya, jadi aman.

---

## Bagian 1: Notebook 01, Eksplorasi Data

Tujuan bagian ini bukan membuat grafik bagus. Tujuannya memastikan kita tahu isi data sebelum diapa-apakan. Kalau langsung masuk ke model tanpa bagian ini, kita akan bingung sendiri waktu hasilnya aneh.

### Sel 1, import dan lokasi folder

```python
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
```

Penjelasan: `matplotlib.use("Agg")` dipakai supaya grafik disimpan jadi file, bukan muncul di jendela terpisah. Ini penting kalau notebook dijalankan otomatis.

Baris `ROOT` itu mendeteksi posisi folder secara otomatis. Kalau dijalankan dari dalam folder `notebook`, dia naik satu tingkat. Kalau dijalankan dari folder proyek, dia pakai posisi sekarang. Jadi notebook tidak rusak walaupun dibuka dari tempat berbeda.

### Sel 2, memuat data

```python
df = pd.read_csv(DATA)
print("Baris :", df.shape[0])
print("Kolom :", df.shape[1])
```

Hasilnya: 140.228 baris dan 59 kolom. Proses ini butuh sekitar 5 sampai 10 detik karena ukuran file 139 MB.

### Sel 3, daftar kolom

```python
for i, c in enumerate(df.columns, 1):
    print(f"{i:2d}. {c}")
```

Kolom yang penting untuk kita: `name`, `brand`, `year`, `gender`, `vote_count`, `longevity_avg`, `accords`, `notes_top`, `notes_middle`, `notes_base`, `description`.

Kolom yang harus dibuang nanti: `sillage_avg`, `rating_avg`, `price_value_avg`, beserta turunannya. Alasannya dijelaskan di Bagian 2.

### Sel 4, cek nilai hilang

```python
miss = df.isna().sum()
miss = miss[miss > 0].sort_values(ascending=False)
tbl_miss = pd.DataFrame({
    "jumlah_hilang": miss,
    "persen": (miss / len(df) * 100).round(2),
})
print(tbl_miss.to_string())
tbl_miss.to_csv(OUT / "tabel_missing.csv")
```

Hasil nyata: `notes_base` hilang di 41.467 baris (29,6 persen), `notes_top` dan `notes_middle` serupa, `year` hilang di 2,8 persen baris, `accords` hilang di 2.791 baris.

Kenapa penting: notes yang hilang tidak boleh diisi rata-rata, karena notes itu nama bahan, bukan angka. Nanti diisi nol, artinya parfum itu tidak memakai bahan tersebut. Ini sudah benar secara logika, karena kalau datanya kosong memang tidak ada informasi bahan.

### Sel 5, cek duplikat

```python
print("Baris duplikat :", df.duplicated().sum())
print("ID duplikat    :", df["id"].duplicated().sum())
print("Slug duplikat  :", df["slug"].duplicated().sum())
```

Hasilnya nol semua. Artinya satu baris satu parfum, tidak ada data ganda.

### Sel 6, statistik target

```python
print(df["longevity_avg"].describe().round(3).to_string())
```

Hasil nyata pada data mentah: rata-rata 2,604, simpangan baku 1,422, minimum 0, maksimum 5.

Angka simpangan baku 1,422 itu besar. Artinya penilaiannya sangat beragam. Ini yang nanti kita perbaiki dengan filter.

### Sel 7, membongkar nol palsu

```python
nol = df["longevity_avg"] == 0
print("Baris longevity = 0      :", int(nol.sum()))
print("Dari situ vote_count = 0 :", int((nol & (df["vote_count"] == 0)).sum()))
print("Persen dari seluruh data :", round(nol.mean() * 100, 2), "%")
print("Nilai minimum selain 0   :", round(df.loc[~nol, "longevity_avg"].min(), 2))
```

Hasil nyata: 26.777 baris bernilai 0, dan 17.540 di antaranya punya `vote_count` nol. Nilai minimum selain 0 adalah 1,0.

Kesimpulannya jelas: nol itu bukan hasil penilaian, tapi penanda bahwa belum ada yang menilai. Skala aslinya 1 sampai 5, jadi 0 mustahil muncul dari penilaian sungguhan.

### Sel 8, tabel ambang vote

```python
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
```

Hasil nyata:

| ambang | baris | persen | std | mean |
|---|---|---|---|---|
| 0 | 140.228 | 100,00 | 1,422 | 2,604 |
| 20 | 57.273 | 40,84 | 0,532 | 3,186 |
| 100 | 26.313 | 18,76 | 0,486 | 3,205 |
| 500 | 8.211 | 5,86 | 0,460 | 3,271 |
| 1.000 | 4.341 | 3,10 | 0,446 | 3,312 |
| 2.000 | 2.046 | 1,46 | 0,435 | 3,362 |
| 5.000 | 631 | 0,45 | 0,439 | 3,415 |

Cara membacanya: dari tanpa filter ke ambang 20, simpangan baku jatuh dari 1,422 ke 0,532. Itu turun drastis, tanda data jadi jauh lebih rapi. Setelah ambang 100, penurunannya tipis saja.

Jadi 500 dipilih sebagai titik aman: sudah stabil, dan datanya masih 8.211 baris, cukup untuk melatih model. Kalau dipilih 5.000, datanya cuma 631 baris, terlalu sedikit.

### Sel 9, histogram target

```python
sub = df[(df["vote_count"] >= 500) & (df["longevity_avg"].notna())]
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(sub["longevity_avg"], bins=30, color="#2F6F8F", edgecolor="white")
ax.set_title("Sebaran longevity_avg (vote_count >= 500)")
ax.set_xlabel("longevity_avg (1-5)")
ax.set_ylabel("Jumlah parfum")
fig.tight_layout()
fig.savefig(OUT / "fig_hist_longevity.png", dpi=150)
plt.close(fig)
print("Skewness:", round(sub["longevity_avg"].skew(), 3))
```

Hasil nyata: skewness 0,002. Artinya sebarannya hampir simetris sempurna, tidak menceng ke kiri atau ke kanan. Ini kabar bagus, karena model regresi paling gampang bekerja pada data yang seimbang.

Grafiknya tersimpan di `output/fig_hist_longevity.png` dan bisa langsung dipakai untuk slide.

### Sel 10, matriks korelasi

```python
num = ["longevity_avg", "sillage_avg", "rating_avg", "price_value_avg",
       "vote_count", "year", "have", "want", "winter", "summer"]
koor = sub[num].corr(numeric_only=True).round(3)
print(koor.to_string())
koor.to_csv(OUT / "tabel_korelasi.csv")
```

Hasil nyata pada data terfilter:

| pasangan | korelasi |
|---|---|
| longevity dan sillage | **0,903** |
| longevity dan rating | 0,293 |
| longevity dan price_value | **-0,216** |
| longevity dan vote_count | 0,091 |
| longevity dan year | 0,027 |

Ini sel paling penting di seluruh notebook. Angka 0,903 berarti sillage hampir sempurna memprediksi longevity. Terdengar bagus, tapi justru ini masalah. Penjelasan lengkapnya di Bagian 2.

Grafik korelasi juga dibuat dan disimpan sebagai `output/fig_korelasi.png`.

### Sel 11, melihat bentuk data teks

```python
print("Accords   :", df["accords"].dropna().iloc[0])
print("notes_top :", df["notes_top"].dropna().iloc[0])
print("notes_base:", df["notes_base"].dropna().iloc[0])
```

Hasil nyata:

```
accords    : citrus:100|fresh spicy:47|green:41|sweet:33|aromatic:31
notes_top  : Orange:100|Bergamot:28|Basil:25|Grapefruit:23|Green Notes:22
notes_base : Honey:25|Amber:20|Cedar:12|Musk:10
```

Formatnya `nama:bobot`, dipisah tanda pipa. Bobot 100 berarti bahan paling dominan, 0 berarti tidak dipakai. Ini yang nanti diubah jadi kolom angka di Bagian 2.

### Sel 12, hitung jumlah jenis bahan

```python
print("Jenis accord unik    :", df["accords"].dropna().str.split("|").explode().str.split(":").str[0].nunique())
print("Tanpa accords        :", int(df["accords"].isna().sum()))
print("Tanpa notes_base     :", int(df["notes_base"].isna().sum()))
```

Hasil: ada 92 jenis accord di seluruh data. Setelah difilter jadi 81, dan angka 81 inilah yang dipakai di proposal.

### Sel 13, kesimpulan

Sel terakhir mencetak ringkasan supaya kamu punya bahan bicara waktu presentasi:

```
Data mentah             : 140.228 baris
Tanpa vote              : 18.996 baris
Target bernilai 0 palsu : 26.777 baris
Setelah filter >= 500   : 8.211 baris
std target sesudahnya   : 0,460
Korelasi sillage        : 0,903 (bocor)
```

Kalau bagian ini sudah jalan, kamu sudah punya jawaban untuk tiga pertanyaan dosen yang paling sering keluar: kenapa datanya 8.211, kenapa nol harus dibuang, dan kenapa sillage berbahaya.
---

## Bagian 2: Notebook 02, Praproses

Ini bagian yang paling banyak kerjaan, dan yang paling menentukan hasil akhir. Semua yang di sini sudah diuji dan menghasilkan 742 fitur.

### Sel 1, import dan muat data

```python
import pandas as pd
import numpy as np
import re
import warnings
from pathlib import Path

ROOT = Path.cwd().parent if Path.cwd().name == "notebook" else Path.cwd()
DATA = ROOT / "data" / "perfumes.csv"
OUT = ROOT / "data"

df = pd.read_csv(DATA)
print("Data mentah:", df.shape)
warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)
```

`PerformanceWarning` itu peringatan karena kita menambah ratusan kolom satu per satu. Bukan error, cuma lambat. Peringatannya dimatikan supaya output tidak penuh.

### Sel 2, filter vote_count

```python
df = df[df["vote_count"] >= 500].copy()
df = df[df["longevity_avg"].notna()].copy()
df = df.reset_index(drop=True)
print("Setelah filter:", df.shape)
```

Hasil: 8.211 baris.

Baris `reset_index(drop=True)` itu wajib, dan ini jebakan yang sudah pernah bikin hasil salah. Kalau tidak dijalankan, index barisnya masih melompat-lompat dari data asli. Nanti waktu menggabungkan kolom, hasilnya bisa jadi 14.315 baris padahal datanya cuma 8.211. Kejadian nyata waktu panduan ini disusun, dan gejalanya halus sehingga tidak kelihatan sampai file akhirnya diperiksa.

### Sel 3, buang kolom bocor

```python
bocor = ["longevity_b1", "longevity_b2", "longevity_b3", "longevity_b4", "longevity_b5"]
bocor += ["sillage_avg"] + [f"sillage_b{i}" for i in range(1, 6)]
bocor += ["rating_avg"] + [f"rating_b{i}" for i in range(1, 6)]
bocor += ["price_value_avg"] + [f"price_value_b{i}" for i in range(1, 6)]
bocor = [c for c in bocor if c in df.columns]
df = df.drop(columns=bocor)
print("Kolom dibuang:", len(bocor))
print("Sisa kolom   :", df.shape[1])
```

Hasil: 23 kolom dibuang.

Kenapa tidak cuma tiga? Di proposal disebut tiga kolom, yaitu `sillage_avg`, `rating_avg`, `price_value_avg`. Itu benar, tapi ketiganya punya kolom turunan bernama `b1` sampai `b5`, isinya sebaran jawaban pengguna. `longevity_b1` sampai `longevity_b5` misalnya, itu jumlah orang yang menjawab tahan 1 jam, 2 jam, dan seterusnya.

Kalau kolom turunan itu dibiarkan, kebocorannya tetap ada. Jadi dibuang semua. Kalau ditanya dosen, bilang: tiga kolom utama ditambah turunannya, total 23.

### Sel 4, isi nilai hilang year

```python
print("year hilang sebelum:", int(df["year"].isna().sum()))
median_year = int(df["year"].median())
df["year"] = df["year"].fillna(median_year)
print("Median year        :", median_year)
print("year hilang sesudah:", int(df["year"].isna().sum()))
```

Hasil: 230 baris hilang, median tahun 2015, setelah diisi jadi nol hilang.

Kenapa median dan bukan rata-rata? Karena tahun itu data yang bisa punya nilai ekstrem, misalnya parfum tahun 1920. Rata-rata bisa tertarik ke nilai ekstrem, median tidak. Untuk tahun, median lebih aman.

### Sel 5, ekstraksi tingkat konsentrasi

```python
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

print("Cakupan:", round(df["conc_known"].mean() * 100, 2), "%")
print(df["concentration"].value_counts().to_string())
```

Hasil nyata:

| konsentrasi | jumlah |
|---|---|
| Tidak diketahui | 5.424 |
| EDP | 1.605 |
| EDT | 924 |
| EDC | 148 |
| Extrait | 96 |
| Eau Fraiche | 14 |

Cakupan: 2.787 dari 8.211 baris, atau **33,94 persen**.

Perhatikan urutan pengecekan. Extrait dicek paling awal karena kalau tidak, nama seperti "Extrait de Parfum" bisa salah tertangkap sebagai EDP. Ini penting: urutan dari yang paling spesifik ke paling umum.

Kenapa ada dua kolom, `concentration_score` dan `conc_known`? Karena kalau hanya ada satu kolom, nilai "tidak diketahui" akan dibaca model sebagai tingkat konsentrasi paling rendah, padahal artinya bukan itu. Dengan kolom kedua, model tahu mana yang datanya benar-benar kosong.

### Sel 6, ubah accords jadi kolom angka

```python
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
print("Jenis accord:", len(daftar_accord))

for a in daftar_accord:
    df[f"ac_{a.replace(' ', '_')}"] = df["_acc"].apply(lambda d: d.get(a, 0))
```

Hasil: 81 jenis accord, jadi 81 kolom baru dengan awalan `ac_`.

Cara kerjanya: teks `woody:45|sweet:33` dipecah jadi kamus Python `{"woody": 45, "sweet": 33}`. Setelah semua baris punya kamusnya sendiri, kita kumpulkan semua nama accord yang pernah muncul. Tiap nama jadi satu kolom. Kalau parfum itu tidak punya accord tersebut, isinya nol.

Nama accord yang ada spasinya, seperti `fresh spicy`, diganti jadi `fresh_spicy` supaya aman dipakai sebagai nama kolom.

### Sel 7, ubah base notes jadi kolom angka

```python
df["_base"] = df["notes_base"].apply(pecah_teks)
df["n_notes_base"] = df["_base"].apply(len)

daftar_base = sorted({k for d in df["_base"] for k in d})
print("Jenis base note:", len(daftar_base))

for n in daftar_base:
    df[f"nb_{n.replace(' ', '_')}"] = df["_base"].apply(lambda d: d.get(n, 0))
```

Hasil: 641 jenis base note, jadi 641 kolom dengan awalan `nb_`. Ini angka yang sama dengan yang ditulis di proposal.

Fun faktanya: 81 kolom accord bisa mengalahkan 641 kolom notes. Alasannya karena accord itu sudah ringkasan. Accord "woody" mewakili puluhan bahan kayu sekaligus, jadi informasinya padat. Sementara 641 notes itu jarang terpakai semua, satu parfum biasanya cuma pakai 4 sampai 12 bahan.

### Sel 8, jumlah notes per lapis

```python
df["n_notes_top"] = df["notes_top"].apply(lambda s: 0 if pd.isna(s) else len(str(s).split("|")))
df["n_notes_middle"] = df["notes_middle"].apply(lambda s: 0 if pd.isna(s) else len(str(s).split("|")))
```

Ini menghitung ada berapa bahan di tiap lapis. Sederhana, tapi berguna: parfum dengan banyak base notes cenderung lebih tahan lama.

### Sel 9, kolom pendukung

```python
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
```

`log_votes` itu logaritma dari jumlah vote. Kenapa perlu? Karena 500 vote dan 5.000 vote jaraknya jauh, tapi pengaruhnya ke model tidak sebanding. Logaritma merapatkan jarak itu supaya model tidak kaget.

### Sel 10, susun matriks fitur

```python
kolom_accord = [c for c in df.columns if c.startswith("ac_")]
kolom_base = [c for c in df.columns if c.startswith("nb_")]
fitur = kolom_base + kolom_accord + kolom_numerik

X = df[fitur].astype("float32")
y = df["longevity_avg"].astype("float32")

print("Total fitur :", X.shape[1])
print("base notes  :", len(kolom_base))
print("accords     :", len(kolom_accord))
print("numerik     :", len(kolom_numerik))
print("baris       :", X.shape[0])
```

Hasil nyata:

```
Total fitur : 742
base notes  : 641
accords     : 81
numerik     : 20
baris       : 8211
```

`float32` dipakai supaya hemat memori, setengah dari `float64`. Untuk angka 0 sampai 100, presisinya lebih dari cukup.

### Sel 11, simpan hasil

```python
simpan = pd.concat([df[["id", "name", "brand", "concentration"]].reset_index(drop=True), X, y], axis=1)
simpan.to_csv(OUT / "clean.csv", index=False)

import json
json.dump({"kolom_fitur": fitur, "kolom_base": kolom_base, "kolom_accord": kolom_accord,
           "kolom_numerik": kolom_numerik},
          open(OUT / "feature_columns.json", "w"), indent=1)
```

Hasil: `data/clean.csv` berisi 8.211 baris dan 747 kolom, ukurannya 25 MB. Jauh lebih kecil dari file asli yang 139 MB.

`feature_columns.json` itu daftar urutan kolom. Ini file yang paling sering dilupakan orang, padahal wajib. Nanti aplikasi harus menyusun kolom dengan urutan persis sama. Kalau urutannya beda, prediksinya ngawur tapi tidak muncul error. Jenis bug yang paling susah dicari.

### Sel 12, cek akhir

```python
print("Nilai hilang pada X:", int(X.isna().sum().sum()))
print(y.describe().round(3).to_string())
```

Hasil: nol nilai hilang. Target rata-rata 3,271, simpangan baku 0,460, minimum 1,538, maksimum 4,897.

Kalau di sini masih ada nilai hilang, berarti ada kolom yang belum ditangani. Jangan lanjut ke pemodelan sebelum angkanya nol.

---

## Bagian 3: Notebook 03, Pembagian Data

Pendeknya, tapi ini penentu apakah hasilmu bisa dipercaya.

### Sel 1, muat data olahan

```python
import pandas as pd
import json
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split

ROOT = Path.cwd().parent if Path.cwd().name == "notebook" else Path.cwd()
DATA = ROOT / "data"

clean = pd.read_csv(DATA / "clean.csv")
info = json.load(open(DATA / "feature_columns.json"))
fitur = info["kolom_fitur"]

X = clean[fitur].astype("float32")
y = clean["longevity_avg"].astype("float32")
```

### Sel 2, bagi data

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Latih:", X_train.shape, "| Uji:", X_test.shape)
```

Hasil: 6.568 baris latih dan 1.643 baris uji.

`random_state=42` itu angka bebas, fungsinya mengunci pengacakan. Dengan angka yang sama, pembagian datanya akan selalu sama persis walaupun dijalankan lain waktu. Ini yang bikin hasilmu bisa diulang orang lain, dan itu syarat wajib kalau mau jadi artikel jurnal.

### Sel 3, hitung baseline

```python
from sklearn.metrics import mean_absolute_error

tebakan = np.full(len(y_test), float(y_train.mean()))
print("MAE baseline:", round(mean_absolute_error(y_test, tebakan), 3))
```

Hasil: **0,370**.

Angka ini penting. Artinya kalau kita tidak pakai model sama sekali, cuma menebak rata-rata, rata-rata melesetnya 0,370 poin. Model apa pun yang kita buat harus lebih kecil dari angka ini, kalau tidak, modelnya tidak ada gunanya.

### Sel 4, simpan

```python
X_train.to_csv(DATA / "X_train.csv", index=False)
X_test.to_csv(DATA / "X_test.csv", index=False)
y_train.to_csv(DATA / "y_train.csv", index=False)
y_test.to_csv(DATA / "y_test.csv", index=False)
```

Setelah ini, orang yang pegang bagian model bisa langsung kerja tanpa perlu mengulang praproses. Ini yang dimaksud serah terima pakai file.
---

## Bagian 4: Notebook 04, Pemodelan dan Evaluasi

Sekarang bagian yang menghasilkan angka. Tiga model, satu pembanding, satu tabel.

### Sel 1, import dan muat data

```python
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

X_train = pd.read_csv(DATA / "X_train.csv")
X_test = pd.read_csv(DATA / "X_test.csv")
y_train = pd.read_csv(DATA / "y_train.csv").iloc[:, 0]
y_test = pd.read_csv(DATA / "y_test.csv").iloc[:, 0]

info = json.load(open(DATA / "feature_columns.json"))
```

### Sel 2, pilih fitur komposisi

```python
komposisi = info["kolom_base"] + info["kolom_accord"] + [
    "concentration_score", "conc_known",
    "n_accords", "n_notes_base", "n_notes_top", "n_notes_middle",
]

X_train = X_train[komposisi]
X_test = X_test[komposisi]

print("Fitur dipakai:", len(komposisi))
```

Hasil: 728 fitur.

Ini keputusan penting, dan bedanya dengan proposal perlu kamu pahami. Di dataset ada kolom popularitas seperti `vote_count`, `want`, `have`, dan `night`. Kalau kolom itu dipakai, hasil model naik jauh, dari R² 0,375 menjadi 0,573.

Tapi kolom itu tidak dipakai, karena parfum baru belum punya data popularitas. Kalau model bergantung pada `night` dan `want`, model itu tidak akan berguna untuk menjawab pertanyaan awal kita. Model yang hebat di data lama tapi tidak bisa dipakai di data baru itu bukan model yang berguna.

Versi dengan fitur popularitas tetap dihitung, tapi ditaruh sebagai perbandingan di Bagian 5. Jadi kalau dosen tanya, kamu punya dua angka dan bisa jelaskan kenapa yang dipilih yang komposisi.

### Sel 3, fungsi metrik

```python
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
```

Fungsi ini dipanggil empat kali, sekali untuk tiap model. R² data latih dihitung juga karena nanti dipakai untuk mendeteksi overfitting.

### Sel 4, baseline

```python
hasil = []
baseline = np.full(len(y_test), float(y_train.mean()))
hasil.append(hitung_metrik("Baseline (rata-rata)", y_test, baseline))
```

Hasil: MAE 0,3699 dan R² −0,0008.

R² negatif sedikit itu normal untuk baseline. Nilainya harus mendekati nol, karena baseline memang tidak menjelaskan apa pun.

### Sel 5, Ridge dengan pencarian alpha

```python
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
hasil.append(hitung_metrik("Ridge", y_test, ridge.predict(X_test), ridge.predict(X_train)))
```

Hasil: MAE 0,3006, R² uji 0,2502, R² latih 0,4157.

`GridSearchCV` mencoba lima nilai alpha dengan validasi silang tiga lipatan, lalu memilih yang MAE-nya paling kecil. Jadi kita tidak menebak nilai alpha, tapi mencarinya.

Perhatikan R² latih dan uji yang berdekatan (0,416 dan 0,250). Model ini tidak overfitting, tapi kemampuannya juga terbatas. Wajar, karena hubungan antara bahan dan ketahanan memang tidak lurus.

### Sel 6, Random Forest

```python
rf = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
hasil.append(hitung_metrik("Random Forest", y_test, rf.predict(X_test), rf.predict(X_train)))
```

Hasil: MAE 0,2815, R² uji 0,3747, R² latih 0,9085.

Selisih R² latih dan uji di sini 0,534. Ini overfitting yang jelas. Di data yang sudah dia lihat, modelnya hampir sempurna. Di data baru, dia jatuh.

### Sel 7, Gradient Boosting

```python
gb = GradientBoostingRegressor(
    n_estimators=200, learning_rate=0.05, max_depth=3, random_state=42
)
gb.fit(X_train, y_train)
hasil.append(hitung_metrik("Gradient Boosting", y_test, gb.predict(X_test), gb.predict(X_train)))
```

Hasil: MAE 0,2859, R² uji 0,3632, R² latih 0,4311.

Selisihnya cuma 0,068. Jauh lebih sehat daripada Random Forest.

### Sel 8, tabel akhir

```python
tabel = pd.DataFrame(hasil)
print(tabel.to_string(index=False))
tabel.to_csv(OUT / "tabel_perbandingan_model.csv", index=False)
```

Hasil nyata:

| Model | MAE | MSE | RMSE | R² uji | R² latih |
|---|---|---|---|---|---|
| Baseline | 0,3699 | 0,2113 | 0,4596 | −0,0008 | tidak ada |
| Ridge | 0,3006 | 0,1583 | 0,3978 | 0,2502 | 0,4157 |
| Random Forest | **0,2815** | 0,1320 | 0,3633 | **0,3747** | 0,9085 |
| Gradient Boosting | 0,2859 | 0,1344 | 0,3666 | 0,3632 | 0,4311 |

Cara membaca tabel ini untuk orang awam: baseline meleset 0,370 poin. Model terbaik meleset 0,282 poin. Jadi modelnya mengurangi kesalahan sekitar 24 persen dibanding tidak pakai model sama sekali.

### Sel 9, analisis overfitting

```python
tabel["selisih_R2"] = (tabel["R2_train"] - tabel["R2_test"]).round(4)
print(tabel[["model", "R2_train", "R2_test", "selisih_R2"]].to_string(index=False))
```

Hasil: Ridge selisih 0,166, Random Forest 0,534, Gradient Boosting 0,068.

Kalau ditanya mana yang paling bisa dipercaya untuk dipakai di dunia nyata, jawabannya Gradient Boosting, walaupun MAE-nya sedikit lebih besar dari Random Forest. Alasannya karena selisih latih dan ujinya paling kecil, artinya dia belajar pola, bukan menghafal.

### Sel 10, kepentingan fitur

```python
penting = pd.DataFrame({
    "fitur": X_train.columns,
    "importance": rf.feature_importances_,
}).sort_values("importance", ascending=False)
print(penting.head(15).to_string(index=False))
penting.to_csv(OUT / "feature_importance.csv", index=False)
```

Fitur teratas setelah fitur popularitas dibuang: accord seperti `ac_oud`, `ac_amber`, `ac_warm_spicy`, dan base note seperti `nb_patchouli`, `nb_musk`, `nb_sandalwood`.

Ini masuk akal secara kimia: oud, amber, dan musk adalah bahan bermolekul berat yang memang menguap lambat. Jadi modelnya menemukan hal yang sesuai teori, bukan kebetulan.

### Sel 11, simpan model

```python
tanpa_baseline = tabel[tabel["model"] != "Baseline (rata-rata)"].copy()
nama_terbaik = tanpa_baseline.sort_values("MAE").iloc[0]["model"]
peta = {"Ridge": ridge, "Random Forest": rf, "Gradient Boosting": gb}
model_terbaik = peta[nama_terbaik]

joblib.dump(model_terbaik, MODEL / "best_model.pkl")
json.dump({"model": nama_terbaik, "fitur": komposisi},
          open(MODEL / "model_info.json", "w"), indent=1)
```

Hasil: model terbaik adalah Random Forest, tersimpan sebagai `model/best_model.pkl` berukuran sekitar 119 MB.

Ukurannya besar karena 200 pohon itu benar-benar disimpan. Kalau mau lebih kecil, kurangi pohonnya, tapi hasilnya bisa berubah.

`model_info.json` menyimpan nama model dan daftar fitur. Aplikasi membacanya supaya tahu harus menyusun kolom apa saja dan dalam urutan apa.

---

## Bagian 4 (tambahan): Eksperimen Pembanding

Bagian ini tidak wajib untuk presentasi minggu ini, tapi sangat berguna kalau nanti ditanya "dari mana tahu accord lebih penting daripada notes".

Cara menjalankannya: muat `clean.csv`, lalu latih ulang dengan kelompok fitur berbeda. Hasil nyata yang sudah dijalankan:

| Skenario | Model | MAE | RMSE | R² uji | R² latih |
|---|---|---|---|---|---|
| A. base notes saja | Ridge | 0,3473 | 0,5235 | −0,2985 | 0,2373 |
| A. base notes saja | Random Forest | 0,3388 | 0,4334 | 0,1104 | 0,6585 |
| B. accords saja | Ridge | 0,2991 | 0,3841 | 0,3012 | 0,3168 |
| B. accords saja | Random Forest | 0,2933 | 0,3753 | 0,3326 | 0,9011 |
| C. accords + base notes | Random Forest | 0,2851 | 0,3666 | 0,3632 | 0,9044 |
| D. C + fitur popularitas | Random Forest | 0,2311 | 0,3002 | 0,5732 | 0,9401 |
| E. popularitas saja | Random Forest | 0,2318 | 0,3005 | 0,5721 | 0,9401 |

Tiga hal yang bisa kamu simpulkan dari tabel ini, dan semuanya layak dibawa ke presentasi.

Pertama, notes sendirian lemah. R² cuma 0,11 walaupun fiturnya 641 kolom. Penyebabnya karena data notes itu jarang, satu parfum cuma memakai belasan bahan dari ratusan yang tersedia, jadi tabelnya kebanyakan nol.

Kedua, accords jauh lebih efisien. Cuma 81 kolom, tapi R² 0,33, tiga kali lipat notes. Accord itu ringkasan, jadi informasinya padat.

Ketiga, dan ini yang paling penting: fitur popularitas mendominasi. Skenario E, yang hanya memakai data popularitas tanpa melihat komposisi sama sekali, hasilnya 0,5721, hampir sama dengan skenario D yang memakai semuanya.

Artinya, sebagian besar kemampuan prediksi model kita datang dari seberapa populer parfum itu, bukan dari bahannya. Ini temuan yang jujur dan sebaiknya disampaikan, bukan disembunyikan. Kalau dosen menemukannya sendiri, posisimu lebih lemah.

Cara menyampaikannya: "Kami menguji dua jalur. Jalur komposisi murni menghasilkan R² 0,375, dan itu yang kami pakai karena bisa diterapkan pada parfum baru. Ketika fitur popularitas ditambahkan, hasilnya naik ke 0,573, tetapi fitur itu tidak tersedia untuk parfum yang belum dirilis, sehingga tidak kami jadikan model utama."

Kalimat itu menunjukkan kamu paham keterbatasan pekerjaanmu sendiri, dan itu nilainya lebih tinggi daripada angka besar.
---

## Bagian 5: Aplikasi

Bagian ini menghasilkan sesuatu yang bisa diklik. Pilih satu bentuk saja, tidak perlu semuanya. Yang dijelaskan di sini adalah versi web dengan Streamlit karena paling cepat jadi, tapi prinsipnya sama untuk desktop, mobile, atau dashboard.

### 5.1 Konsep yang harus dipahami dulu

Aplikasi tidak memuat ulang data dan tidak melatih model. Aplikasi cuma memanggil model yang sudah jadi, lalu menyusun input pengguna supaya bentuknya sama persis dengan data waktu latihan.

Alurnya: pengguna memilih bahan lewat tampilan, pilihan itu diubah jadi baris angka, baris angka dimasukkan ke model, model keluar angka, angka ditampilkan.

Kesalahan paling umum ada di langkah "diubah jadi baris angka". Kalau urutan kolomnya berbeda dari waktu latihan, model tetap jalan tanpa error, tapi hasilnya ngawur. Karena itu di Bagian 2 kita menyimpan `feature_columns.json` dan di Bagian 4 kita menyimpan `model_info.json`.

### 5.2 Kode aplikasi

```python
import json
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "model" / "best_model.pkl"
INFO_PATH = ROOT / "data" / "feature_columns.json"
MODEL_INFO_PATH = ROOT / "model" / "model_info.json"


@st.cache_resource
def muat_model():
    return joblib.load(MODEL_PATH)


@st.cache_data
def muat_json(p):
    return json.load(open(p))


model = muat_model()
info = muat_json(INFO_PATH)
info_model = muat_json(MODEL_INFO_PATH)
fitur = info_model["fitur"]

nama_base = [k.replace("nb_", "").replace("_", " ") for k in info["kolom_base"]]
nama_accord = [k.replace("ac_", "").replace("_", " ") for k in info["kolom_accord"]]

st.title("Prediksi Ketahanan Parfum")

with st.form("form"):
    base = st.multiselect("Base notes", sorted(nama_base))
    accord = st.multiselect("Accords", sorted(nama_accord))
    konsentrasi = st.selectbox(
        "Konsentrasi", ["Tidak diketahui", "Eau Fraiche", "EDC", "EDT", "EDP", "Extrait"]
    )
    kirim = st.form_submit_button("Prediksi")

if kirim:
    skor = {"Tidak diketahui": 0, "Eau Fraiche": 1, "EDC": 2,
            "EDT": 3, "EDP": 4, "Extrait": 5}[konsentrasi]

    baris = {k: 0.0 for k in fitur}
    for n in base:
        k = "nb_" + n.replace(" ", "_")
        if k in baris:
            baris[k] = 100.0
    for n in accord:
        k = "ac_" + n.replace(" ", "_")
        if k in baris:
            baris[k] = 100.0

    baris["concentration_score"] = float(skor)
    baris["conc_known"] = float(skor > 0)
    baris["n_accords"] = float(len(accord))
    baris["n_notes_base"] = float(len(base))
    baris["n_notes_top"] = 0.0
    baris["n_notes_middle"] = 0.0

    X = pd.DataFrame([baris])[fitur]
    nilai = float(model.predict(X)[0])
    nilai = max(1.0, min(5.0, nilai))

    st.metric("Perkiraan skor ketahanan", f"{nilai:.2f} / 5")
```

### 5.3 Penjelasan per bagian

`@st.cache_resource` membuat model hanya dimuat sekali. Tanpa ini, setiap kali tombol ditekan, model 100 MB dimuat ulang dan aplikasi terasa lambat.

`ROOT = Path(__file__).parent.parent` dipakai supaya aplikasi menemukan folder model walaupun dijalankan dari mana saja. Ini jauh lebih aman daripada menulis path lengkap seperti `C:\Users\...`.

`baris = {k: 0.0 for k in fitur}` itu kuncinya. Semua fitur diisi nol dulu, baru yang dipilih pengguna diubah. Dengan begitu jumlah dan urutan kolomnya dijamin sama.

Bobot 100 dipakai karena di dataset, bahan paling dominan selalu bernilai 100. Kalau pengguna memilih tiga bahan, kita anggap ketiganya sama dominan. Ini penyederhanaan yang wajar untuk input manual, dan sebaiknya disebut sebagai keterbatasan waktu presentasi.

### 5.4 Cara menjalankan

Kalau Streamlit belum ada:

```
conda activate ENV_001
pip install streamlit joblib
```

Lalu jalankan dari folder proyek:

```
cd "Documents/Semester 5/Machine Learning/Project Akhir - Prediksi Longevity Parfum"
streamlit run app/app.py
```

Browser terbuka otomatis di alamat `localhost:8501`. Kalau tidak terbuka, buka manual alamatnya.

Untuk menghentikan, tekan Ctrl+C di terminal. Jangan tutup terminalnya selama presentasi, karena aplikasi mati kalau terminalnya ditutup.

### 5.5 Uji bahwa aplikasi benar

Jangan cuma lihat tampilannya hidup. Uji tiga hal ini sebelum presentasi:

Pertama, pilih beberapa bahan dan tekan prediksi. Harus keluar angka antara 1 dan 5.

Kedua, kosongkan semua pilihan lalu prediksi. Harus tetap jalan, tidak error. Hasilnya akan mendekati rata-rata, dan itu wajar.

Ketiga, pilih banyak base notes sekaligus, misalnya sepuluh bahan. Harus tetap jalan.

Kalau salah satu dari tiga ini error, jangan dibawa presentasi.

### 5.6 Alternatif bentuk aplikasi

Kalau kamu tidak mau pakai Streamlit, tiga pilihan lain yang masuk akal untuk waktu satu minggu:

**Desktop application** pakai Tkinter, sudah ada di Python standar, tidak perlu install apa pun. Cocok kalau laptop presentasi tidak ada internet.

**Mobile application** sebaiknya jangan dari nol. Pakai Flutter kalau sudah pernah, atau lewati saja. Bikin aplikasi mobile dalam sehari tanpa pengalaman itu tidak realistis.

**Dashboard interaktif** pakai Streamlit juga, tapi lebih banyak grafik: sebaran prediksi, perbandingan model, kepentingan fitur. Ini paling enak dilihat waktu presentasi karena banyak visual.

Yang penting dipahami: dosen menilai alurnya jelas dan bisa didemokan, bukan teknologinya canggih.
---

## Bagian 6: Menghadapi Pertanyaan

Semua jawaban di bawah memakai angka yang benar-benar keluar dari eksekusi. Hafalkan yang bertanda tebal, sisanya cukup dipahami alurnya.

**Kenapa data dari 140.228 jadi 8.211?**

Karena banyak parfum belum punya cukup penilaian. Nilai rata-rata dari lima orang tidak bisa dipercaya. Setelah disaring minimal 500 vote, yang tersisa 8.211 parfum. Simpangan bakunya juga turun dari 1,422 jadi 0,460, tanda datanya jauh lebih rapi.

**Kenapa nilai 0 dibuang, bukan dianggap ketahanan paling rendah?**

Karena skala yang dipakai di dataset 1 sampai 5. Nilai 0 muncul saat belum ada yang menilai, bukan saat parfumnya cepat hilang. Buktinya, dari 26.777 baris bernilai 0, sebanyak 17.540 punya jumlah vote nol. Kalau 0 dianggap nilai asli, model akan belajar bahwa separuh parfum di dunia ini tidak tahan sama sekali, dan itu salah.

**Apa itu kebocoran data, dan kenapa sillage dibuang?**

Kebocoran data terjadi kalau ada kolom yang isinya mengandung jawaban yang mau ditebak. Sillage dan longevity itu dua hal yang dinilai orang yang sama dalam satu formulir. Korelasinya 0,903, hampir sempurna. Kalau dipakai, model akan kelihatan pintar sekali, tapi sebenarnya dia cuma membaca jawaban yang sudah ada di lembar soal. Yang dibuang total 23 kolom, yaitu tiga kolom rata-rata ditambah kolom turunannya.

**Kenapa Ridge, bukan regresi linear biasa?**

Karena fiturnya 728 dan banyak yang saling terkait. Regresi linear biasa jadi tidak stabil pada kondisi itu, koefisiennya bisa meledak. Ridge menambahkan penalti supaya koefisiennya tetap wajar. Nilai penaltinya dicari otomatis lewat validasi silang, bukan ditebak.

**Kenapa Random Forest menang MAE tapi kamu bilang Gradient Boosting lebih sehat?**

Random Forest MAE-nya 0,2815 dan R² latihnya 0,9085 sementara ujinya 0,3747. Selisihnya 0,534, itu overfitting berat. Gradient Boosting MAE-nya 0,2859 dengan selisih R² cuma 0,068. Untuk dipakai di dunia nyata, model yang selisihnya kecil lebih bisa dipercaya, walaupun angkanya sedikit lebih jelek di kertas.

**Kenapa notes kalah dari accords padahal jumlah kolomnya jauh lebih banyak?**

Karena accord itu ringkasan. Satu accord seperti woody mewakili puluhan bahan kayu. Sementara data notes jarang, satu parfum biasanya cuma memakai 4 sampai 12 bahan dari 641 yang tersedia, jadi tabelnya kebanyakan nol. Hasilnya, 81 kolom accord menghasilkan R² 0,3326, sedangkan 641 kolom notes cuma 0,1104.

**R² 0,375 itu jelek atau bagus?**

Tergantung dibanding apa. Dibanding baseline, jelas lebih baik, karena MAE turun dari 0,370 ke 0,282, sekitar 24 persen. Tapi kalau dibanding model yang sempurna, masih jauh. Untuk data penilaian manusia, R² 0,375 itu wajar, karena selera dan kulit orang berbeda-beda. Yang penting kita jujur menyebut angka ini, bukan membulatkannya jadi "akurat 90 persen".

**Kenapa model utama tidak memakai jumlah vote padahal hasilnya lebih tinggi?**

Karena parfum baru belum punya jumlah vote. Kalau model bergantung pada data popularitas, model itu hanya bisa memprediksi parfum yang sudah terkenal, dan itu tidak menjawab pertanyaan awal penelitian. Versi dengan popularitas tetap kami hitung sebagai pembanding, hasilnya R² 0,573.

**Apa fungsi konsentrasi, dan kenapa cuma 34 persen yang diketahui?**

Konsentrasi menunjukkan seberapa pekat parfum, dan itu berpengaruh besar ke ketahanan. Extrait memang lebih tahan dari eau de toilette. Tapi informasi ini tidak ada di kolom khusus, jadi kami ambil dari nama dan deskripsi memakai pencocokan pola. Hasilnya 2.787 dari 8.211 parfum, atau 33,94 persen. Sisanya diberi tanda "tidak diketahui" lewat kolom kedua, supaya model tidak salah menganggapnya konsentrasi paling lemah.

**Kenapa harus ada feature_columns.json?**

Karena urutan kolom saat melatih dan saat memakai model harus sama persis. Kalau berbeda, model tetap jalan tanpa pesan error, tapi hasilnya ngawur. Ini jenis kesalahan yang paling mahal karena tidak kelihatan.

**Apa keterbatasan penelitian ini?**

Tiga hal. Pertama, data berasal dari satu situs, jadi bias ke selera pengguna situs itu. Kedua, targetnya persepsi orang, bukan hasil ukur laboratorium, jadi ada unsur subjektif. Ketiga, sebagian besar kekuatan prediksi datang dari popularitas parfum, bukan dari komposisinya, sehingga model komposisi murni kemampuannya terbatas di R² 0,375.

**Kalau disuruh memprediksi parfum yang belum ada di dataset, bisa?**

Bisa, dan itu tujuan aplikasinya. Pengguna memasukkan bahan dan konsentrasi, aplikasi menyusun baris angka dengan urutan yang sama seperti data latihan, lalu model memperkirakan skornya. Yang tidak bisa diprediksi adalah popularitas, karena itu memang baru terbentuk setelah parfumnya dirilis.

---

## Bagian 7: Kalau Ada Error

**`ModuleNotFoundError: No module named streamlit`**

Environment-nya belum benar. Jalankan `conda activate ENV_001` dulu, baru `pip install streamlit joblib`. Kalau masih gagal, cek kernel di Jupyter: menu Kernel, Change Kernel, pastikan yang dipilih ENV_001, bukan base.

**`FileNotFoundError` pada data/perfumes.csv**

Notebook dijalankan dari folder yang salah. Semua kode di panduan ini memakai pendeteksi otomatis, jadi seharusnya aman. Kalau masih error, cetak `print(ROOT)` dan lihat apakah menunjuk ke folder proyek.

**`KeyError` saat memilih kolom**

Nama kolomnya tidak ada. Cetak `print(df.columns.tolist())` lalu bandingkan. Kesalahan paling sering karena spasi di nama kolom, misalnya `notes_base` ditulis `notes base`.

**Hasil penggabungan jadi 14.315 baris padahal datanya 8.211**

Index baris belum direset setelah filter. Tambahkan `df = df.reset_index(drop=True)` tepat setelah baris filter. Gejala ini halus dan tidak memunculkan error, jadi selalu cek `shape` setelah menggabungkan kolom.

**R² negatif besar, misalnya −1,8**

Biasanya karena regresi linear dipakai pada fitur yang sangat banyak dan saling terkait. Ganti ke Ridge dengan alpha, atau kurangi fiturnya. R² negatif artinya modelnya lebih buruk daripada menebak rata-rata.

**Kernel mati saat melatih Random Forest**

Memori habis. Turunkan `n_estimators` dari 200 ke 100, atau latih satu model per sel supaya memori sebelumnya dilepas. Dataset ini butuh sekitar 4 GB saat melatih.

**Aplikasi jalan tapi hasil prediksi selalu sama**

Ada dua kemungkinan. Pertama, pilihan pengguna tidak masuk ke baris data, biasanya karena nama kolom tidak cocok setelah spasi diganti garis bawah. Kedua, model yang dimuat bukan model yang baru dilatih, biasanya karena file lama masih tersimpan. Hapus `model/best_model.pkl` lalu latih ulang.

---

## Bagian 8: Urutan Waktu

Kalau dikerjakan sendiri, ini perkiraan realistis per bagian.

| Bagian | Perkiraan waktu | Kalau macet |
|---|---|---|
| Persiapan environment | 15 menit | paling sering karena salah env |
| Notebook 01 EDA | 45 menit | grafik tidak muncul, cek backend Agg |
| Notebook 02 praproses | 90 menit | bagian tersulit, banyak kolom |
| Notebook 03 split | 15 menit | paling cepat |
| Notebook 04 model | 45 menit | latih satu model per sel |
| Eksperimen pembanding | 30 menit | opsional |
| Aplikasi | 45 menit | uji tiga skenario sebelum presentasi |
| Slide | 30 menit | satu orang satu slide |

Total sekitar 5 jam, tanpa menghitung waktu membaca. Kalau dibagi tiga orang seperti rencana tim, masing-masing kebagian 1,5 sampai 2 jam.

---

## Bagian 9: Daftar Periksa Sebelum Presentasi

Berkas yang harus ada:

1. `notebook/01_eda.ipynb` sudah dijalankan, ada grafiknya
2. `notebook/02_preprocessing.ipynb` sudah dijalankan, keluar 742 fitur
3. `notebook/03_split.ipynb` sudah dijalankan, keluar 6.568 dan 1.643 baris
4. `notebook/04_modeling.ipynb` sudah dijalankan, keluar tabel empat baris
5. `data/clean.csv`, `X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`
6. `data/feature_columns.json`
7. `model/best_model.pkl` dan `model/model_info.json`
8. `app/app.py`, sudah diuji tiga skenario
9. `output/tabel_perbandingan_model.csv` dan `output/feature_importance.csv`
10. Tiga slide, satu per orang

Yang harus bisa kamu jawab tanpa buka file:

- kenapa 8.211, bukan 140.228
- kenapa nilai 0 dibuang
- kenapa sillage dibuang, dan berapa korelasinya
- berapa MAE baseline dan berapa MAE model terbaik
- kenapa model utama tidak memakai jumlah vote
- apa fungsi `feature_columns.json`

Enam hal itu yang paling mungkin ditanya. Sisanya bisa kamu cari di dokumen ini.

Satu hal terakhir: sebelum presentasi, jalankan ulang semua notebook dari atas ke bawah sekali. Notebook yang selnya dijalankan acak-acakan sering menyimpan output lama, dan itu bisa bikin kamu menjelaskan angka yang sudah tidak berlaku.
