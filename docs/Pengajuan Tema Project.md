# PENGAJUAN TEMA PROJECT AKHIR
## Mata Kuliah Pembelajaran Mesin (TEK1314)
### Kelas A - Kelompok 9

| No | Nama Anggota | NIM |
|---|---|---|
| 1 | Fattih Algie Maulana | J0404241002 |
| 2 | Aisyah Elfiyuni M.A | J0404241067 |
| 3 | Anggi Permana Putra | J0404241154 |

**Tanggal pengajuan:** 26 Oktober 2026

---

## 1. Judul Project

**Prediksi Tingkat Ketahanan (Longevity) Parfum Berdasarkan Komposisi Fragrance Notes, Accords, dan Tingkat Konsentrasi Menggunakan Perbandingan Ridge Regression, Random Forest, dan Gradient Boosting**

Tema: **B. Regression**

**Judul terdaftar pada SPS daftar kelompok (versi ringkas):**

> Prediksi Tingkat Ketahanan (Longevity) Parfum Berdasarkan Komposisi Fragrance Notes dan Accords

Judul pada proposal ini merupakan versi lengkap yang menambahkan dua hal: tingkat konsentrasi sebagai variabel prediktor, serta metode yang digunakan. Penambahan tingkat konsentrasi dilakukan karena variabel tersebut merupakan salah satu penentu utama longevity dan ketersediaannya pada dataset telah diverifikasi melalui pengujian awal.

---

## 2. Latar Belakang

Industri parfum global bernilai lebih dari USD 50 miliar dan terus tumbuh setiap tahun. Perkembangan e-commerce membuat pembelian parfum semakin banyak dilakukan secara daring. Namun terdapat masalah mendasar: pembeli tidak dapat mencium aroma produk sebelum membeli. Satu-satunya informasi yang tersedia adalah deskripsi tertulis dari penjual, dan deskripsi tersebut bersifat subjektif serta cenderung menampilkan produk secara positif.

Salah satu parameter terpenting bagi konsumen adalah **longevity**, yaitu seberapa lama aroma parfum bertahan di kulit. Konsumen sering kecewa bukan karena wanginya tidak disukai, melainkan karena aroma hilang terlalu cepat dari yang diharapkan. Survei komunitas menunjukkan longevity konsisten menjadi salah satu dari tiga faktor utama dalam keputusan pembelian ulang, bersama proyeksi sillage dan harga.

Secara kimia, longevity parfum ditentukan oleh komposisi bahan penyusunnya. Parfum tersusun dalam piramida tiga lapis: top notes, middle notes, dan base notes. Molekul dengan berat molekul tinggi dan titik didih tinggi, seperti musk, amber, patchouli, dan sandalwood, menguap jauh lebih lambat dibanding molekul ringan seperti citrus dan aroma aquatic. Artinya, secara teori longevity dapat diprediksi dari komposisi bahan.

Komunitas penggemar parfum di platform Fragrantica telah menghasilkan data penilaian berskala besar. Setiap parfum memperoleh penilaian longevity dari ribuan pengguna, dan setiap parfum memiliki daftar komposisi bahan yang terstruktur. Kombinasi keduanya memungkinkan pembangunan model yang mempelajari hubungan antara komposisi bahan dan persepsi ketahanan aroma.

---

## 3. Permasalahan yang Ingin Diselesaikan

**Permasalahan utama:**
Bagaimana memprediksi tingkat ketahanan (longevity) sebuah parfum berdasarkan komposisi fragrance notes dan accords-nya, sehingga konsumen dapat memperkirakan daya tahan parfum sebelum membeli?

**Rincian permasalahan:**

1. Deskripsi produk dari penjual bersifat subjektif dan tidak terukur, sehingga konsumen tidak memiliki acuan objektif untuk menilai daya tahan parfum.
2. Data penilaian komunitas tersedia dalam jumlah besar, tetapi belum dimanfaatkan sebagai dasar prediksi yang dapat digunakan konsumen secara langsung.
3. Belum diketahui bahan atau kelompok bahan mana yang paling berpengaruh terhadap persepsi longevity.
4. Belum diketahui algoritma regresi mana yang paling sesuai untuk memodelkan hubungan antara komposisi bahan dan longevity parfum.

---

## 4. Tujuan Project

1. Menganalisis karakteristik dataset penilaian parfum serta mengidentifikasi komposisi bahan yang paling berpengaruh terhadap longevity.
2. Membangun model regresi yang mampu memprediksi skor longevity parfum berdasarkan komposisi fragrance notes dan accords.
3. Membandingkan performa tiga algoritma regresi, yaitu Ridge Regression, Random Forest Regression, dan Gradient Boosting Regression, menggunakan metrik MAE, MSE, RMSE, dan R².
4. Menganalisis penyebab perbedaan performa antar model, termasuk indikasi overfitting, serta mengidentifikasi keterbatasan model.
5. Mengimplementasikan model terbaik ke dalam aplikasi web sederhana yang dapat menerima input komposisi bahan dan menampilkan hasil prediksi longevity.

---

## 5. Dataset yang Akan Digunakan

| Item | Keterangan |
|---|---|
| Nama dataset | Fragrantica Perfumes: Ratings, Notes, Votes & More |
| Penyusun | Le Decanteur (akun Kaggle `ledecanteur`) |
| Jumlah data mentah | 140.228 baris |
| Jumlah kolom | 59 kolom |
| Ukuran berkas | 139 MB (CSV) |
| Data yang dipakai | 8.211 baris, setelah filter `vote_count >= 500` |
| Tahun penyusunan | 2025 |
| Lisensi | CC BY-NC-SA 4.0 (non-komersial, wajib atribusi) |

**Alasan pemilihan filter `vote_count >= 500`:**

Dataset mentah memuat 140.228 baris, namun 18.996 baris di antaranya belum memiliki penilaian sama sekali (`vote_count = 0`), dan pada baris tersebut skor longevity tercatat sebagai 0,00. Nilai 0,00 ini bukan menunjukkan parfum yang tidak tahan lama, melainkan menandakan data yang belum tersedia. Selain itu, 82.955 baris memiliki penilaian dari kurang dari 20 pengguna, sehingga skornya belum stabil secara statistik. Setelah difilter dengan ambang 500 penilai, deviasi standar target turun dari 1,422 menjadi 0,460, dan tidak ditemukan lagi baris dengan skor longevity 0,00.
---

## 6. Sumber Dataset

Dataset diperoleh dari platform Kaggle:

**URL:** https://www.kaggle.com/datasets/ledecanteur/fragrantica-perfumes

**Format sitasi:**
> Le Decanteur. (2025). *Fragrantica Perfumes: Ratings, Notes, Votes & More* [Data set]. Kaggle. https://www.kaggle.com/datasets/ledecanteur/fragrantica-perfumes

**Asal data:** Data merupakan hasil pengumpulan terstruktur dari halaman produk situs komunitas parfum Fragrantica (fragrantica.com). Setiap baris mewakili satu produk parfum.

**Catatan lisensi:** Dataset dilisensikan CC BY-NC-SA 4.0, yang berarti penggunaan diizinkan untuk keperluan non-komersial dengan kewajiban mencantumkan atribusi kepada penyusun. Project ini digunakan murni untuk keperluan akademik dan atribusi dicantumkan pada laporan serta dokumentasi kode.

---

## 7. Variabel / Feature yang Digunakan

### 7.1 Fitur Utama (Komposisi Bahan)

| Fitur | Tipe Data | Contoh Isi | Perlakuan |
|---|---|---|---|
| `accords` | Teks terstruktur | `woody:45\|sweet:33\|powdery:22` | Dipecah menjadi vektor, 81 kelompok bahan |
| `notes_base` | Teks terstruktur | `Sandalwood:24\|Amber:13\|Vanilla:12` | Dipecah menjadi vektor, 641 jenis bahan |
| `notes_middle` | Teks terstruktur | `Rose:30\|Jasmine:20` | Dipecah menjadi vektor |
| `notes_top` | Teks terstruktur | `Bergamot:49\|Lemon:5` | Dipecah menjadi vektor |

Fitur teks di atas berisi nama bahan beserta bobot kepentingannya (skala 0 hingga 100), yang merepresentasikan seberapa menonjol bahan tersebut menurut pemungutan suara anggota komunitas. Nilai bobot ini kemudian dapat digunakan langsung sebagai nilai fitur, bukan sekadar indikator ada atau tidak ada.

### 7.2 Fitur Pendukung (Karakteristik Produk)

| Fitur | Tipe Data | Rentang / Kategori | Perlakuan |
|---|---|---|---|
| `vote_count` | Numerik (integer) | 0 hingga 36.883 | Ditransformasi `log1p` karena distribusinya sangat miring |
| `year` | Numerik (integer) | Tahun rilis parfum | Nilai kosong diisi median |
| `gender` | Kategorikal | male, female, unisex | One-hot encoding |
| `brand` | Kategorikal | 1.288 nilai unik | Target encoding (kardinalitas tinggi) |

### 7.3 Fitur Tambahan (Tingkat Konsentrasi)

Tingkat konsentrasi parfum merupakan salah satu penentu utama daya tahan aroma karena menentukan persentase minyak wangi dalam larutan. Namun dataset tidak menyediakan kolom konsentrasi secara eksplisit, sehingga nilai ini diekstraksi dari kolom `name` dan `description` menggunakan pencocokan pola.

| Fitur | Tipe Data | Kategori | Perlakuan |
|---|---|---|---|
| `concentration` | Kategorikal | extrait, edp, edt, edc, unknown | One-hot encoding |
| `conc_known` | Biner | 0, 1 | Penanda apakah konsentrasi berhasil diidentifikasi |

**Cakupan ekstraksi:** 34,4% baris berhasil diidentifikasi (8,5% dari nama produk, sisanya dari deskripsi). Sisanya 65,6% masuk kategori `unknown`.

**Bukti pengaruh konsentrasi terhadap longevity** pada subset yang teridentifikasi:

| Konsentrasi | Jumlah baris | Rata-rata longevity |
|---|---|---|
| Extrait | 27 | 4,042 |
| Eau de Parfum | 455 | 3,391 |
| Eau de Toilette | 169 | 3,162 |
| Eau de Cologne | 48 | 3,030 |

Urutan tersebut konsisten dengan teori: semakin tinggi konsentrasi minyak wangi, semakin lama aroma bertahan. Analisis varians pada subset tersebut menunjukkan konsentrasi menjelaskan 14,80% variasi longevity.

**Catatan keterbatasan:** karena cakupan hanya sepertiga data, kontribusi fitur ini terhadap performa model terbatas. Pengujian awal menunjukkan kenaikan R² sebesar 0,007 pada Gradient Boosting dan 0,0005 pada Random Forest. Kolom `conc_known` ditambahkan agar model dapat membedakan antara konsentrasi rendah yang sebenarnya dan konsentrasi yang tidak diketahui.

### 7.4 Fitur yang Ditolak (Pencegahan Data Leakage)

Tiga kolom ditolak karena berpotensi menyebabkan kebocoran data, yaitu kondisi ketika model mempelajari jawaban alih-alih pola:

| Kolom | Korelasi dengan target | Alasan penolakan |
|---|---|---|
| `sillage_avg` | **+0,903** | Berasal dari blok pemungutan suara yang sama dengan longevity. Pengguna yang menilai parfum tahan lama hampir selalu menilai aromanya menyebar jauh, sehingga kedua kolom memuat informasi yang nyaris identik |
| `rating_avg` | +0,293 | Merupakan target alternatif dengan konsep yang tumpang tindih |
| `price_value_avg` | −0,216 | Berasal dari blok pemungutan suara yang sama |

Kolom `sillage_avg` khususnya berbahaya: jika digunakan sebagai fitur, nilai R² model akan terlihat sangat tinggi (di atas 0,8) namun model tersebut tidak benar-benar melakukan prediksi, melainkan menyalin jawaban.

---

## 8. Target / Output yang Diprediksi

**Kolom target:** `longevity_avg`

| Properti | Nilai |
|---|---|
| Tipe data | Numerik kontinu (float) |
| Skala | 1 hingga 5 |
| Arti skala | 1 = Very Weak (kurang dari 1 jam), 2 = Weak (1-2 jam), 3 = Moderate (3-6 jam), 4 = Long Lasting (7-12 jam), 5 = Eternal (lebih dari 12 jam) |
| Nilai rata-rata data | 3,271 |
| Deviasi standar | 0,460 |
| Kemiringan distribusi (skewness) | +0,002 (hampir simetris sempurna) |

Kolom target ini merupakan rata-rata penilaian longevity dari seluruh pengguna yang memberikan vote pada parfum tersebut. Karena sifatnya kontinu dan bukan kategorikal, permasalahan ini termasuk dalam kategori regresi.

**Output aplikasi:** aplikasi akan menerima input berupa pilihan komposisi bahan parfum, kemudian menampilkan hasil prediksi berupa skor longevity dalam skala 1 hingga 5 beserta interpretasi kategorinya (Weak, Moderate, Long Lasting, atau Eternal).

---

## 9. Algoritma Machine Learning yang Direncanakan

Project ini menggunakan tiga algoritma regresi, sesuai ketentuan minimal tiga algoritma untuk dibandingkan.

### 9.1 Ridge Regression

**Cara kerja:** Regresi linear yang menambahkan penalti L2 pada fungsi biaya, sehingga koefisien model dibatasi agar tidak bernilai terlalu besar.

**Alasan pemilihan:** Dataset ini memiliki ratusan fitur komposisi bahan yang bersifat sparse (banyak bernilai nol). Pada kondisi tersebut, regresi linear tanpa regularisasi mengalami multikolinearitas sehingga performanya jatuh. Pengujian awal menunjukkan Linear Regression menghasilkan R² sebesar **−1,893** pada pengujian, yang berarti performanya lebih buruk daripada sekadar menebak nilai rata-rata. Ridge Regression dengan penalti L2 meningkatkan hasil tersebut menjadi **−0,394**, atau sekitar lima kali lebih baik. Ridge dipilih menggantikan Linear Regression murni karena alasan ini.

### 9.2 Random Forest Regression

**Cara kerja:** Ensemble dari banyak pohon keputusan yang dilatih pada subset data dan subset fitur yang berbeda (bagging), kemudian hasilnya dirata-ratakan.

**Alasan pemilihan:** Mampu menangkap hubungan non-linear antar bahan parfum tanpa memerlukan asumsi bentuk fungsi tertentu. Relatif tahan terhadap pencilan (outlier) dan tidak memerlukan normalisasi fitur. Cocok untuk data tabular dengan campuran fitur numerik dan kategorikal.

### 9.3 Gradient Boosting Regression

**Cara kerja:** Ensemble pohon keputusan yang dilatih secara berurutan, di mana setiap pohon baru berusaha memperbaiki kesalahan yang dibuat oleh pohon-pohon sebelumnya.

**Alasan pemilihan:** Umumnya memberikan performa terbaik pada data tabular berukuran sedang. Berbeda dengan Random Forest yang melatih pohon secara paralel dan independen, Gradient Boosting melakukan penyempurnaan bertahap sehingga cenderung lebih tahan terhadap overfitting meskipun Random Forest memiliki kedalaman pohon yang lebih besar.

### 9.4 Ringkasan Perbandingan

| Model | Jenis | Kelebihan | Keterbatasan |
|---|---|---|---|
| Ridge Regression | Linear + regularisasi L2 | Cepat, mudah diinterpretasi, stabil pada fitur sparse | Hanya menangkap hubungan linear |
| Random Forest Regression | Ensemble bagging | Menangkap hubungan non-linear, tahan pencilan | Cenderung overfitting pada dataset kecil, sulit diinterpretasi |
| Gradient Boosting Regression | Ensemble boosting | Akurasi tinggi, lebih stabil terhadap overfitting | Training lebih lambat, sensitif terhadap hyperparameter |
---

## 10. Daftar Artikel Jurnal Referensi

Berikut enam artikel jurnal ilmiah yang menjadi referensi project. Seluruh artikel telah diverifikasi keberadaannya beserta detail bibliografinya.

### Jurnal 1

> Nurmuthia, L. D., Imtiyaza, R., & Sagala, N. T. M. (2025). Personalized Perfume Recommendations Based on User Descriptions Using Cosine and Jaccard Similarity. *Procedia Computer Science*, 269, 1097-1106. https://doi.org/10.1016/j.procs.2025.09.051

Kontribusi: kerangka kerja sistem rekomendasi parfum berbasis kemiripan konten menggunakan dataset Fragrantica berskala besar.

### Jurnal 2

> Kim, J., Oh, K., & Oh, B.-S. (2024). An NLP-Based Perfume Note Estimation Based on Descriptive Sentences. *Applied Sciences*, 14(20), 9293. https://doi.org/10.3390/app14209293

Kontribusi: pemodelan hubungan antara deskripsi tekstual parfum dengan komposisi notes menggunakan sentence transformer dan proses fine-tuning.

### Jurnal 3

> Fichtelmann, P., & Westermayr, J. (2026). Machine learning for smell: ordinal odor strength prediction of molecular perfumery components. *RSC Advances*, 16(28), 25696-25704. PMID: 42158754. https://pubmed.ncbi.nlm.nih.gov/42158754/

Kontribusi: prediksi kekuatan bau (odor strength) sebagai variabel ordinal menggunakan machine learning, disertai analisis kepentingan fitur melalui SHAP.

### Jurnal 4

> Rodrigues, B. C. L., Santana, V. V., Queiroz, L. P., Rebello, C. M., & Nogueira, I. B. R. (2024). Harnessing graph neural networks to craft fragrances based on consumer feedback. *Computers & Chemical Engineering*, 185, 108674. https://doi.org/10.1016/j.compchemeng.2024.108674

Kontribusi: pemanfaatan graph neural network untuk mengelompokkan parfum berdasarkan profil aroma dan menyusun formulasi baru berdasarkan umpan balik konsumen.

### Jurnal 5

> Nikolić, M., & Marjanović, M. (2025). Data Science Meets Fragrance: Analyzing User Reviews to Decode Emotional Connections to Perfume Notes. Dalam *Proceedings of the International Scientific Conference on Information Technology, Computer Science, and Data Science (SINTEZA 2025)* (hlm. 213-220). https://doi.org/10.15308/Sinteza-2025-213-220

Kontribusi: analisis sentimen ulasan pengguna Fragrantica menggunakan VADER dan DistilBERT untuk mengaitkan komposisi notes dengan respons emosional konsumen.

### Jurnal 6

> Nikolić, M., Marjanović, M., & Rađenović, Ž. (2024). Application of Machine Learning for Perfume Popularity Prediction: Analysis of Fragrance Notes and Consumer Behavior. *Proceedings of the Academy of Applied Technical and Preschool Studies Niš*, 64-67.

Kontribusi: penerapan machine learning untuk memprediksi popularitas parfum berdasarkan komposisi notes dan perilaku konsumen.

### Relevansi Terhadap Project

| Kebutuhan project | Jurnal yang mendukung |
|---|---|
| Permasalahan penelitian | Jurnal 1, 6 |
| Dataset dan variabel | Jurnal 1, 5, 6 |
| Metode preprocessing | Jurnal 2, 3 |
| Algoritma Machine Learning | Jurnal 3, 4, 6 |
| Metode evaluasi model | Jurnal 3, 4 |

---

## 11. Tabel Studi Literatur

| No | Penulis & Tahun | Permasalahan | Dataset | Metode / Algoritma | Metrik Evaluasi | Hasil Utama | Perbedaan dengan Project |
|---|---|---|---|---|---|---|---|
| 1 | Nurmuthia, Imtiyaza & Sagala (2025) | Memberikan rekomendasi parfum yang dipersonalisasi berdasarkan deskripsi kebutuhan pengguna | 24.760 parfum dengan 11 fitur, bersumber dari Fragrantica | Cosine Similarity dan Jaccard Similarity | Tingkat relevansi hasil rekomendasi | Sistem rekomendasi berbasis kemiripan konten mampu mencocokkan deskripsi pengguna dengan parfum yang sesuai | Project ini tidak melakukan rekomendasi, melainkan membangun model regresi untuk memprediksi nilai longevity secara numerik |
| 2 | Kim, Oh & Oh (2024) | Mengestimasi komposisi notes parfum dari kalimat deskriptif | 62 parfum dengan 255 jenis notes | Sentence Transformer dengan proses fine-tuning | Hit rate@5 dan Mean Reciprocal Rank (MRR) | Hit rate@5 meningkat dari 37,1-41,1% menjadi 72,6-79,0%; MRR meningkat dari 22,1-31,9% menjadi 57,3-63,2% | Project ini menggunakan notes yang sudah terstruktur sebagai input, bukan mengekstraksi notes dari teks bebas, dan outputnya berupa nilai kontinu bukan daftar notes |
| 3 | Fichtelmann & Westermayr (2026) | Memprediksi kekuatan bau komponen parfum berdasarkan struktur molekul | Lebih dari 2.300 molekul dari penggabungan dua sumber publik | Algoritma machine learning ordinal dengan optimasi hyperparameter dan analisis SHAP | Metrik evaluasi ordinal dan analisis kepentingan fitur | Model mampu memprediksi kekuatan bau secara ordinal; analisis SHAP mengidentifikasi penentu fisikokimia utama | Project ini bekerja pada tingkat produk jadi dengan representasi komposisi notes, bukan pada tingkat struktur molekul individual |
| 4 | Rodrigues, Santana, Queiroz, Rebello & Nogueira (2024) | Merancang formulasi parfum baru berdasarkan umpan balik konsumen | Data parfum komersial beserta umpan balik konsumen | Graph Neural Network dan clustering | Metrik kualitas klaster dan evaluasi formulasi | GNN mampu mengelompokkan parfum berdasarkan profil aroma dan mengusulkan formulasi baru | Project ini menggunakan algoritma regresi tabular klasik, bukan graph neural network, dan bertujuan memprediksi nilai longevity bukan merancang formula |
| 5 | Nikolić & Marjanović (2025) | Menghubungkan komposisi notes parfum dengan respons emosional konsumen | Ulasan pengguna platform Fragrantica | VADER, DistilBERT, clustering, dan visualisasi statistik | Akurasi klasifikasi sentimen dan analisis korelasi | Ditemukan pola hubungan antara profil aroma tertentu dengan kelompok emosi konsumen | Project ini memprediksi parameter sensorik berupa longevity (numerik), bukan mengklasifikasikan emosi dari teks ulasan |
| 6 | Nikolić, Marjanović & Rađenović (2024) | Memprediksi popularitas parfum berdasarkan komposisi notes dan perilaku konsumen | Data parfum dan perilaku konsumen | Algoritma machine learning untuk prediksi | Metrik evaluasi prediksi | Komposisi notes terbukti memiliki daya prediksi terhadap tingkat popularitas parfum | Project ini memprediksi atribut sensorik (longevity) bukan metrik popularitas, dan membandingkan tiga algoritma regresi secara eksplisit |

---

## 12. Kesimpulan Pengajuan

Project ini memenuhi seluruh ketentuan pengajuan tema:

| Ketentuan | Status |
|---|---|
| Judul project | Tersedia (bagian 1) |
| Latar belakang singkat | Tersedia (bagian 2) |
| Permasalahan yang ingin diselesaikan | Tersedia (bagian 3) |
| Tujuan project | Tersedia (bagian 4) |
| Dataset yang akan digunakan | Tersedia (bagian 5) |
| Sumber dataset | Tersedia (bagian 6) |
| Variabel / feature yang digunakan | Tersedia (bagian 7) |
| Target / output yang diprediksi | Tersedia (bagian 8) |
| Algoritma Machine Learning yang direncanakan | Tersedia (bagian 9) |
| Minimal 5 artikel jurnal ilmiah | Tersedia 6 artikel (bagian 10) |
| Tabel studi literatur | Tersedia (bagian 11) |
