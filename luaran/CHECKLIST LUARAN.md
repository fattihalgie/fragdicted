# Checklist Luaran Project Akhir

**Mata kuliah:** Pembelajaran Mesin TEK1302, modul M15
**Kelas:** A, Kelompok 9
**Nama folder wajib:** `ML2026_A_Kelompok09_PrediksiLongevityParfum` (sudah sesuai)

---

## Status luaran wajib

| No | Luaran | Status | Letak |
|---|---|---|---|
| 1 | PPT laporan project | **Belum** | dibuat di Canva, ditaruh di `luaran/` |
| 2 | Source code / repository | Sebagian | `notebook/`, `app/`, `model/` |
| 3 | Dataset atau link dataset | Ada | `data/`, plus link Kaggle |
| 4 | Model hasil training | Ada | `model/model_aplikasi.pkl` |
| 5 | Video demo maksimal 7 menit | **Belum** | rekam, taruh di `luaran/` |
| 6 | Daftar 5 jurnal referensi | Ada | `luaran/5 Referensi Jurnal - Longevity Parfum.md` |
| 7 | Tabel studi literatur | Ada | `luaran/Tabel Studi Literatur.md` |
| 8 | Link aplikasi / deployment | Lokal | `http://localhost:8501` |
| 9 | Draft jurnal | **Belum** | opsional, hanya untuk yang mau publish |

---

## Yang harus dibereskan sebelum Selasa

### 1. PPT laporan project

Ikuti struktur A sampai O dari panduan bagian 14. Isi per bagian:

| Bagian | Isi | Sumber di folder ini |
|---|---|---|
| A | Judul, anggota, NIM, kelas | `docs/Proposal Project - Kelompok 9.md` |
| B | Latar belakang dan masalah | idem |
| C | Tujuan project | `luaran/Narasi Presentasi - Slide 04 dan 05.md` |
| D | Studi literatur | `luaran/Tabel Studi Literatur.md` |
| E | Dataset: sumber, jumlah, fitur, target | `data/SCHEMA.md`, README |
| F | EDA dan visualisasi | `output/fig_hist_longevity.png`, `output/fig_korelasi.png` |
| G | Preprocessing dan alasannya | `notebook/02_preprocessing.ipynb` |
| H | Pengembangan model: algoritma, split, parameter | `notebook/04_modeling.ipynb` |
| I | Evaluasi dan perbandingan | `output/tabel_perbandingan_model.csv` |
| J | Pemilihan model terbaik | narasi slide 05 |
| K | Implementasi aplikasi | `app/app.py` |
| L | Demo aplikasi | tangkapan layar |
| M | Kesimpulan | lihat di bawah |
| N | Keterbatasan dan pengembangan | lihat di bawah |
| O | Pembagian tugas | `docs/Panduan Penyusunan Pembagian Tugas - Kelompok 9.docx` |

**Kesimpulan yang bisa dipakai:** komposisi parfum menjelaskan sekitar 38 persen variasi ketahanan. Model Gradient Boosting dipilih untuk aplikasi karena selisih R² latih dan uji hanya 0,066, jauh lebih stabil dibanding Random Forest yang selisihnya 0,53.

**Keterbatasan:** dataset tidak memuat faktor kulit, cuaca, cara pakai, dan kualitas bahan baku. Konsentrasi hanya terisi pada 33,95 persen baris. Model pohon tidak dapat memprediksi di luar rentang data latih, sehingga prediksi mentok sekitar 2,9 sampai 4,1.

### 2. Video demo maksimal 7 menit

Urutan yang disarankan sesuai panduan bagian 13:

1. Perkenalan anggota dan judul, 30 detik
2. Latar belakang masalah, 45 detik
3. Dataset dan preprocessing, 60 detik
4. Algoritma dan perbandingan performa, 90 detik
5. Model terbaik dan alasannya, 60 detik
6. Demonstrasi aplikasi dengan beberapa input berbeda, 120 detik
7. Kesimpulan, 30 detik

Aplikasi harus benar-benar dijalankan, bukan tangkapan layar. Tunjukkan minimal tiga contoh input dengan hasil berbeda, misalnya parfum berat dengan extrait, parfum ringan dengan eau fraiche, dan satu input manual.

### 3. Source code yang bisa dijalankan ulang

Panduan bagian 12 meminta struktur yang mudah dijalankan penguji. Yang perlu ditambah:

- `requirements.txt` berisi daftar dependensi beserta versinya
- Petunjuk menjalankan di README
- Samakan notebook `04_modeling.ipynb` dengan model 181 fitur yang sekarang dipakai

### 4. Link aplikasi

Aplikasi sekarang hanya berjalan lokal di port 8501. Kalau ingin ada link publik, perlu deployment ke Streamlit Community Cloud. Kalau tidak, panduan membolehkan demo lokal asalkan lingkungannya dapat dijalankan ulang. Itu sebabnya `requirements.txt` penting.

---

## Kalau deploy ke Streamlit Community Cloud

Yang perlu disiapkan:

1. Repository GitHub publik berisi folder ini
2. File `requirements.txt`
3. File `katalog_parfum.json` harus ikut diunggah, ukurannya 3,2 MB, masih di bawah batas GitHub
4. `data/perfumes.csv` ukurannya 139 MB, **jangan diunggah**. GitHub menolak file di atas 100 MB. Cukup `clean.csv` dan file X/y, atau ganti dengan link Kaggle di README.

---

## Isi tiap folder

```
ML2026_A_Kelompok09_PrediksiLongevityParfum/
├── app/              aplikasi Streamlit
├── data/             dataset mentah, bersih, dan split
├── docs/             proposal, panduan, PDF panduan resmi
├── luaran/           semua berkas untuk dikumpulkan
├── model/            model terlatih dan metadata fitur
├── notebook/         notebook 01 sampai 04
├── output/           tabel dan grafik hasil
├── katalog_parfum.json
└── README.txt
```

Mulai sekarang, semua berkas baru untuk project ini masuk ke folder di atas. Berkas presentasi dan referensi yang tadinya tersebar di Downloads sudah dipindahkan ke `luaran/`.
