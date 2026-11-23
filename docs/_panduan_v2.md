# PANDUAN PENYUSUNAN PROPOSAL
## Pembagian Tugas Penyusunan Proposal Project Akhir Prediksi Longevity Parfum
### Mata Kuliah Pembelajaran Mesin (TEK1314) - Kelas A

| Anggota | NIM | Bagian |
|---|---|---|
| Fattih Algie Maulana | J0404241002 | BAB III Metodologi (sudah jadi) |
| Aisyah Elfiyuni M.A | J0404241067 | BAB II Tinjauan Pustaka |
| Anggi Permana Putra | J0404241154 | BAB I Pendahuluan + Daftar Pustaka |

Aturan umum: bahasa Indonesia baku, tiap paragraf 4-8 kalimat, klaim wajib ada sitasi, istilah asing dicetak italic, desimal pakai koma (0,903 bukan 0.903). Jangan copy-paste kalimat jurnal, parafrase.

<<<PB>>>

## BAB I PENDAHULUAN

### 1.1 Latar Belakang

**Anggi** - 5 sampai 6 paragraf

Jelasin dari sejarah parfum dulu, terus geser ke masalah beli parfum online, pentingnya longevity, dasar kimianya, konsentrasi, terakhir kenapa perlu machine learning.

Alurnya: parfum dari zaman dulu sampai jadi industri besar, orang beli parfum pindah ke online, tapi online gak bisa cium bau, jadi cuma bisa percaya deskripsi penjual, padahal longevity yang paling bikin kecewa, longevity itu ditentuin komposisi bahan, apalagi konsentrasi, nah data Fragrantica bisa dipakai buat modelin itu.

Wajib ada minimal 3 sitasi dari 6 jurnal di Daftar Pustaka. Jangan bahas dataset detail, itu di BAB III.

### 1.2 Rumusan Masalah

**Anggi** - 1 pertanyaan utama + 4 sampai 5 rinci

Rumusan masalah utama: gimana cara prediksi longevity parfum dari komposisi notes, accords, dan konsentrasinya, biar orang bisa tau daya tahan sebelum beli.

Terus pecah jadi pertanyaan rinci: karakteristik datasetnya gimana, bahan apa yang paling ngaruh, konsentrasi ngaruh seberapa besar, algoritma mana yang paling bagus, apa yang bikin model terbatas.

Semua harus bentuk kalimat tanya. Jumlah pertanyaan rinci harus sama dengan jumlah poin di 1.3.

### 1.3 Tujuan

**Anggi** - 5 sampai 6 poin

Jawab tiap pertanyaan rinci di 1.2, satu poin satu jawaban, urutannya sejajar.

Mulai tiap poin pakai kata kerja: menganalisis, mengidentifikasi, menguji, membangun, membandingkan, mengimplementasikan.

Jangan pakai kata "mengetahui", terlalu umum.

### 1.4 Manfaat

**Anggi** - 1 paragraf + 3 poin

Teoretis: bedanya project ini sama penelitian lama. Yang lama neliti di level molekul atau lewat teks ulasan, kita di level produk jadi pakai komposisi bahan.

Praktis: buat konsumen (bantu sebelum beli), buat pelaku usaha (bahan mana yang paling ngaruh), buat mahasiswa (latihan alur ML lengkap).

### 1.5 Batasan Masalah

**Anggi** - 5 poin

Wajib jujur soal ini: longevity di data itu cuma persepsi orang, bukan hasil ukur lab. Cuma pakai 1 sumber data. Konsentrasi cuma kebaca 34,4% jadi diakui terbatas. Model cuma regresi tabular, gak pakai molekul atau GNN. Aplikasinya cuma lokal, bukan produksi.

Jangan nulis batasan kayak "keterbatasan waktu".

## BAB II TINJAUAN PUSTAKA

### 2.1 Landasan Teori

**Aisyah**

Ini bukan ringkasan jurnal. Fungsinya jelasin konsep yang dipakai di BAB III, jadi tiap istilah yang muncul di BAB III harus ada penjelasannya di sini. Urutannya dari domain parfum dulu, baru masuk ML. Tiap subbab minimal kutip 1 sumber.

#### 2.1.1 Parfum dan Longevity

**Aisyah** - 2 paragraf

Jelasin parfum itu campuran apa aja, terus piramida aroma 3 lapis (top, middle, base), kenapa base notes paling lama bertahan (berat molekul dan titik didih), longevity diukur gimana di Fragrantica (5 tingkat penilaian user, dirata-rata), terus kenapa hasilnya cuma persepsi, bukan ukuran lab.

#### 2.1.2 Fragrance Notes dan Accords

**Aisyah** - 2 paragraf

Beda notes sama accords. Notes itu bahan satuan, contoh formatnya Sandalwood:24|Amber:13, angkanya 0-100 nunjukin seberapa menonjol. Accords itu kesan aroma keseluruhan, kayak woody, sweet, powdery.

Terus jelasin notes lebih detail tapi jarang, accords lebih ringkas tapi padat, makanya dua-duanya dipakai.

#### 2.1.3 Tingkat Konsentrasi

**Aisyah** - 1 paragraf + 1 tabel

Konsentrasi itu kadar minyak wangi dalam larutan, makin tinggi makin lama nempel. Bikin tabel Extrait, EDP, EDT, EDC lengkap sama kadar minyak dan perkiraan daya tahan. Cari angkanya dari sumber, jangan ngarang.

Sisipin satu kalimat: konsentrasi tinggi gak selalu lebih bagus, bisa kepekatan.

#### 2.1.4 Regresi dalam Machine Learning

**Aisyah** - 2 paragraf

Beda regresi sama klasifikasi. Regresi keluarannya angka kontinu, klasifikasi keluarannya kelas.

Kenapa longevity dianggap kontinu: skalanya 1-5 dan berjarak, kalau dianggap kelas nanti jarak antar nilai ilang. Kasih contoh: selisih 3,1 ke 3,2 gak sama artinya sama selisih 3,1 ke 4,8.

#### 2.1.5 Ridge Regression

**Aisyah** - 3 paragraf

Ridge itu regresi linear yang dikasih penalti L2, tujuannya biar koefisien gak membengkak.

Hubungin ke multikolinearitas: kalau fitur banyak dan saling berkorelasi, regresi linear biasa bisa kacau, koefisiennya jadi besar-besar tanda berlawanan.

Wajib masukin angka dari project ini: regresi linear biasa R² negatif 1,893, sedangkan Ridge negatif 0,394. Itu alasan kenapa Ridge dipakai.

Jangan tulis rumus doang tanpa dijelasin artinya.

#### 2.1.6 Random Forest Regression

**Aisyah** - 3 paragraf

Random Forest itu kumpulan pohon keputusan, tiap pohon dilatih dari sampel acak (bagging), tiap cabang cuma liat sebagian fitur.

Kelebihannya bisa nangkep hubungan non-linear tanpa asumsi bentuk fungsi. Kelemahannya gampang overfitting kalau pohonnya dibiarin dalem, tandanya selisih R² latih sama uji jauh. Di project ini R² latih 0,912 tapi uji cuma 0,382.

#### 2.1.7 Gradient Boosting Regression

**Aisyah** - 3 paragraf

Gradient Boosting dibangun berurutan, model berikutnya belajar dari sisa error model sebelumnya. Learning rate nentuin seberapa besar tiap model baru nyumbang.

Bandingin sama Random Forest: RF paralel, GB berurutan. GB biasanya lebih stabil di data tabular ukuran sedang.

#### 2.1.8 Metrik Evaluasi

**Aisyah** - 4 sampai 5 paragraf

Masing-masing MAE, MSE, RMSE, R² satu paragraf. Jelasin cara hitungnya secara konsep dan cara bacanya di skala 1-5.

Wajib jelasin arti R² = 0 dan R² negatif, soalnya di project ini muncul nilai negatif.

### 2.2 Studi Literatur

**Aisyah**

6 artikelnya udah ditentuin, tugas lu cuma baca dan rangkum, gak perlu nyari lagi.

#### 2.2.1 Ringkasan Artikel Jurnal

**Aisyah** - 6 paragraf, 90-130 kata per paragraf

Pola tiap paragraf: tujuan penelitian, dataset yang dipakai, metode, hasil (wajib ada angka), relevansi sama project kita.

Daftar artikelnya:

| No | Penulis dan Tahun | Terbitan | Tautan |
|---|---|---|---|
| 1 | Nurmuthia, Imtiyaza, dan Sagala (2025) | Procedia Computer Science | https://doi.org/10.1016/j.procs.2025.09.051 |
| 2 | Kim, Oh, dan Oh (2024) | Applied Sciences | https://doi.org/10.3390/app14209293 |
| 3 | Fichtelmann dan Westermayr (2026) | RSC Advances | https://pubmed.ncbi.nlm.nih.gov/42158754/ |
| 4 | Rodrigues dkk. (2024) | Computers and Chemical Engineering | https://doi.org/10.1016/j.compchemeng.2024.108674 |
| 5 | Nikolic dan Marjanovic (2025) | SINTEZA 2025 | https://doi.org/10.15308/Sinteza-2025-213-220 |
| 6 | Nikolic, Marjanovic, dan Radenovic (2024) | Proceedings AATPS Nis | prosiding, gak ada DOI |

Jangan nulis "penelitian ini berhasil membuktikan metodenya bagus" tanpa angka.

#### 2.2.2 Tabel Studi Literatur

**Aisyah** - 1 tabel, 6 baris, 8 kolom

Kolomnya urut: No, Penulis dan Tahun, Permasalahan, Dataset, Metode atau Algoritma, Metrik Evaluasi, Hasil Utama, Perbedaan dengan Project.

Kolom "Perbedaan dengan Project" gak boleh kosong atau diisi "tidak ada". Isi yang konkret, misal beda target, beda jenis keluaran, atau beda algoritma.

#### 2.2.3 Relevansi Artikel terhadap Project

**Aisyah** - 1 tabel

Tabel 2 kolom: kebutuhan project sama artikel pendukungnya. Minimal ada penentuan masalah, pemilihan dataset, praproses, pemilihan algoritma, evaluasi, dan interpretasi fitur.

### 2.3 Posisi Penelitian

**Aisyah** - 3 sampai 4 paragraf

Kelompokin 6 artikel jadi 3 kelompok (sistem rekomendasi, ekstraksi komposisi aroma, analisis perilaku konsumen).

Terus tentuin posisi kita di mana: prediksi atribut sensorik di level produk jadi pakai regresi tabular.

Sebutin bedanya soal konsentrasi, karena artikel yang dirujuk gak masukin itu.

Terakhir rumusin 3 kebaruan: target longevity sebagai regresi, gabungan notes + accords, pengujian konsentrasi hasil ekstraksi teks.

Jangan nulis "belum pernah ada penelitian", pakai "sejauh penelusuran yang dilakukan".

<<<PART2>>>END
