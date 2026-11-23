# Fragdicted: Prediksi Ketahanan Parfum dari Komposisi

Project Akhir Pembelajaran Mesin TEK1302

**Kelas A, Kelompok 9**

| Anggota | NIM |
|---|---|
| Fattih Algie Maulana | J0404241002 |
| Aisyah Elfiyuni M.A | J0404241067 |
| Anggi Permana Putra | J0404241154 |

## Judul

Prediksi Tingkat Ketahanan (Longevity) Parfum Berdasarkan Komposisi Fragrance Notes, Accords, dan Tingkat Konsentrasi Menggunakan Perbandingan Ridge Regression, Random Forest, dan Gradient Boosting

## Ringkasan

Parfum dibeli tanpa bisa dicium lebih dulu. Ketahanannya baru diketahui setelah dipakai, padahal ketahanan itu dipengaruhi komposisi bahan. Project ini memprediksi skor ketahanan parfum pada skala 1 sampai 5 berdasarkan 126 fragrance notes, 54 accords, dan tingkat konsentrasi, lalu membandingkan tiga model regresi dan memilih satu untuk dipakai di aplikasi web.

## Dataset

| Item | Keterangan |
|---|---|
| Nama | Fragrantica Perfumes: Ratings, Notes, Votes & More |
| Penyusun | Le Decanteur |
| Sumber | https://www.kaggle.com/datasets/ledecanteur/fragrantica-perfumes |
| Lisensi | CC BY-NC-SA 4.0, atribusi wajib, non-komersial |
| Ukuran mentah | 140.228 parfum, 59 kolom |
| Setelah filter | 8.211 parfum, `vote_count >= 500` |
| Target | `longevity_avg`, skala 1 sampai 5 |

Data dipakai hanya untuk keperluan akademik. Dataset mentah tidak disertakan dalam repository karena ukurannya 139 MB, melebihi batas unggah. Unduh dari tautan di atas, lalu jalankan notebook sesuai urutan.

## Hasil model

181 fitur, split 80 banding 20 dengan `random_state=42`, 6.568 data latih dan 1.643 data uji.

| Model | MAE | R2 uji | R2 latih | Selisih |
|---|---|---|---|---|
| Baseline (rata-rata) | 0,3699 | -0,0008 | 0,0000 | 0,0008 |
| Ridge (alpha via GridSearchCV) | 0,2896 | 0,3494 | 0,3653 | 0,0159 |
| Random Forest (300 pohon) | **0,2784** | **0,3855** | 0,9118 | 0,5263 |
| Gradient Boosting (200 pohon, lr 0,05) | 0,2821 | 0,3783 | 0,4440 | 0,0657 |

Model yang dipakai di aplikasi adalah **Gradient Boosting**. Kriterianya bukan MAE terkecil, tetapi selisih R2 latih dan uji harus di bawah 0,10, baru kemudian dipilih MAE terkecil. Random Forest tidak lolos karena selisihnya 0,53, tanda overfitting.

## Cara menjalankan

### 1. Pasang dependensi

Dari folder project, jalankan pemasangan paket memakai berkas `requirements.txt`.

### 2. Jalankan aplikasi

Dari folder project, jalankan Streamlit dengan berkas `app/app.py`. Aplikasi terbuka di `http://localhost:8501`.

### 3. Jalankan notebook

Notebook dijalankan berurutan dari `01_eda.ipynb` sampai `04_modeling.ipynb`, dari dalam folder `notebook`.

## Struktur folder

```
├── app/              aplikasi Streamlit
├── data/             dataset bersih, split, dan skema
├── docs/             proposal dan panduan
├── luaran/           berkas untuk dikumpulkan
├── model/            model terlatih dan metadata fitur
├── notebook/         notebook 01 sampai 04
├── output/           tabel dan grafik hasil
├── katalog_parfum.json   8.201 parfum dengan komposisinya
└── requirements.txt
```

## Aplikasi

Aplikasi punya dua mode masukan:

1. **Pilih parfum dari katalog.** Pengguna memilih satu dari 8.201 parfum, notes dan accords terisi otomatis. Kalau konsentrasi tidak tercatat di dataset, pengguna memilihnya manual.
2. **Isi manual.** Pengguna memilih notes dan accords sendiri, lalu menentukan konsentrasi.

Keluaran aplikasi berupa skor ketahanan desimal, kategori ketahanan, dan bar progres.

## Keterbatasan

R2 sebesar 0,38 berarti komposisi parfum menjelaskan sekitar 38 persen variasi ketahanan. Sisanya dipengaruhi faktor yang tidak tersedia di dataset, yaitu kondisi kulit pemakai, cuaca, cara pemakaian, kualitas bahan baku, dan kandungan fixative yang tidak tercatat sebagai fragrance note.

Konsentrasi hanya terisi pada 2.788 dari 8.211 baris, yaitu 33,95 persen. Model berbasis pohon tidak dapat memprediksi di luar rentang data latih, sehingga hasil prediksi berada pada kisaran 2,9 sampai 4,1 walaupun nilai aktual mencapai 4,9.
