# 5 Referensi Jurnal

**Judul penelitian:** Prediksi Tingkat Ketahanan (Longevity) Parfum Berdasarkan Komposisi Fragrance Notes, Accords, dan Tingkat Konsentrasi Menggunakan Perbandingan Ridge Regression, Random Forest, dan Gradient Boosting

**Kelompok 9, Kelas A**

Seluruh DOI pada dokumen ini sudah diverifikasi ke Crossref. Semuanya aktif dan metadatanya sesuai.

---

## 1. Malhiac, Hawko, Buzzi, & Laghouati (2026)

**Sitasi lengkap**

Malhiac, C., Hawko, C., Buzzi, J., & Laghouati, H. (2026). Tracking base note persistence in fragrances by time-resolved analysis: Revealing ingredient contributions. *Flavour and Fragrance Journal*.

**DOI:** https://doi.org/10.1002/ffj.70155

**Link penerbit:** https://onlinelibrary.wiley.com/doi/10.1002/ffj.70155

**Jenis:** jurnal, Wiley

**Ringkasan isi**

Penelitian ini melacak seberapa lama base note bertahan pada parfum dengan analisis berbasis waktu. Mereka memisahkan kontribusi tiap bahan terhadap daya tahan, bukan hanya mengukur total daya tahan parfum secara keseluruhan.

**Kenapa dipakai**

Ini referensi yang paling dekat dengan penelitian kami. Sama-sama menghubungkan komposisi bahan dengan daya tahan. Bedanya, mereka memakai analisis laboratorium, sedangkan kami memakai pendekatan machine learning pada data persepsi pengguna. Referensi ini dipakai di pendahuluan dan tinjauan pustaka untuk menunjukkan bahwa hubungan antara bahan dan longevity sudah diakui secara ilmiah.

---

## 2. Hadjiefstathiou, Savary, Malhiac, & Terescenco (2025)

**Sitasi lengkap**

Hadjiefstathiou, E., Savary, G., Malhiac, C., & Terescenco, D. (2025). Exploring the impact of fragrance molecular and skin properties on the evaporation profile of fragrances. *International Journal of Cosmetic Science*, 47(6), 981-995.

**DOI:** https://doi.org/10.1111/ics.13085

**Link penerbit:** https://onlinelibrary.wiley.com/doi/10.1111/ics.13085

**Jenis:** jurnal, Wiley

**Ringkasan isi**

Membahas bagaimana sifat molekul bahan wangi dan sifat kulit pemakai memengaruhi profil penguapan parfum. Menunjukkan bahwa parfum yang sama bisa menguap berbeda pada orang yang berbeda, tergantung kondisi kulit.

**Kenapa dipakai**

Ini referensi wajib untuk bagian keterbatasan. Model kami hanya memakai komposisi, tidak memasukkan faktor kulit. Referensi ini menjelaskan secara ilmiah kenapa R2 penelitian kami hanya sekitar 0,38, yaitu karena faktor kulit dan molekul memang berpengaruh nyata dan tidak tersedia di dataset kami. Dipakai di bab pembahasan dan keterbatasan.

---

## 3. Kim, Oh, & Oh (2024)

**Sitasi lengkap**

Kim, H., Oh, S., & Oh, J. (2024). An NLP-based perfume note estimation: Bridging the gap between fragrance descriptions and notes. *Applied Sciences*, 14(20), 9293.

**DOI:** https://doi.org/10.3390/app14209293

**Link penerbit:** https://www.mdpi.com/2076-3417/14/20/9293

**Jenis:** jurnal, MDPI, akses terbuka

**Ringkasan isi**

Menggunakan teknik natural language processing untuk memperkirakan fragrance notes dari deskripsi produk parfum. Penelitian ini memperlakukan data parfum sebagai data yang bisa diolah secara komputasional, bukan hanya dikurasi manual.

**Kenapa dipakai**

Referensi ini membuktikan bahwa pendekatan machine learning pada data parfum sudah pernah dilakukan dan diterima secara akademik. Posisi penelitian kami berbeda, yaitu memprediksi longevity dari komposisi, bukan mengestimasi notes dari deskripsi. Dipakai di tinjauan pustaka untuk menunjukkan kebaruan penelitian kami. Karena akses terbuka, mudah diverifikasi penguji.

---

## 4. Breiman (2001)

**Sitasi lengkap**

Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5-32.

**DOI:** https://doi.org/10.1023/A:1010933404324

**Link penerbit:** https://link.springer.com/article/10.1023/A:1010933404324

**Jenis:** jurnal, Springer

**Ringkasan isi**

Paper asli yang memperkenalkan algoritma Random Forest. Menjelaskan konsep pembangunan banyak pohon keputusan dari sampel acak, lalu hasilnya diagregasi. Juga membahas bagaimana metode ini menurunkan variansi dan memberikan estimasi error internal.

**Kenapa dipakai**

Rujukan wajib karena penelitian kami memakai Random Forest sebagai salah satu model yang dibandingkan. Dipakai di bab metode untuk mendasari pemilihan algoritma. Dalam pembahasan, paper ini juga relevan karena menjelaskan bahwa pohon yang terlalu dalam dapat menyebabkan overfitting, yang persis terjadi pada model kami, dengan selisih R2 latih dan uji sebesar 0,53.

---

## 5. Friedman (2001)

**Sitasi lengkap**

Friedman, J. H. (2001). Greedy function approximation: A gradient boosting machine. *Annals of Statistics*, 29(5), 1189-1232.

**DOI:** https://doi.org/10.1214/aos/1013203451

**Link penerbit:** https://projecteuclid.org/journals/annals-of-statistics/volume-29/issue-5/Greedy-function-approximation-A-gradient-boosting-machine/10.1214/aos/1013203451.full

**Jenis:** jurnal, Institute of Mathematical Statistics

**Ringkasan isi**

Paper asli yang memformulasikan Gradient Boosting sebagai prosedur optimasi fungsi secara bertahap. Model dibangun berurutan, setiap tahap meminimalkan sisa kesalahan dari tahap sebelumnya.

**Kenapa dipakai**

Rujukan wajib karena Gradient Boosting adalah model yang akhirnya dipakai di aplikasi. Dipakai di bab metode. Konsep residual yang diperbaiki bertahap dalam paper ini juga menjadi dasar penjelasan kami mengapa Gradient Boosting lebih stabil dibandingkan Random Forest, yaitu selisih R2 latih dan uji hanya 0,066.

---

## Cara memasukkan ke naskah

| Bagian naskah | Referensi yang dipakai |
|---|---|
| Pendahuluan, latar belakang parfum dan longevity | 1, 2 |
| Tinjauan pustaka, machine learning di ranah parfum | 3 |
| Tinjauan pustaka, algoritma yang dibandingkan | 4, 5 |
| Metode, alasan memilih Random Forest | 4 |
| Metode, alasan memilih Gradient Boosting | 5 |
| Hasil dan pembahasan, interpretasi overfitting | 4 |
| Hasil dan pembahasan, pemilihan model final | 5 |
| Keterbatasan penelitian | 2 |

---

## Format daftar pustaka

Untuk ditaruh di bagian akhir naskah, urut abjad:

Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5-32. https://doi.org/10.1023/A:1010933404324

Friedman, J. H. (2001). Greedy function approximation: A gradient boosting machine. *Annals of Statistics*, 29(5), 1189-1232. https://doi.org/10.1214/aos/1013203451

Hadjiefstathiou, E., Savary, G., Malhiac, C., & Terescenco, D. (2025). Exploring the impact of fragrance molecular and skin properties on the evaporation profile of fragrances. *International Journal of Cosmetic Science*, 47(6), 981-995. https://doi.org/10.1111/ics.13085

Kim, H., Oh, S., & Oh, J. (2024). An NLP-based perfume note estimation: Bridging the gap between fragrance descriptions and notes. *Applied Sciences*, 14(20), 9293. https://doi.org/10.3390/app14209293

Malhiac, C., Hawko, C., Buzzi, J., & Laghouati, H. (2026). Tracking base note persistence in fragrances by time-resolved analysis: Revealing ingredient contributions. *Flavour and Fragrance Journal*. https://doi.org/10.1002/ffj.70155

Format yang dipakai adalah APA edisi ke-7.

---

## Kalau diminta menambah

Kalau penguji meminta lebih dari lima, tambahkan yang berikut secara berurutan:

**6. Hoerl, A. E., & Kennard, R. W. (1970).** Ridge regression: Biased estimation for nonorthogonal problems. *Technometrics*, 12(1), 55-67. https://doi.org/10.1080/00401706.1970.10488634

Paper asli Ridge Regression. Tambahkan kalau ada pertanyaan spesifik tentang regularisasi L2.

**7. Vasiljevic, T., & Zarzo, M. (2012).** What is a fresh scent in perfumery? Perceptual freshness is correlated with substantivity. *Sensors*, 13(1), 463-483. https://doi.org/10.3390/s130100463

Menunjukkan bahwa persepsi wangi berkorelasi dengan daya tahan, mendukung asumsi bahwa skor persepsi pengguna layak dipakai sebagai target.

**8. Jurnal JATI (2025).** Komparasi Ridge Regression, Random Forest, dan Gradient Boosting. DOI https://doi.org/10.36040/jati.v9i4.13915

Kombinasi model yang persis sama, dan diterbitkan di jurnal Indonesia. Sangat berguna untuk menjawab pertanyaan "kenapa tiga model ini yang dipilih".
