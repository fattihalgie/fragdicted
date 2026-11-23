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

## BAB III METODOLOGI

### 3.1 Dataset

#### 3.1.1 Sumber Dataset

Dataset yang digunakan adalah Fragrantica Perfumes: Ratings, Notes, Votes and More, yang dipublikasikan pada platform Kaggle oleh penyusun dengan nama pengguna ledecanteur.

| Item | Keterangan |
|---|---|
| Nama dataset | Fragrantica Perfumes: Ratings, Notes, Votes and More |
| Penyusun | Le Decanteur (akun Kaggle ledecanteur) |
| Platform | Kaggle |
| Tautan | https://www.kaggle.com/datasets/ledecanteur/fragrantica-perfumes |
| Jumlah data mentah | 140.228 baris |
| Jumlah kolom | 59 kolom |
| Ukuran berkas | 139 MB (CSV) |
| Tahun publikasi | 2025 |
| Lisensi | CC BY-NC-SA 4.0 |

Sitasi yang digunakan pada laporan:

> Le Decanteur. (2025). Fragrantica Perfumes: Ratings, Notes, Votes and More [Data set]. Kaggle. https://www.kaggle.com/datasets/ledecanteur/fragrantica-perfumes

Data merupakan hasil pengumpulan terstruktur dari halaman produk situs komunitas parfum Fragrantica. Setiap baris merepresentasikan satu produk parfum. Lisensi CC BY-NC-SA 4.0 mengizinkan penggunaan untuk keperluan non-komersial dengan kewajiban mencantumkan atribusi kepada penyusun serta menggunakan lisensi serupa untuk karya turunan. Project ini digunakan murni untuk keperluan akademik dan atribusi dicantumkan pada laporan serta dokumentasi kode.

#### 3.1.2 Karakteristik Dataset

Dataset mentah memuat 140.228 baris, namun tidak seluruh baris layak digunakan. Terdapat dua persoalan utama pada data mentah.

Persoalan pertama adalah keberadaan baris tanpa penilaian. Sebanyak 18.996 baris memiliki nilai vote_count sama dengan nol, dan pada 17.540 baris di antaranya nilai longevity_avg tercatat sebagai 0,00. Nilai tersebut bukan menunjukkan parfum yang tidak tahan lama, melainkan menandakan belum adanya penilaian. Apabila baris tersebut dipertahankan, model akan mempelajari nilai yang secara konseptual keliru.

Persoalan kedua adalah ketidakstabilan penilaian pada baris dengan jumlah penilai sedikit. Sebanyak 82.955 baris memiliki penilai kurang dari 20 orang, dengan nilai median vote_count hanya 11. Pada jumlah penilai sekecil itu, nilai rata-rata belum mencerminkan penilaian populasi.

Berdasarkan pertimbangan tersebut, diterapkan ambang batas vote_count minimal 500. Pengaruh ambang batas terhadap sebaran target disajikan pada tabel berikut.

| Ambang vote_count | Jumlah baris | Deviasi standar target |
|---|---|---|
| Tanpa filter | 140.228 | 1,422 |
| minimal 100 | 26.313 | 0,486 |
| minimal 500 | 8.211 | 0,460 |
| minimal 1.000 | 4.341 | 0,446 |
| minimal 2.000 | 2.046 | 0,435 |
| minimal 5.000 | 631 | 0,439 |

Peningkatan ambang dari tanpa filter menjadi 100 menurunkan deviasi standar secara drastis, dari 1,422 menjadi 0,486. Peningkatan ambang lebih lanjut hanya memberikan penurunan yang sangat kecil. Ambang 500 dipilih karena berada pada titik seimbang antara kualitas target dan jumlah data, serta menghasilkan data yang tidak lagi memuat nilai longevity 0,00.

Dataset akhir yang digunakan berjumlah 8.211 baris dengan 59 kolom mentah.

#### 3.1.3 Variabel Penelitian

Variabel dibagi menjadi empat kelompok.

**Kelompok 1 - Fitur inti, komposisi bahan:**

| Fitur | Tipe Data | Contoh Isi | Perlakuan |
|---|---|---|---|
| accords | Teks terstruktur | woody:45\|sweet:33\|powdery:22 | Dipecah menjadi vektor, 81 kelompok |
| notes_base | Teks terstruktur | Sandalwood:24\|Amber:13\|Vanilla:12 | Dipecah menjadi vektor, 641 jenis |
| notes_middle | Teks terstruktur | Rose:30\|Jasmine:20 | Dipecah menjadi vektor |
| notes_top | Teks terstruktur | Bergamot:49\|Lemon:5 | Dipecah menjadi vektor |

Fitur teks tersebut memuat nama bahan beserta bobotnya pada skala 0 hingga 100. Bobot merepresentasikan seberapa menonjol bahan tersebut menurut pemungutan suara komunitas, sehingga dapat digunakan langsung sebagai nilai fitur, bukan sekadar penanda keberadaan.

**Kelompok 2 - Fitur pendukung, karakteristik produk:**

| Fitur | Tipe Data | Rentang atau Kategori | Perlakuan |
|---|---|---|---|
| vote_count | Numerik integer | 0 hingga 36.883 | Transformasi log1p |
| year | Numerik integer | Tahun rilis parfum | Nilai kosong diisi median |
| gender | Kategorikal | male, female, unisex | One-hot encoding |
| brand | Kategorikal | 1.288 nilai unik | Target encoding |

**Kelompok 3 - Fitur tambahan, tingkat konsentrasi:**

| Fitur | Tipe Data | Kategori | Perlakuan |
|---|---|---|---|
| concentration | Kategorikal | extrait, edp, edt, edc, unknown | One-hot encoding |
| conc_known | Biner | 0, 1 | Penanda keberhasilan identifikasi |

Tingkat konsentrasi tidak tersedia sebagai kolom eksplisit pada dataset. Nilainya diekstraksi dari kolom name dan description menggunakan pencocokan pola. Cakupan ekstraksi mencapai 34,4 persen baris, terdiri atas 8,5 persen dari nama produk dan sisanya dari deskripsi. Pada subset yang berhasil diidentifikasi, rata-rata longevity menunjukkan pola yang konsisten dengan teori.

| Konsentrasi | Jumlah baris | Rata-rata longevity |
|---|---|---|
| Extrait | 27 | 4,042 |
| Eau de Parfum | 455 | 3,391 |
| Eau de Toilette | 169 | 3,162 |
| Eau de Cologne | 48 | 3,030 |

Analisis varians pada subset tersebut menunjukkan konsentrasi menjelaskan 14,80 persen variasi longevity. Meskipun demikian, karena cakupan hanya sepertiga data, kontribusi fitur ini terhadap performa model terbatas. Pengujian awal menunjukkan kenaikan R² sebesar 0,007 pada Gradient Boosting dan 0,0005 pada Random Forest. Kolom conc_known ditambahkan agar model dapat membedakan antara konsentrasi rendah yang sebenarnya dan konsentrasi yang tidak diketahui.

**Kelompok 4 - Fitur yang ditolak:**

| Kolom | Korelasi dengan target | Alasan penolakan |
|---|---|---|
| sillage_avg | +0,903 | Berasal dari blok pemungutan suara yang sama dengan longevity |
| rating_avg | +0,293 | Merupakan target alternatif dengan konsep tumpang tindih |
| price_value_avg | -0,216 | Berasal dari blok pemungutan suara yang sama |

Kolom sillage_avg khususnya berbahaya. Korelasi sebesar 0,903 menunjukkan bahwa penilaian sillage dan longevity hampir identik, karena keduanya diisi oleh pengguna yang sama pada sesi penilaian yang sama. Apabila kolom tersebut digunakan sebagai fitur, nilai R² model akan terlihat sangat tinggi namun model tidak benar-benar melakukan prediksi, melainkan menyalin jawaban. Kondisi ini disebut kebocoran data (data leakage).

#### 3.1.4 Target Penelitian

| Properti | Nilai |
|---|---|
| Nama kolom | longevity_avg |
| Tipe data | Numerik kontinu |
| Skala | 1 hingga 5 |
| Arti skala | 1 Very Weak, 2 Weak, 3 Moderate, 4 Long Lasting, 5 Eternal |
| Rata-rata pada data terfilter | 3,271 |
| Deviasi standar | 0,460 |
| Kemiringan distribusi | +0,002 |
| Rentang pada data terfilter | 1,54 hingga 4,90 |

Nilai target merupakan rata-rata penilaian longevity dari seluruh pengguna yang memberikan suara pada parfum tersebut. Karena bersifat kontinu dan bukan kategorikal, permasalahan ini termasuk kategori regresi. Distribusi target yang hampir simetris sempurna, ditunjukkan oleh kemiringan +0,002, berarti tidak diperlukan transformasi target.

### 3.2 Tahapan Penelitian

Penelitian dilaksanakan melalui tujuh tahap yang berurutan.

1. Pengumpulan dan pemahaman data, mencakup penelusuran sumber dataset, pembacaan kamus data, dan pemahaman arti setiap kolom.
2. Eksplorasi data, mencakup statistik deskriptif, pemeriksaan nilai hilang, duplikat, pencilan, distribusi target, serta korelasi antarvariabel.
3. Praproses data, mencakup pembersihan, penanganan nilai hilang, pengodean variabel kategorikal, rekayasa fitur, pencegahan kebocoran data, dan pembagian data.
4. Pembangunan model, mencakup pelatihan tiga algoritma regresi dengan konfigurasi yang terdokumentasi.
5. Evaluasi dan perbandingan model menggunakan metrik MAE, MSE, RMSE, dan R², disertai analisis overfitting.
6. Pemilihan model terbaik berdasarkan hasil evaluasi dan pertimbangan karakteristik permasalahan.
7. Implementasi aplikasi web sederhana yang menjalankan model terbaik.

### 3.3 Eksplorasi Data

#### 3.3.1 Informasi Umum Dataset

Pemeriksaan awal dilakukan menggunakan atribut bentuk data, tipe data setiap kolom, dan cuplikan baris. Dataset mentah memiliki 140.228 baris dan 59 kolom dengan tipe data campuran, yaitu numerik, kategorikal, dan teks terstruktur. Setelah penerapan ambang vote_count minimal 500, data yang digunakan berjumlah 8.211 baris.

#### 3.3.2 Statistik Deskriptif

Statistik deskriptif dihitung untuk seluruh kolom numerik. Fokus utama diberikan pada kolom target dan kolom pendukung utama.

| Statistik | vote_count | longevity_avg |
|---|---|---|
| Rata-rata | 3.248,7 | 3,271 |
| Deviasi standar | 4.512,3 | 0,460 |
| Nilai minimum | 500 | 1,54 |
| Median | 1.598 | 3,30 |
| Nilai maksimum | 36.883 | 4,90 |

Kolom vote_count memiliki rentang yang sangat lebar dan distribusi yang sangat miring ke kanan, sehingga ditransformasi menggunakan logaritma. Kolom longevity_avg memiliki sebaran yang sempit dan simetris.

#### 3.3.3 Pemeriksaan Nilai Hilang

| Kolom | Persentase nilai hilang |
|---|---|
| notes_base | 15,6 persen |
| year | 2,8 persen |
| accords | 0,1 persen |
| longevity_avg | 0 persen |

Kolom target tidak memiliki nilai hilang, sehingga seluruh baris dapat digunakan untuk pelatihan. Nilai hilang pada kolom notes dan accords ditangani dengan memperlakukan ketiadaan bahan sebagai nilai nol pada vektor fitur, sedangkan nilai hilang pada kolom year diisi menggunakan nilai median.

#### 3.3.4 Pemeriksaan Data Duplikat

Pemeriksaan dilakukan berdasarkan kombinasi nama produk dan nama brand. Baris duplikat dihapus dengan mempertahankan kemunculan pertama. Penghapusan duplikat penting dilakukan karena baris kembar dapat membuat model berat sebelah terhadap produk tertentu.

#### 3.3.5 Pemeriksaan Pencilan

| Kolom | Jumlah pencilan | Persentase |
|---|---|---|
| longevity_avg | 49 | 0,6 persen |
| vote_count | 882 | 10,7 persen |

Pencilan pada kolom target dipertahankan karena nilainya masih berada dalam skala sah 1 hingga 5 dan merepresentasikan penilaian komunitas yang valid. Pencilan pada vote_count tidak dihapus, melainkan ditangani melalui transformasi logaritma.

#### 3.3.6 Distribusi Target

Distribusi longevity_avg divisualisasikan menggunakan histogram. Hasilnya menunjukkan sebaran yang mendekati simetris dengan kemiringan +0,002, terkonsentrasi pada rentang 3,0 hingga 3,8. Karena distribusi sudah simetris, tidak diperlukan transformasi pada target.

#### 3.3.7 Korelasi Antarvariabel

Perhitungan korelasi dilakukan antara target dan seluruh kolom numerik untuk mengidentifikasi variabel yang berpotensi menjadi fitur sekaligus mendeteksi kebocoran data.

| Kolom | Korelasi dengan longevity_avg | Tindakan |
|---|---|---|
| sillage_avg | +0,903 | Ditolak |
| rating_avg | +0,293 | Ditolak |
| winter | +0,239 | Dipertimbangkan |
| want | +0,219 | Dipertimbangkan |
| price_value_avg | -0,216 | Ditolak |
| vote_count | +0,114 | Digunakan dengan transformasi log |

Korelasi sebesar 0,903 pada sillage_avg menjadi temuan paling penting pada tahap eksplorasi, karena nilai tersebut mengindikasikan kebocoran data. Visualisasi matriks korelasi juga digunakan untuk memeriksa korelasi antarfitur yang berpotensi menimbulkan multikolinearitas.

### 3.4 Praproses Data

#### 3.4.1 Pembersihan Data

Pembersihan mencakup penghapusan baris duplikat, penyeragaman tipe data, dan penerapan ambang vote_count minimal 500. Hasil akhir pembersihan adalah 8.211 baris siap olah.

#### 3.4.2 Penanganan Nilai Hilang

Nilai hilang pada kolom year diisi dengan median tahun rilis. Pendekatan median dipilih karena distribusi tahun rilis tidak simetris dan median lebih tahan terhadap nilai ekstrem dibandingkan rata-rata. Nilai hilang pada kolom notes dan accords tidak diisi, melainkan direpresentasikan sebagai nilai nol pada vektor fitur, yang secara semantik berarti bahan tersebut tidak tercatat pada produk.

#### 3.4.3 Pengodean Variabel Kategorikal

| Kolom | Metode | Alasan |
|---|---|---|
| gender | One-hot encoding | Hanya tiga kategori, tanpa urutan |
| concentration | One-hot encoding | Empat kategori ditambah penanda unknown |
| brand | Target encoding | Kardinalitas tinggi, 1.288 nilai unik |

Target encoding dipilih untuk kolom brand karena one-hot encoding pada 1.288 kategori akan menghasilkan vektor yang sangat jarang dan berpotensi menyebabkan multikolinearitas.

#### 3.4.4 Rekayasa Fitur

Rekayasa fitur mencakup empat hal. Pertama, pemecahan kolom notes dan accords menjadi vektor fitur, di mana setiap jenis bahan menjadi satu kolom dengan nilai bobotnya. Kedua, ekstraksi tingkat konsentrasi dari kolom name dan description menggunakan pencocokan pola. Ketiga, transformasi logaritma pada vote_count menggunakan log1p untuk mengurangi kemiringan distribusi. Keempat, pembuatan fitur turunan berupa jumlah jenis notes pada tiap lapisan piramida aroma.

#### 3.4.5 Pencegahan Kebocoran Data

Tiga kolom ditolak berdasarkan hasil analisis korelasi dan pemahaman terhadap proses pembentukan data, yaitu sillage_avg, rating_avg, dan price_value_avg. Penolakan ini didasarkan pada pertimbangan bahwa ketiga kolom tersebut dihasilkan dari blok pemungutan suara yang sama dengan target, sehingga memuat informasi yang tumpang tindih. Selain penolakan kolom, pencegahan kebocoran data juga dilakukan dengan memastikan bahwa proses pengodean dan penskalaan hanya di-fit pada data latih.

#### 3.4.6 Pembagian Data

Data dibagi menjadi data latih dan data uji dengan proporsi 80 banding 20. Pembagian dilakukan menggunakan train_test_split dengan random_state tetap agar hasil dapat direproduksi. Data uji tidak digunakan pada proses pelatihan maupun pada proses pemilihan hyperparameter. Untuk memperkuat validitas evaluasi, digunakan pula K-Fold Cross Validation pada data latih.

### 3.5 Pengembangan Model

#### 3.5.1 Konfigurasi Algoritma

Tiga algoritma regresi dilatih pada data latih yang sama dan dievaluasi pada data uji yang sama. Konfigurasi awal yang direncanakan adalah sebagai berikut.

| Model | Konfigurasi Awal | Pertimbangan |
|---|---|---|
| Ridge Regression | alpha = 1.0, solver otomatis | Nilai alpha akan disetel melalui Grid Search pada rentang 0,01 hingga 100 |
| Random Forest Regression | n_estimators = 200, max_depth = None, random_state = 42 | Kedalaman dibiarkan bebas, overfitting dikendalikan melalui evaluasi pada data uji |
| Gradient Boosting Regression | n_estimators = 200, learning_rate = 0.05, max_depth = 3, random_state = 42 | Learning rate kecil dengan jumlah pohon sedang untuk menjaga kestabilan |

Seluruh model dilatih menggunakan data latih yang telah melalui praproses. Penyetelan hyperparameter dilakukan menggunakan K-Fold Cross Validation pada data latih, bukan pada data uji.

#### 3.5.2 Alasan Pemilihan Algoritma

Pemilihan ketiga algoritma didasarkan pada pertimbangan berikut, bukan pada percobaan acak.

**Ridge Regression** dipilih sebagai representasi model linear dengan regularisasi. Model ini berfungsi sebagai pembanding dasar sekaligus menguji apakah hubungan antara komposisi bahan dan longevity dapat dijelaskan secara linear. Ridge dipilih menggantikan regresi linear murni karena pengujian awal menunjukkan bahwa regresi linear tanpa regularisasi gagal pada data ini, dengan R² sebesar negatif 1,893 pada 641 fitur base notes, sedangkan Ridge menghasilkan negatif 0,394.

**Random Forest Regression** dipilih sebagai representasi metode ensemble berbasis bagging. Model ini mampu menangkap hubungan non-linear dan interaksi antarfitur tanpa memerlukan asumsi bentuk fungsi, serta tidak menuntut normalisasi fitur. Model ini juga menyediakan atribut feature_importances_ yang dapat digunakan untuk menginterpretasikan kontribusi tiap bahan.

**Gradient Boosting Regression** dipilih sebagai representasi metode ensemble berbasis boosting. Model ini umumnya memberikan performa terbaik pada data tabular berukuran sedang dan lebih stabil terhadap overfitting dibandingkan Random Forest. Kehadiran kedua metode ensemble memungkinkan perbandingan antara pendekatan paralel dan berurutan pada data yang sama.

#### 3.5.3 Skenario Pengujian Fitur

Selain membandingkan algoritma, project ini membandingkan empat skenario fitur untuk mengetahui kontribusi masing-masing representasi komposisi.

| Skenario | Fitur yang digunakan | Tujuan |
|---|---|---|
| A | notes_base saja | Mengukur daya prediksi notes secara tunggal |
| B | accords saja | Mengukur daya prediksi accords secara tunggal |
| C | accords dan notes digabung | Mengukur daya prediksi gabungan |
| D | C ditambah konsentrasi dan conc_known | Mengukur kontribusi tambahan konsentrasi |

Hasil pengujian awal menunjukkan skenario B menghasilkan R² sebesar 0,381 dengan MAE 0,281, skenario A menghasilkan R² sebesar 0,185 dengan MAE 0,324, dan skenario C menghasilkan R² sebesar 0,396 dengan MAE 0,277. Skenario D sedang diuji dan dilaporkan pada laporan akhir.

#### 3.5.4 Baseline Pembanding

Sebagai pembanding, dihitung baseline yang memprediksi nilai rata-rata target pada data latih untuk seluruh data uji. Baseline ini menghasilkan MAE sebesar 0,370. Nilai tersebut menjadi ambang Batasan: model yang memiliki MAE lebih besar dari 0,370 berarti tidak lebih baik daripada sekadar menebak nilai rata-rata.

### 3.6 Evaluasi Model

Evaluasi dilakukan menggunakan empat metrik wajib, yaitu MAE, MSE, RMSE, dan R². Selain nilai metrik, evaluasi mencakup tiga analisis tambahan.

Pertama, perbandingan R² pada data latih dan data uji untuk setiap model, guna mengidentifikasi indikasi overfitting. Selisih yang besar antara keduanya menunjukkan model menghafal data latih.

Kedua, analisis kesalahan prediksi, mencakup identifikasi parfum dengan kesalahan terbesar dan pemeriksaan apakah kesalahan terkonsentrasi pada segmen tertentu, misalnya pada parfum dengan vote_count rendah atau pada konsentrasi tertentu.

Ketiga, analisis kepentingan fitur menggunakan atribut feature_importances_ pada Random Forest dan Gradient Boosting, serta nilai koefisien pada Ridge Regression. Hasilnya digunakan untuk mengidentifikasi bahan yang paling berpengaruh terhadap longevity.

Perbandingan performa antar model disajikan dalam bentuk tabel sebagai berikut.

| Model | MAE | MSE | RMSE | R² data uji | R² data latih | Selisih R² |
|---|---|---|---|---|---|---|
| Ridge Regression | diisi setelah pengujian | diisi setelah pengujian | diisi setelah pengujian | diisi setelah pengujian | diisi setelah pengujian | diisi setelah pengujian |
| Random Forest Regression | diisi setelah pengujian | diisi setelah pengujian | diisi setelah pengujian | diisi setelah pengujian | diisi setelah pengujian | diisi setelah pengujian |
| Gradient Boosting Regression | diisi setelah pengujian | diisi setelah pengujian | diisi setelah pengujian | diisi setelah pengujian | diisi setelah pengujian | diisi setelah pengujian |

Pemilihan model terbaik tidak semata-mata didasarkan pada nilai metrik tertinggi. Pertimbangan lain mencakup stabilitas model, selisih R² antara data latih dan data uji, waktu prediksi yang layak untuk aplikasi web, serta kemudahan interpretasi hasil.

### 3.7 Implementasi Aplikasi

Model terbaik disimpan menggunakan joblib dalam bentuk berkas pkl, kemudian dijalankan melalui aplikasi web berbasis Streamlit. Aplikasi dirancang dengan tiga komponen sesuai ketentuan tugas.

| Komponen | Rancangan |
|---|---|
| Input | Pemilihan notes dari daftar, pemilihan accords, pemilihan tingkat konsentrasi, serta input jumlah vote |
| Proses | Data masukan diubah menjadi vektor fitur menggunakan pipeline yang sama dengan proses pelatihan, kemudian model melakukan prediksi |
| Output | Skor longevity dalam skala 1 hingga 5, kategori interpretasi (Weak, Moderate, Long Lasting, Eternal), serta grafik pendukung |

Alur pemrosesan pada aplikasi mengikuti pola: data masukan, praproses, model machine learning, prediksi, lalu hasil. Aplikasi dijalankan secara lokal dan didemonstrasikan langsung pada video demo.

### 3.8 Rencana Luaran

| Luaran | Bentuk |
|---|---|
| Model terlatih | Berkas pkl hasil pelatihan model terbaik |
| Kode sumber | Notebook tahapan EDA, praproses, pemodelan, serta berkas aplikasi |
| Aplikasi | Aplikasi web Streamlit beserta berkas requirements |
| Laporan | Presentasi berisi 15 bagian sesuai ketentuan |
| Video demo | Rekaman layar berdurasi maksimal 7 menit |
| Dataset | Berkas CSV dan tautan sumber |

<<<PB>>>

## DAFTAR PUSTAKA

Daftar pustaka berikut telah lengkap dan sesuai APA edisi 7. Periksa kesesuaian sitasi pada BAB I dan BAB II dengan entri di sini, urutan alfabetis, serta kelengkapan DOI.

Fichtelmann, P., & Westermayr, J. (2026). Machine learning for smell: Ordinal odor strength prediction of molecular perfumery components. *RSC Advances*, 16(28), 25696-25704. https://pubmed.ncbi.nlm.nih.gov/42158754/

Kim, J., Oh, K., & Oh, B.-S. (2024). An NLP-based perfume note estimation based on descriptive sentences. *Applied Sciences*, 14(20), 9293. https://doi.org/10.3390/app14209293

Le Decanteur. (2025). *Fragrantica Perfumes: Ratings, Notes, Votes and More* [Data set]. Kaggle. https://www.kaggle.com/datasets/ledecanteur/fragrantica-perfumes

Nikolic, M., & Marjanovic, M. (2025). Data science meets fragrance: Analyzing user reviews to decode emotional connections to perfume notes. Dalam *Proceedings of the International Scientific Conference on Information Technology, Computer Science, and Data Science (SINTEZA 2025)* (hlm. 213-220). https://doi.org/10.15308/Sinteza-2025-213-220

Nikolic, M., Marjanovic, M., & Radenovic, Z. (2024). Application of machine learning for perfume popularity prediction: Analysis of fragrance notes and consumer behavior. *Proceedings of the Academy of Applied Technical and Preschool Studies Nis*, 64-67.

Nurmuthia, L. D., Imtiyaza, R., & Sagala, N. T. M. (2025). Personalized perfume recommendations based on user descriptions using cosine and Jaccard similarity. *Procedia Computer Science*, 269, 1097-1106. https://doi.org/10.1016/j.procs.2025.09.051

Rodrigues, B. C. L., Santana, V. V., Queiroz, L. P., Rebello, C. M., & Nogueira, I. B. R. (2024). Harnessing graph neural networks to craft fragrances based on consumer feedback. *Computers & Chemical Engineering*, 185, 108674. https://doi.org/10.1016/j.compchemeng.2024.108674

<<<PB>>>

## LAMPIRAN

### Lampiran 1. Daftar Kolom Utama Dataset

| No | Nama Kolom | Tipe Data | Keterangan |
|---|---|---|---|
| 1 | name | Teks | Nama produk parfum |
| 2 | brand | Teks | Nama rumah parfum |
| 3 | gender | Kategorikal | male, female, unisex |
| 4 | year | Numerik | Tahun rilis parfum |
| 5 | vote_count | Numerik | Jumlah pengguna yang memberi penilaian |
| 6 | rating_avg | Numerik | Rata-rata penilaian umum, skala 1 hingga 5 |
| 7 | longevity_avg | Numerik | Rata-rata penilaian ketahanan, target penelitian |
| 8 | sillage_avg | Numerik | Rata-rata penilaian penyebaran aroma |
| 9 | price_value_avg | Numerik | Rata-rata penilaian nilai harga |
| 10 | accords | Teks terstruktur | Daftar accord beserta bobot |
| 11 | notes_top | Teks terstruktur | Daftar top notes beserta bobot |
| 12 | notes_middle | Teks terstruktur | Daftar middle notes beserta bobot |
| 13 | notes_base | Teks terstruktur | Daftar base notes beserta bobot |
| 14 | description | Teks | Deskripsi produk |
| 15 | perfumers | Teks | Nama peracik parfum |

### Lampiran 2. Contoh Format Data Terstruktur

Kolom komposisi bahan disimpan dalam format pasangan nama dan bobot yang dipisahkan karakter pipa, sebagai berikut.

> accords: woody:45|sweet:33|powdery:22|musky:18
> notes_base: Sandalwood:24|Amber:13|Vanilla:12|Musk:9
> notes_middle: Rose:30|Jasmine:20|Orris:11
> notes_top: Bergamot:49|Lemon:5|Pink Pepper:4

Format tersebut diubah menjadi vektor fitur melalui pemecahan berdasarkan karakter pipa dan pemisahan nama bahan dari bobotnya. Setiap jenis bahan yang ditemukan pada seluruh dataset menjadi satu kolom tersendiri, dan nilai bobot diisi pada kolom yang sesuai. Apabila suatu bahan tidak tercatat pada sebuah produk, kolom tersebut bernilai nol.

### Lampiran 3. Rencana Pembagian Tugas

| Anggota | Tugas Utama | Pemahaman yang Wajib Dikuasai |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

Kolom anggota dan tugas diisi sesuai pembagian yang disepakati kelompok. Seluruh anggota wajib memahami keseluruhan alur project, karena penilaian presentasi dan tanya jawab bersifat individual.
