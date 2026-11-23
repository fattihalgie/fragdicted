# Tabel Studi Literatur

**Judul penelitian:** Prediksi Tingkat Ketahanan (Longevity) Parfum Berdasarkan Komposisi Fragrance Notes, Accords, dan Tingkat Konsentrasi Menggunakan Perbandingan Ridge Regression, Random Forest, dan Gradient Boosting

**Kelompok 9, Kelas A**
Fattih Algie Maulana (J0404241002), Aisyah Elfiyuni M.A (J0404241067), Anggi Permana Putra (J0404241154)

**Mata kuliah:** Pembelajaran Mesin TEK1302
**Dosen pengampu:** Bapak Dodik

Kolom terakhir diisi hal spesifik yang membedakan penelitian kami dengan artikel yang dirujuk, sesuai ketentuan panduan project akhir bagian 03.

---

## Tabel

| No. | Penulis & Tahun | Permasalahan / Dataset | Algoritma & Metrik | Hasil & Perbedaan |
|---|---|---|---|---|
| 1 | Malhiac, C., Hawko, C., Buzzi, J., & Laghouati, H. (2026). *Flavour and Fragrance Journal*. DOI 10.1002/ffj.70155 | Mengukur berapa lama base note parfum bertahan dan seberapa besar kontribusi tiap bahan terhadap daya tahan tersebut. Data diperoleh dari analisis laboratorium berbasis waktu (time-resolved analysis), bukan dari dataset publik. | Bukan machine learning. Pendekatan analitis kimia dengan pengukuran persistensi per bahan pada interval waktu tertentu. Metrik berupa kurva persistensi dan kontribusi relatif tiap ingredient. | Menemukan bahwa tiap bahan punya pola penguapan berbeda dan kontribusinya terhadap base note bisa dipisahkan. **Perbedaan:** penelitian kami memakai dataset persepsi pengguna berskala besar (8.211 parfum) dan pendekatan regresi machine learning, bukan pengukuran laboratorium. Target kami skor longevity agregat 1 sampai 5, bukan kurva waktu per bahan. |
| 2 | Hadjiefstathiou, E., Savary, G., Malhiac, C., & Terescenco, D. (2025). *International Journal of Cosmetic Science*, 47(6), 981-995. DOI 10.1111/ics.13085 | Meneliti pengaruh sifat molekul bahan wangi dan sifat kulit pemakai terhadap profil penguapan parfum. Data dari pengukuran instrumental pada berbagai kondisi kulit. | Bukan machine learning. Analisis fisika-kimia penguapan dengan pembandingan antar jenis molekul dan jenis kulit. Metrik berupa laju penguapan dan headspace concentration. | Membuktikan parfum yang sama dapat menguap berbeda pada pemakai berbeda karena faktor kulit. **Perbedaan:** penelitian kami tidak memasukkan variabel kulit sama sekali, karena dataset hanya berisi komposisi. Temuan jurnal ini justru menjadi dasar penjelasan kami mengapa R² hanya sekitar 0,38, yaitu 62 persen variasi dijelaskan faktor di luar dataset. |
| 3 | Kim, H., Oh, S., & Oh, J. (2024). *Applied Sciences*, 14(20), 9293. DOI 10.3390/app14209293 | Memperkirakan fragrance notes parfum dari teks deskripsi produk. Data berupa deskripsi parfum berbahasa alami yang dipasangkan dengan daftar notes. | Machine learning berbasis NLP (natural language processing) untuk klasifikasi dan ekstraksi notes. Metrik yang dipakai adalah akurasi dan F1-score per kategori note. | Menunjukkan bahwa data parfum dapat diolah secara komputasional dengan pendekatan machine learning dan hasilnya dapat dipertanggungjawabkan. **Perbedaan:** arah prediksi kami berlawanan. Jurnal ini memprediksi notes dari deskripsi, sedangkan kami memprediksi longevity dari notes. Selain itu, model kami adalah regresi dengan target kontinu 1 sampai 5, bukan klasifikasi teks, dan metrik kami MAE serta R², bukan akurasi. |
| 4 | Breiman, L. (2001). *Machine Learning*, 45(1), 5-32. DOI 10.1023/A:1010933404324 | Masalah akurasi dan stabilitas pohon keputusan tunggal yang mudah overfitting. Dataset yang dipakai adalah benchmark klasifikasi standar (sonar, ionosphere, diabetes, glass, satimage). | Random Forest, yaitu ensemble pohon keputusan yang dibangun dari bootstrap sampling dan pemilihan fitur acak. Metrik berupa error rate dan estimasi error internal (out-of-bag). | Random Forest menyamai atau mengalahkan AdaBoost pada sebagian besar dataset dan lebih tahan terhadap noise. Paper ini juga menyebut bahwa pohon yang tumbuh terlalu dalam dapat overfitting. **Perbedaan:** penelitian kami menerapkan Random Forest pada masalah regresi dengan target kontinu, bukan klasifikasi. Kami juga tidak memakai estimasi out-of-bag, melainkan pembagian data 80 banding 20 yang eksplisit, dan kami justru menemukan overfitting pada Random Forest sendiri dengan selisih R² latih dan uji sebesar 0,53. |
| 5 | Friedman, J. H. (2001). *Annals of Statistics*, 29(5), 1189-1232. DOI 10.1214/aos/1013203451 | Masalah optimasi fungsi loss secara bertahap pada model aditif berbasis pohon. Dataset uji berupa data simulasi dan data regresi nyata. | Gradient Boosting Machine, yaitu pembangunan model secara berurutan dengan tiap tahap meminimalkan residual tahap sebelumnya melalui gradient descent pada ruang fungsi. Metrik berupa deviance dan error regresi. | Model dibangun bertahap dengan kontribusi tiap pohon dikendalikan learning rate, sehingga lebih stabil dibandingkan pohon tunggal. **Perbedaan:** kami menerapkan Gradient Boosting pada data komposisi parfum berskala 181 fitur yang sangat sparse (91,2 persen sel bernilai nol). Kami juga memakai kriteria pemilihan model yang tidak ada di paper ini, yaitu selisih R² latih dan uji harus di bawah 0,10 sebelum MAE dibandingkan. |

---

## Ringkasan keterkaitan dengan penelitian kami

| Referensi | Peran dalam penelitian kami | Letak di naskah |
|---|---|---|
| 1 | Dasar bahwa hubungan komposisi bahan dengan daya tahan sudah diakui secara ilmiah | Pendahuluan, tinjauan pustaka |
| 2 | Dasar ilmiah untuk menjelaskan keterbatasan model (faktor kulit tidak masuk) | Pembahasan, keterbatasan |
| 3 | Bukti bahwa machine learning pada data parfum sudah diterima akademik | Tinjauan pustaka |
| 4 | Rujukan algoritma Random Forest dan dasar teori overfitting | Metode, hasil dan pembahasan |
| 5 | Rujukan algoritma Gradient Boosting dan dasar teori boosting bertahap | Metode, pemilihan model |

---

## Catatan pemenuhan ketentuan

Panduan project akhir bagian 03 mensyaratkan minimal 5 artikel jurnal ilmiah relevan, dan kelima jurnal tersebut harus menjadi dasar untuk merumuskan masalah, memilih dataset dan variabel, menyusun preprocessing, membandingkan algoritma, dan menentukan evaluasi. Kolom terakhir pada tabel di atas mengisi bagian "Perbedaan", yang menurut panduan harus memuat hal spesifik yang membedakan project dengan artikel yang dirujuk, berdasarkan fakta di jurnal.

Seluruh DOI pada tabel ini sudah diverifikasi aktif melalui Crossref, bukan dikarang.
