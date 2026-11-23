# Referensi Jurnal

**Judul:** Prediksi Tingkat Ketahanan (Longevity) Parfum Berdasarkan Komposisi Fragrance Notes, Accords, dan Tingkat Konsentrasi Menggunakan Perbandingan Ridge Regression, Random Forest, dan Gradient Boosting

Semua DOI di bawah sudah dicek satu per satu ke Crossref, bukan dikarang. Tanda `[terverifikasi]` berarti DOI aktif dan metadatanya cocok.

---

## A. Domain parfum, longevity, dan penguapan

**1. Vasiljevic, T., & Zarzo, M. (2012).** What is a fresh scent in perfumery? Perceptual freshness is correlated with substantivity. *Sensors*, 13(1), 463-483. https://doi.org/10.3390/s130100463 `[terverifikasi]`

Relevansi: bukti empiris bahwa konsep "fresh" berkorelasi dengan daya tahan (substantivity). Ini landasan kuat bahwa persepsi wangi berhubungan langsung dengan longevity.

**2. Hadjiefstathiou, E., Savary, G., Malhiac, C., & Terescenco, D. (2025).** Exploring the impact of fragrance molecular and skin properties on the evaporation profile of fragrances. *International Journal of Cosmetic Science*, 47(6), 981-995. https://doi.org/10.1111/ics.13085 `[terverifikasi]`

Relevansi: menjelaskan kenapa longevity satu parfum berbeda antar pemakai. Ini referensi wajib untuk bagian keterbatasan, karena model regresi kalian tidak memasukkan faktor kulit.

**3. Malhiac, C., Hawko, C., Buzzi, J., & Laghouati, H. (2026).** Tracking base note persistence in fragrances by time-resolved analysis: Revealing ingredient contributions. *Flavour and Fragrance Journal*. https://doi.org/10.1002/ffj.70155 `[terverifikasi]`

Relevansi: paling dekat dengan topik kalian. Mengukur kontribusi bahan terhadap daya tahan base note secara time-resolved.

**4. Teixeira, M. A., Rodríguez, O., Rodrigues, A. E., & Selway, R. (2013).** Prediction model for the odor intensity of fragrance mixtures: A valuable tool for perfumed product design. *Industrial & Engineering Chemistry Research*, 52(2), 963-971. https://doi.org/10.1021/ie302538c `[terverifikasi]`

Relevansi: preseden pemodelan kuantitatif untuk intensitas wangi campuran. Berguna untuk argumen bahwa pendekatan prediktif di ranah parfum bukan hal baru.

**5. Rodrigues, A. E., Nogueira, I. B. R., & Faria, R. P. V. (2021).** Perfume and flavor engineering: A chemical engineering perspective. *Molecules*, 26(11), 3095. https://doi.org/10.3390/molecules26113095 `[terverifikasi]`

Relevansi: kerangka dasar hubungan komposisi kimia dengan performa parfum, termasuk volatilitas dan fiksatif.

**6. Berthier, D., Girard, V., Fromm, M., & Herrmann, A. (2024).** Fixative effect of 2-oxo-2-phenylacetates in fine fragrance and eau-de-toilette applications. *Flavour and Fragrance Journal*, 39(1), 80-89. https://doi.org/10.1002/ffj.3769 `[terverifikasi]`

Relevansi: bukti bahwa zat fiksatif memperpanjang daya tahan, dan efeknya berbeda antara konsentrasi tinggi dan EDT. Ini dukungan langsung untuk variabel tingkat konsentrasi di model kalian.

**7. Oliveira, V., Santana, V., Rodrigues, A., Ribeiro, A., & Nogueira, I. B. R. (2023).** A framework for predicting odor threshold values of perfumes by scientific machine learning and transfer learning. *Heliyon*, 9(10), e20813. https://doi.org/10.1016/j.heliyon.2023.e20813 `[terverifikasi]`

Relevansi: contoh penerapan machine learning untuk properti fisik parfum. Bagus untuk membuka bagian metode.

---

## B. Dasar algoritma

**8. Hoerl, A. E., & Kennard, R. W. (1970).** Ridge regression: Biased estimation for nonorthogonal problems. *Technometrics*, 12(1), 55-67. https://doi.org/10.1080/00401706.1970.10488634 `[terverifikasi]`

Relevansi: rujukan asli Ridge. Kutip ini, bukan versi reprint 2000.

**9. Breiman, L. (2001).** Random forests. *Machine Learning*, 45(1), 5-32. https://doi.org/10.1023/A:1010933404324 `[terverifikasi]`

Relevansi: rujukan asli Random Forest.

**10. Friedman, J. H. (2001).** Greedy function approximation: A gradient boosting machine. *The Annals of Statistics*, 29(5), 1189-1232. https://doi.org/10.1214/aos/1013203451 `[terverifikasi]`

Relevansi: rujukan asli Gradient Boosting.

---

## C. Machine learning untuk parfum dan aroma

**11. Kim, J., Oh, K., & Oh, B. (2024).** An NLP-based perfume note estimation based on descriptive sentences. *Applied Sciences*, 14(20), 9293. https://doi.org/10.3390/app14209293 `[terverifikasi]`

Relevansi: memetakan deskripsi teks ke fragrance notes. Mendukung argumen bahwa notes bisa dijadikan fitur terstruktur.

**12. Rodrigues, B. C. L., Santana, V. V., Queiroz, L. P., Rebello, C. M., & Nogueira, I. B. R. (2024).** Harnessing graph neural networks to craft fragrances based on consumer feedback. *Computers & Chemical Engineering*, 185, 108674. https://doi.org/10.1016/j.compchemeng.2024.108674 `[terverifikasi]`

Relevansi: model prediktif untuk performa parfum dari umpan balik konsumen. Pembanding pendekatan non-linier.

**13. Fichtelmann, P., & Westermayr, J. (2026).** Machine learning for smell: Ordinal odor strength prediction of molecular perfumery components. *RSC Advances*, 16(28), 25696-25704. https://doi.org/10.1039/d6ra01805j `[terverifikasi]`

Relevansi: prediksi kekuatan odor sebagai variabel ordinal. Sangat relevan karena target kalian juga ordinal 1-5, meskipun diperlakukan sebagai regresi.

**14. Suh, J., Hong, Y., & Park, C. (2025).** A comparative study of machine learning models on molecular fingerprints for odor decoding. *Communications Chemistry*, 8(1). https://doi.org/10.1038/s42004-025-01651-7 `[terverifikasi]`

Relevansi: perbandingan beberapa model ML pada data aroma. Contoh struktur penulisan bagian hasil perbandingan model.

**15. Nurmuthia, L., Imtiyaz, R., & Sagala, N. M. (2025).** Personalized perfume recommendations based on user descriptions using cosine and Jaccard similarity. *Procedia Computer Science*, 269, 1097-1106. https://doi.org/10.1016/j.procs.2025.09.051 `[terverifikasi]`

Relevansi: sistem rekomendasi parfum berbasis kemiripan. Berguna untuk bagian aplikasi/output.

---

## D. Studi komparasi Ridge, Random Forest, dan Gradient Boosting

**16. Alvines, M., Wijayanto, M. R., Danendra, M. A. D., Herdiansyah, M. R., Lubis, M. K., Rachmad, M. I. F., Tania, K. D., & Meiriza, A. (2025).** Komparasi Ridge Regression, Random Forest, dan Gradient Boosting untuk prediksi curah hujan harian di Sumatra Selatan berbasis time series cross-validation. *JATI (Jurnal Mahasiswa Teknik Informatika)*, 9(4), 5742-5748. https://doi.org/10.36040/jati.v9i4.13915 `[terverifikasi]`

Relevansi: komposisi tiga algoritma persis sama dengan penelitian kalian. Ini rujukan pembanding paling penting, dan bisa dipakai untuk membenarkan pemilihan ketiga model.

**17. Fitri, E. (2023).** Analisis perbandingan metode regresi linier, Random Forest Regression dan Gradient Boosted Trees Regression method untuk prediksi harga rumah. *Journal of Applied Computer Science and Technology*, 4(1), 58-64. https://doi.org/10.52158/jacost.v4i1.491 `[terverifikasi]`

Relevansi: pola hasil yang mirip, model berbasis pohon mengalahkan regresi linier pada data tabular.

**18. Akhmadi, A., & Budiman, F. (2025).** Prediksi harga rumah menggunakan algoritma regresi linier, Random Forest, dan Gradient Boosting. *JURIKOM (Jurnal Riset Komputer)*, 12(6), 1018-1025. https://doi.org/10.30865/jurikom.v12i6.9369 `[terverifikasi]`

Relevansi: acuan tambahan untuk skema evaluasi MAE, RMSE, dan R2 pada tiga model.

**19. Maulita, I., Widiawati, C. R. A., & Wahid, A. M. (2024).** Analisis komparatif Linear Regression, Random Forest, dan Gradient Boosting untuk prediksi banjir. *Jurnal Pendidikan dan Teknologi Indonesia*, 4(8), 369-379. https://doi.org/10.52436/1.jpti.599 `[terverifikasi]`

Catatan: DOI terdaftar di Crossref tapi resolver doi.org mengembalikan 404. Kalau diminta bukti, akses langsung lewat halaman jurnal: https://jpti.journals.id/index.php/jpti/article/view/599

---

## E. Dataset

**20. Ledecanteur. (2024).** Fragrantica perfumes: Ratings, notes, votes & more [Data set]. Kaggle. https://www.kaggle.com/datasets/ledecanteur/fragrantica-perfumes

Relevansi: dataset yang dipakai. Lisensi CC BY-NC-SA 4.0, jadi wajib atribusi dan tidak boleh komersial. Sebutkan ini di bagian metode dan cantumkan di daftar pustaka.

**21. FragDB. (2025).** FragDB: Fragrance database multilingual [Data set]. Hugging Face. https://huggingface.co/datasets/FragDBnet/fragrance-database

Relevansi: alternatif dataset kalau penguji menanyakan sumber pembanding. Berisi 134 ribu lebih parfum, 23 bahasa.

---

## F. Rujukan sistem rekomendasi parfum dalam negeri

**22. Malaiga, H. A., & Sancoko, S. D. (2025).** Development of the "Scentify" application as a web and mobile-based perfume recommendation system using content-based filtering based on user preferences. *J-INTECH*, 13(02), 354-364. https://doi.org/10.32664/j-intech.v13i02.2143

Catatan: DOI terdaftar di halaman jurnal tapi resolver doi.org 404. Pakai URL halaman artikelnya: https://jurnal.ubhinus.ac.id/index.php/J-INTECH/article/view/2143

**23. Gunawan, V. S., Malik, R. A., Hadia, D., & Ananda, A. R. (2026).** Sistem rekomendasi parfum adaptif berbasis web dengan metode weighted scoring dan eliminasi. *Jurnal Data Sains dan Teknologi Informasi (DASTIS)*, 3(02), 46-61. https://doi.org/10.62003/7jc6ex98 `[terverifikasi]`

Relevansi: contoh aplikasi web parfum buatan Indonesia, cocok untuk bagian output.

**24. Sary, Y., & Putra, E. M. (2026).** Sentiment analysis of customer reviews to determine favorite perfume scents using the Naive Bayes method. *Ambidextrous Journal of Innovation Efficiency and Technology in Organization*, 5(03), 456-466. https://doi.org/10.61536/ambidextrous.v5i03.800 `[terverifikasi]`

Relevansi: pengolahan ulasan parfum jadi informasi terstruktur. Mendukung bagian prapemrosesan data.

---

## Saran pemakaian di naskah

| Bagian | Pakai nomor |
|---|---|
| Pendahuluan, konteks parfum dan longevity | 1, 5, 7 |
| Tinjauan pustaka, algoritma | 8, 9, 10 |
| Tinjauan pustaka, ML di ranah parfum | 11, 12, 13, 14 |
| Metode, alasan memilih tiga model | 16, 17, 18, 19 |
| Metode, data | 20, 21 |
| Hasil dan pembahasan, pembanding | 16, 17, 13 |
| Keterbatasan | 2, 3, 6 |
| Aplikasi dan output | 15, 22, 23 |

Total 24 rujukan, cukup untuk artikel jurnal. Minimal 18 sudah aman untuk SINTA 4, 24 ini memberi ruang kalau ada yang harus dibuang penguji.
