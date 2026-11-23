# PANDUAN PENYUSUNAN PROPOSAL
## Pembagian Tugas Penyusunan Proposal Project Akhir Prediksi Longevity Parfum
### Mata Kuliah Pembelajaran Mesin (TEK1314) - Kelas A

| Anggota | NIM | Bagian yang dikerjakan |
|---|---|---|
| Fattih Algie Maulana | J0404241002 | BAB III Metodologi |
| Aisyah Elfiyuni M.A | J0404241067 | BAB II Tinjauan Pustaka |
| Anggi Permana Putra | J0404241154 | BAB I Pendahuluan dan Daftar Pustaka |

**Cara pakai dokumen ini:** susunan bab dan subbab sama persis dengan proposal final. Setiap subbab berisi keterangan mengenai isi yang harus ditulis, bukan isi jadi. BAB III sudah selesai dan dilampirkan utuh sebagai contoh acuan gaya penulisan.

**Aturan umum penulisan:**

1. Setiap paragraf minimal 4 kalimat, maksimal 8 kalimat. Paragraf satu ide.
2. Setiap klaim yang bukan hasil pengamatan sendiri wajib disertai sitasi.
3. Gunakan bahasa Indonesia baku, bukan bahasa lisan. Hindari kata "dimana", "sehingga" di awal kalimat, dan "dilakukan oleh" yang berlebihan.
4. Istilah asing dicetak miring pada kemunculan pertama, contoh: *longevity*, *machine learning*.
5. Angka desimal memakai koma, bukan titik. Contoh: 0,903 bukan 0.903.
6. Jangan menyalin kalimat dari jurnal. Parafrasekan dan sebutkan sumbernya.

<<<PB>>>

## BAB I PENDAHULUAN

### 1.1 Latar Belakang

**Penanggung jawab:** Anggi Permana Putra
**Target:** 4 sampai 6 paragraf, total 450 sampai 600 kata

**Urutan yang harus diikuti:**

1. Paragraf 1, gambaran umum: besarnya industri parfum dan pergeseran transaksi dari toko fisik ke perdagangan elektronik. Sebutkan angka pasar bila ada sumbernya.
2. Paragraf 2, masalah: pembeli daring tidak dapat mencium aroma, sehingga keputusan pembelian bergantung pada deskripsi penjual yang bersifat subjektif.
3. Paragraf 3, pentingnya variabel: jelaskan bahwa *longevity* adalah salah satu pertimbangan utama konsumen, dan kekecewaan lebih sering disebabkan aroma yang cepat hilang daripada ketidaksukaan pada wanginya.
4. Paragraf 4, dasar kimia: jelaskan piramida aroma tiga lapis dan mengapa *base notes* bertahan paling lama. Paragraf ini yang menghubungkan komposisi bahan dengan *longevity*.
5. Paragraf 5, variabel konsentrasi: jelaskan bahwa tingkat konsentrasi menentukan daya tahan, tetapi umumnya tidak dicantumkan pada katalog produk daring.
6. Paragraf 6, solusi: jelaskan bahwa data komunitas Fragrantica memungkinkan pemodelan, lalu perkenalkan pendekatan *machine learning* dan tiga algoritma yang dibandingkan.

**Wajib ada:**

- Minimal tiga sitasi dari enam jurnal pada Daftar Pustaka.
- Satu kalimat yang menyatakan celah penelitian, misalnya bahwa penelitian terdahulu belum memodelkan *longevity* pada tingkat produk jadi.

**Jangan:**

- Menjelaskan dataset secara rinci. Itu tempatnya di BAB III.
- Menjelaskan cara kerja algoritma. Itu tempatnya di BAB II.
- Menulis tujuan penelitian di bagian ini.

### 1.2 Rumusan Masalah

**Penanggung jawab:** Anggi Permana Putra
**Target:** 1 pertanyaan utama dan 4 sampai 5 pertanyaan rinci

**Yang harus diisi:**

1. Satu pertanyaan utama yang memuat variabel bebas (komposisi *notes*, *accords*, konsentrasi) dan variabel terikat (*longevity*).
2. Pertanyaan rinci yang menurun dari pertanyaan utama. Setiap pertanyaan rinci harus dapat dijawab oleh satu bagian di BAB III.

**Contoh pola pertanyaan rinci yang benar:**

1. Bagaimana karakteristik dataset dan permasalahan kualitas datanya?
2. Bahan apa yang paling berpengaruh terhadap *longevity*?
3. Seberapa besar pengaruh tingkat konsentrasi?
4. Algoritma mana yang paling baik?
5. Apa yang membatasi kemampuan model?

**Aturan:** rumusan masalah harus berbentuk kalimat tanya yang diakhiri tanda tanya, bukan pernyataan. Jumlah pertanyaan rinci harus sama dengan jumlah poin pada subbab 1.3.

### 1.3 Tujuan Project

**Penanggung jawab:** Anggi Permana Putra
**Target:** 5 sampai 6 poin

**Yang harus diisi:** setiap poin merupakan jawaban langsung dari pertanyaan rinci pada subbab 1.2. Urutannya harus sejajar, poin pertama menjawab pertanyaan rinci pertama, dan seterusnya.

**Aturan penulisan:** gunakan kata kerja operasional di awal poin, misalnya menganalisis, mengidentifikasi, menguji, membangun, membandingkan, mengimplementasikan, menganalisis.

**Jangan:** menulis tujuan yang tidak ada pertanyaannya di 1.2, dan jangan menulis "mengetahui" karena terlalu umum.

### 1.4 Manfaat Project

**Penanggung jawab:** Anggi Permana Putra
**Target:** 1 paragraf manfaat teoretis dan 3 poin manfaat praktis

**Yang harus diisi:**

1. Manfaat teoretis: kontribusi terhadap kajian pemodelan atribut sensorik produk. Jelaskan bahwa penelitian terdahulu memodelkan pada tingkat molekul atau melalui teks ulasan, sedangkan project ini pada tingkat produk jadi menggunakan komposisi bahan terstruktur.
2. Manfaat praktis poin 1: bagi konsumen, sebagai alat bantu estimasi sebelum membeli.
3. Manfaat praktis poin 2: bagi pelaku usaha, analisis kepentingan fitur sebagai pertimbangan penyusunan komposisi.
4. Manfaat praktis poin 3: bagi mahasiswa, sarana penerapan tahapan *machine learning* secara menyeluruh.

### 1.5 Batasan Masalah

**Penanggung jawab:** Anggi Permana Putra
**Target:** 5 poin

**Yang harus diisi:** batasan harus menyatakan apa yang tidak dicakup penelitian, bukan kekurangan penulis. Lima batasan yang wajib ada:

1. Data berupa penilaian komunitas, bukan pengukuran laboratorium, sehingga *longevity* yang diprediksi adalah persepsi.
2. Hanya satu sumber data, karena perbedaan skala penilaian dan penamaan bahan antarplatform.
3. Konsentrasi diekstraksi dari teks dengan cakupan 34,4 persen, dan keterbatasan ini diakui.
4. Model terbatas pada regresi tabular, tidak mencakup pendekatan molekul, *graph neural network*, atau model bahasa besar.
5. Aplikasi berupa aplikasi lokal sederhana, bukan layanan produksi.

**Jangan:** menulis batasan yang sebenarnya bisa diselesaikan, misalnya "keterbatasan waktu pengerjaan".

## BAB II TINJAUAN PUSTAKA

### 2.1 Landasan Teori

**Penanggung jawab:** Aisyah Elfiyuni M.A

Bagian ini bukan ringkasan jurnal. Fungsinya menjelaskan konsep yang dipakai di BAB III, sehingga setiap konsep yang muncul di BAB III harus punya penjelasannya di sini. Urutannya sengaja dibuat dari konsep domain parfum menuju konsep *machine learning*.

**Aturan:** setiap subbab minimal mengutip satu sumber, dan setiap istilah asing dicetak miring pada kemunculan pertama.

#### 2.1.1 Parfum dan Longevity

**Target:** 2 paragraf

**Yang harus diisi:**

1. Definisi parfum dan penyusunnya, yaitu minyak esensial, senyawa aroma sintetis, dan pelarut.
2. Piramida aroma tiga lapis: *top notes*, *middle notes*, *base notes*. Jelaskan bahwa perbedaan utamanya adalah berat molekul dan titik didih, yang menentukan laju penguapan.
3. Definisi *longevity* dan cara pengukurannya di Fragrantica, yaitu lima tingkat penilaian pengguna, lalu dirata-ratakan.
4. Kalimat yang menyatakan bahwa karena berbasis persepsi, nilai ini juga dipengaruhi kimia kulit, suhu, kelembapan, dan penyimpanan.

**Wajib ada:** penjelasan mengapa *base notes* menjadi penentu utama daya tahan.

#### 2.1.2 Fragrance Notes dan Accords

**Target:** 2 paragraf

**Yang harus diisi:**

1. Definisi *fragrance notes* dan pengelompokannya menurut lapisan piramida.
2. Format penyimpanan pada dataset, yaitu pasangan nama dan bobot yang dipisahkan karakter pipa, contoh: Sandalwood:24|Amber:13|Vanilla:12. Jelaskan bahwa angka menunjukkan seberapa menonjol bahan tersebut menurut komunitas, dengan skala 0 sampai 100.
3. Definisi *accords* sebagai representasi kesan aroma secara keseluruhan, bukan bahan tunggal, contoh: woody, sweet, powdery.
4. Perbandingan: *notes* lebih granular tetapi lebih jarang, *accords* lebih ringkas dan lebih padat. Jelaskan implikasinya pada jumlah fitur.

**Wajib ada:** alasan mengapa kedua representasi dipakai bersamaan, bukan salah satu saja.

#### 2.1.3 Tingkat Konsentrasi

**Target:** 1 paragraf pengantar dan 1 tabel

**Yang harus diisi:** penjelasan bahwa konsentrasi menyatakan persentase minyak wangi dalam larutan, dan bahwa semakin tinggi konsentrasi semakin lambat aroma menguap. Sertakan tabel berikut dan lengkapi kolom kadar minyak serta perkiraan daya tahan dari sumber terpercaya.

| Tingkatan | Nama Lengkap | Perkiraan Kadar Minyak | Perkiraan Daya Tahan |
|---|---|---|---|
| Extrait | Extrait de Parfum | isi | isi |
| EDP | Eau de Parfum | isi | isi |
| EDT | Eau de Toilette | isi | isi |
| EDC | Eau de Cologne | isi | isi |

**Wajib ada:** satu kalimat yang menyatakan bahwa konsentrasi tinggi tidak selalu berarti lebih baik, karena dapat terasa terlalu pekat bagi sebagian pemakai.

#### 2.1.4 Regresi dalam Machine Learning

**Target:** 2 paragraf

**Yang harus diisi:**

1. Definisi regresi sebagai *supervised learning* yang memetakan fitur ke target kontinu, dan bedanya dengan klasifikasi yang menghasilkan label diskret.
2. Alasan target *longevity* diperlakukan sebagai kontinu: skalanya 1 sampai 5 dan berjarak, sehingga jika diperlakukan sebagai kelas, informasi jarak antarnilai hilang. Beri contoh: selisih 3,1 dengan 3,2 tidak sama maknanya dengan selisih 3,1 dengan 4,8.

#### 2.1.5 Ridge Regression

**Target:** 3 paragraf

**Yang harus diisi:**

1. Penjelasan regularisasi L2, yaitu penalti berupa kuadrat besar koefisien pada fungsi objektif, dan tujuannya membatasi koefisien agar model tidak sensitif.
2. Penjelasan multikolinearitas dan mengapa kondisi ini muncul ketika jumlah fitur besar dan antarfitur berkorelasi. Jelaskan akibatnya: koefisien menjadi sangat besar dengan tanda berlawanan dan model tidak stabil.
3. Bukti dari data project ini: regresi linear tanpa regularisasi menghasilkan R² negatif 1,893 pada 641 fitur *base notes*, sedangkan Ridge menghasilkan negatif 0,394.

**Wajib ada:** kalimat yang menyimpulkan bahwa Ridge dipilih karena alasan tersebut, bukan karena kebiasaan.

**Jangan:** menulis rumus panjang tanpa menjelaskan arti setiap simbolnya.

#### 2.1.6 Random Forest Regression

**Target:** 3 paragraf

**Yang harus diisi:**

1. Konsep *ensemble* dan *bagging*: banyak pohon dibangun dari sampel *bootstrap*, dan pada tiap percabangan hanya sebagian fitur dipertimbangkan.
2. Kelebihan: menangkap hubungan non-linear dan interaksi antarfitur tanpa asumsi bentuk fungsi, tahan terhadap pencilan, tidak menuntut normalisasi.
3. Kekurangan: cenderung *overfitting* bila pohon tumbuh sangat dalam, terutama pada data berukuran kecil sampai sedang. Jelaskan bahwa indikasinya adalah selisih besar antara R² data latih dan data uji.

#### 2.1.7 Gradient Boosting Regression

**Target:** 3 paragraf

**Yang harus diisi:**

1. Konsep *boosting*: model dibangun berurutan, model berikutnya mempelajari residual dari model sebelumnya.
2. Peran *learning rate* dalam memperkecil kontribusi setiap model baru.
3. Perbandingan dengan Random Forest: paralel versus berurutan, dan mengapa *boosting* umumnya lebih stabil terhadap *overfitting* pada data tabular berukuran sedang.

#### 2.1.8 Metrik Evaluasi

**Target:** 1 paragraf per metrik, total 5 paragraf

**Yang harus diisi:** satu paragraf untuk masing-masing MAE, MSE, RMSE, dan R². Setiap paragraf menjelaskan cara hitung secara konseptual dan cara menafsirkan nilainya pada skala 1 sampai 5.

**Wajib ada:** penjelasan arti R² bernilai 0 dan negatif, karena pada project ini muncul nilai R² negatif.

**Jangan:** menuliskan rumus matematis tanpa penjelasan verbal. Rumus boleh ada, tetapi harus diikuti kalimat yang menjelaskan artinya.

### 2.2 Studi Literatur

**Penanggung jawab:** Aisyah Elfiyuni M.A

Bagian ini membahas enam artikel yang menjadi rujukan. Seluruh artikel sudah ditentukan, jadi tugasnya membaca, merangkum, dan memetakan, bukan mencari artikel baru.

#### 2.2.1 Ringkasan Artikel Jurnal

**Target:** 6 paragraf, satu paragraf per artikel, masing-masing 90 sampai 130 kata

**Pola setiap paragraf:** tujuan penelitian, dataset yang dipakai, metode atau algoritma, hasil berupa angka bila ada, lalu satu kalimat yang menyatakan relevansinya dengan project ini.

**Daftar artikel yang harus diringkas:**

| No | Penulis dan Tahun | Terbitan | Tautan |
|---|---|---|---|
| 1 | Nurmuthia, Imtiyaza, dan Sagala (2025) | Procedia Computer Science | https://doi.org/10.1016/j.procs.2025.09.051 |
| 2 | Kim, Oh, dan Oh (2024) | Applied Sciences | https://doi.org/10.3390/app14209293 |
| 3 | Fichtelmann dan Westermayr (2026) | RSC Advances | https://pubmed.ncbi.nlm.nih.gov/42158754/ |
| 4 | Rodrigues, Santana, Queiroz, Rebello, dan Nogueira (2024) | Computers and Chemical Engineering | https://doi.org/10.1016/j.compchemeng.2024.108674 |
| 5 | Nikolic dan Marjanovic (2025) | SINTEZA 2025 | https://doi.org/10.15308/Sinteza-2025-213-220 |
| 6 | Nikolic, Marjanovic, dan Radenovic (2024) | Proceedings AATPS Nis | prosiding, tanpa DOI |

**Aturan:** setiap paragraf wajib memuat minimal satu angka hasil dari artikel. Jangan menulis "penelitian ini berhasil membuktikan bahwa metode tersebut baik" tanpa menyebut angka.

#### 2.2.2 Tabel Studi Literatur

**Target:** satu tabel berisi 6 baris dan 8 kolom

**Kolom yang wajib ada, berurutan:** No, Penulis dan Tahun, Permasalahan, Dataset, Metode atau Algoritma, Metrik Evaluasi, Hasil Utama, Perbedaan dengan Project.

**Aturan:** kolom "Perbedaan dengan Project" tidak boleh kosong dan tidak boleh diisi "tidak ada". Setiap baris harus menyatakan satu perbedaan yang konkret, misalnya perbedaan target, perbedaan jenis keluaran, atau perbedaan jenis algoritma.

#### 2.2.3 Relevansi Artikel terhadap Project

**Target:** satu tabel pemetaan

**Yang harus diisi:** tabel dua kolom yang memetakan kebutuhan project ke artikel pendukung. Kebutuhan yang wajib muncul minimal: penentuan permasalahan, pemilihan dataset, metode praproses, pemilihan algoritma, metode evaluasi, dan interpretasi kepentingan fitur.

### 2.3 Posisi Penelitian

**Penanggung jawab:** Aisyah Elfiyuni M.A
**Target:** 3 sampai 4 paragraf

**Yang harus diisi:**

1. Paragraf 1: kelompokkan enam artikel menjadi tiga kelompok penelitian, yaitu sistem rekomendasi, ekstraksi atau estimasi komposisi aroma, serta analisis perilaku konsumen dan popularitas.
2. Paragraf 2: nyatakan posisi project ini, yaitu memprediksi satu atribut sensorik pada tingkat produk jadi menggunakan regresi tabular.
3. Paragraf 3: nyatakan perbedaan pada perlakuan konsentrasi, karena artikel yang dirujuk tidak memasukkannya sebagai variabel penjelas.
4. Paragraf 4: rumuskan kebaruan dalam tiga poin, yaitu target *longevity* sebagai regresi pada tingkat produk jadi, penggunaan gabungan *notes* dan *accords*, serta pengujian pengaruh konsentrasi hasil ekstraksi teks.

**Jangan:** mengklaim "belum pernah ada penelitian" tanpa dasar. Gunakan rumusan "sejauh penelusuran yang dilakukan" atau "belum ditemukan penelitian yang".

<<<PART2>>>END
