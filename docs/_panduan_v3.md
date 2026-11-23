# PANDUAN PENYUSUNAN PROPOSAL
## Pembagian Tugas Penyusunan Proposal Project Akhir Prediksi Longevity Parfum
### Mata Kuliah Pembelajaran Mesin (TEK1314) - Kelas A

| Nama | NIM |
|---|---|
| Fattih Algie Maulana | J0404241002 |
| Aisyah Elfiyuni M.A | J0404241067 |
| Anggi Permana Putra | J0404241154 |

Dokumen ini memuat susunan bab dan subbab yang sama dengan proposal final. Setiap subbab berisi keterangan mengenai isi yang harus ditulis. BAB III dilampirkan utuh sebagai acuan gaya penulisan.

Ketentuan umum: gunakan bahasa Indonesia baku, setiap paragraf terdiri atas empat sampai delapan kalimat, setiap klaim disertai sitasi, istilah asing dicetak miring, dan bilangan desimal menggunakan koma.

<<<PB>>>

## BAB I PENDAHULUAN

### 1.1 Latar Belakang

Uraikan sejarah dan perkembangan industri parfum, pergeseran pembelian ke kanal daring, pentingnya longevity bagi konsumen, dasar kimia daya tahan aroma, peran konsentrasi, serta peluang penerapan machine learning. Sertakan minimal tiga sitasi dari jurnal pada Daftar Pustaka.

### 1.2 Rumusan Masalah

Rumuskan satu pertanyaan utama mengenai prediksi longevity berdasarkan notes, accords, dan tingkat konsentrasi. Turunkan pertanyaan tersebut menjadi empat sampai lima pertanyaan rinci yang seluruhnya dapat dijawab pada BAB III.

### 1.3 Tujuan

Tuliskan tujuan yang menjawab setiap pertanyaan rinci pada subbab 1.2 secara berurutan. Gunakan kata kerja operasional seperti menganalisis, mengidentifikasi, menguji, membangun, membandingkan, dan mengimplementasikan.

### 1.4 Manfaat

Jelaskan manfaat teoretis sebagai pembeda dari penelitian terdahulu yang bekerja pada tingkat molekul atau melalui teks ulasan. Uraikan manfaat praktis bagi konsumen, pelaku usaha, dan mahasiswa.

### 1.5 Batasan Masalah

Nyatakan lima batasan penelitian, mencakup sifat longevity sebagai persepsi, penggunaan satu sumber data, cakupan identifikasi konsentrasi sebesar 34,4 persen, ruang lingkup regresi tabular, dan bentuk aplikasi lokal.

## BAB II TINJAUAN PUSTAKA

### 2.1 Landasan Teori

Bagian ini menjelaskan konsep yang digunakan pada BAB III, bukan merangkum jurnal. Setiap istilah yang muncul di BAB III harus memiliki penjelasan di sini, dan setiap subbab minimal mengutip satu sumber.

#### 2.1.1 Parfum dan Longevity

Jelaskan komposisi parfum, piramida aroma tiga lapis, alasan base notes bertahan paling lama, serta cara longevity diukur di Fragrantica. Tegaskan bahwa nilai tersebut merupakan persepsi pengguna, bukan hasil pengukuran laboratorium.

#### 2.1.2 Fragrance Notes dan Accords

Jelaskan perbedaan fragrance notes sebagai bahan satuan dengan accords sebagai kesan aroma keseluruhan, termasuk format penyimpanan nama dan bobotnya. Nyatakan alasan kedua representasi digunakan bersamaan.

#### 2.1.3 Tingkat Konsentrasi

Jelaskan hubungan tingkat konsentrasi dengan daya tahan aroma, lalu sajikan tabel perbandingan extrait, EDP, EDT, dan EDC beserta kadar minyak dan perkiraan daya tahannya. Tambahkan catatan bahwa konsentrasi tinggi tidak selalu berarti lebih baik.

#### 2.1.4 Regresi dalam Machine Learning

Jelaskan perbedaan regresi dan klasifikasi serta alasan longevity diperlakukan sebagai target kontinu. Berikan contoh yang menunjukkan hilangnya informasi jarak apabila target diperlakukan sebagai kelas.

#### 2.1.5 Ridge Regression

Jelaskan regularisasi L2 dan kaitannya dengan multikolinearitas pada data berdimensi tinggi. Sertakan bukti dari project ini, yaitu R² regresi linear tanpa regularisasi sebesar negatif 1,893 dan Ridge sebesar negatif 0,394.

#### 2.1.6 Random Forest Regression

Jelaskan mekanisme bagging dan pembentukan pohon pada Random Forest beserta kelebihan dan kekurangannya. Sebutkan indikasi overfitting pada project ini, yaitu R² data latih 0,912 dan data uji 0,382.

#### 2.1.7 Gradient Boosting Regression

Jelaskan mekanisme boosting yang membangun model secara berurutan dan peran learning rate di dalamnya. Bandingkan sifatnya dengan Random Forest dari sisi kestabilan pada data tabular.

#### 2.1.8 Metrik Evaluasi

Jelaskan cara hitung dan cara menafsirkan MAE, MSE, RMSE, dan R² pada skala 1 sampai 5. Sertakan penjelasan mengenai arti R² bernilai nol dan negatif.

### 2.2 Studi Literatur

Bagian ini membahas enam artikel yang telah ditentukan. Tugasnya merangkum dan memetakan, bukan mencari artikel baru.

#### 2.2.1 Ringkasan Artikel Jurnal

Ringkas keenam artikel dalam satu paragraf masing-masing, memuat tujuan, dataset, metode, hasil berupa angka, dan relevansi terhadap project. Gunakan daftar artikel berikut sebagai acuan.

| No | Penulis dan Tahun | Terbitan | Tautan |
|---|---|---|---|
| 1 | Nurmuthia, Imtiyaza, dan Sagala (2025) | Procedia Computer Science | https://doi.org/10.1016/j.procs.2025.09.051 |
| 2 | Kim, Oh, dan Oh (2024) | Applied Sciences | https://doi.org/10.3390/app14209293 |
| 3 | Fichtelmann dan Westermayr (2026) | RSC Advances | https://pubmed.ncbi.nlm.nih.gov/42158754/ |
| 4 | Rodrigues dkk. (2024) | Computers and Chemical Engineering | https://doi.org/10.1016/j.compchemeng.2024.108674 |
| 5 | Nikolic dan Marjanovic (2025) | SINTEZA 2025 | https://doi.org/10.15308/Sinteza-2025-213-220 |
| 6 | Nikolic, Marjanovic, dan Radenovic (2024) | Proceedings AATPS Nis | prosiding, tanpa DOI |

#### 2.2.2 Tabel Studi Literatur

Susun tabel studi literatur dengan delapan kolom sesuai ketentuan, yaitu nomor, penulis dan tahun, permasalahan, dataset, metode, metrik evaluasi, hasil utama, dan perbedaan dengan project. Kolom perbedaan wajib diisi dengan perbedaan yang konkret.

#### 2.2.3 Relevansi Artikel terhadap Project

Susun tabel yang memetakan kebutuhan project terhadap artikel pendukung, mencakup penentuan masalah, pemilihan dataset, praproses, pemilihan algoritma, evaluasi, dan interpretasi kepentingan fitur.

### 2.3 Posisi Penelitian

Kelompokkan keenam artikel menjadi tiga kelompok penelitian, kemudian nyatakan posisi project ini di antaranya. Rumuskan tiga kebaruan dan hindari klaim bahwa penelitian semacam ini belum pernah dilakukan.

<<<PART2>>>END
