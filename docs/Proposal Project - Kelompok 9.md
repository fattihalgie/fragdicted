# PENGAJUAN TEMA PROJECT AKHIR
## Prediksi Tingkat Ketahanan (Longevity) Parfum Berdasarkan Komposisi Fragrance Notes, Accords, dan Tingkat Konsentrasi Menggunakan Perbandingan Ridge Regression, Random Forest, dan Gradient Boosting
### Mata Kuliah Pembelajaran Mesin (TEK1314) - Kelas A

| No | Nama Anggota | NIM | Kontribusi Utama |
|---|---|---|---|
| 1 | Fattih Algie Maulana | J0404241002 | Dataset, EDA, preprocessing |
| 2 | Aisyah Elfiyuni M.A | J0404241067 | Modeling, evaluasi, analisis |
| 3 | Anggi Permana Putra | J0404241154 | Aplikasi, dokumentasi, demo |

**Tanggal pengajuan:** 26 Oktober 2026

<<<PB>>>

## BAB I PENDAHULUAN

### 1.1 Latar Belakang

Industri parfum global bernilai lebih dari USD 50 miliar dan terus tumbuh setiap tahun. Perkembangan perdagangan elektronik mengubah cara konsumen membeli parfum: transaksi yang dahulu menuntut kehadiran fisik di gerai kini dapat dilakukan sepenuhnya secara daring. Perubahan ini membawa satu persoalan mendasar yang belum terselesaikan, yaitu pembeli tidak dapat mencium aroma produk sebelum memutuskan pembelian. Satu-satunya informasi yang tersedia adalah deskripsi tertulis dari penjual, dan deskripsi tersebut bersifat subjektif serta berkecenderungan menampilkan produk secara positif.

Di antara berbagai parameter yang dinilai konsumen, longevity atau tingkat ketahanan aroma menempati posisi yang sangat penting. Longevity menyatakan seberapa lama aroma parfum bertahan pada kulit setelah disemprotkan. Kekecewaan konsumen terhadap produk parfum lebih sering disebabkan oleh aroma yang hilang terlalu cepat daripada oleh ketidaksukaan terhadap wanginya. Pada komunitas penggemar parfum, longevity secara konsisten menjadi salah satu dari tiga faktor utama dalam keputusan pembelian ulang, bersama proyeksi penyebaran aroma (sillage) dan penilaian terhadap harga.

Secara kimia, daya tahan aroma parfum ditentukan oleh komposisi bahan penyusunnya. Parfum tersusun mengikuti piramida tiga lapis, yaitu top notes, middle notes, dan base notes. Molekul dengan berat molekul dan titik didih tinggi seperti musk, amber, patchouli, dan sandalwood menguap jauh lebih lambat dibandingkan molekul ringan seperti sitrus dan aroma akuatik. Perbedaan laju penguapan inilah yang menentukan seberapa lama aroma tetap terdeteksi. Dengan demikian, secara teoritis longevity dapat diprediksi dari komposisi bahan penyusun parfum.

Selain komposisi bahan, tingkat konsentrasi merupakan penentu utama daya tahan aroma. Konsentrasi menyatakan persentase minyak wangi di dalam larutan pembawa. Parfum jenis extrait mengandung sekitar 20 hingga 40 persen minyak wangi, eau de parfum sekitar 15 hingga 20 persen, eau de toilette sekitar 5 hingga 15 persen, dan eau de cologne sekitar 2 hingga 4 persen. Semakin tinggi konsentrasi minyak, semakin lambat aroma menguap. Namun pada sebagian besar katalog produk daring, termasuk pada dataset yang digunakan dalam project ini, tingkat konsentrasi tidak dicantumkan sebagai atribut tersendiri.

Komunitas penggemar parfum pada platform Fragrantica telah menghasilkan data penilaian berskala besar yang dapat dimanfaatkan. Setiap parfum memperoleh penilaian longevity dari ribuan pengguna, dan setiap parfum memiliki daftar komposisi bahan yang terstruktur. Kombinasi keduanya memungkinkan pembangunan model yang mempelajari hubungan antara komposisi bahan dan persepsi ketahanan aroma. Pendekatan ini mengubah data penilaian komunitas yang semula hanya bersifat informatif menjadi dasar prediksi yang dapat diukur.

Machine learning menawarkan kerangka yang sesuai untuk persoalan tersebut. Dengan memperlakukan longevity sebagai variabel kontinu, permasalahan ini termasuk dalam kategori regresi. Model regresi dapat mempelajari pola hubungan antara ratusan jenis bahan penyusun dan skor longevity yang diberikan komunitas, kemudian menggunakan pola tersebut untuk memprediksi parfum yang belum pernah dinilai. Project ini membandingkan tiga algoritma regresi, yaitu Ridge Regression, Random Forest Regression, dan Gradient Boosting Regression, untuk menentukan pendekatan yang paling sesuai dengan karakteristik data.

### 1.2 Rumusan Masalah

**Rumusan masalah utama:**

Bagaimana memprediksi tingkat ketahanan (longevity) sebuah parfum berdasarkan komposisi fragrance notes, accords, dan tingkat konsentrasinya, sehingga konsumen dapat memperkirakan daya tahan parfum sebelum melakukan pembelian?

**Rincian rumusan masalah:**

1. Bagaimana karakteristik dataset penilaian parfum komunitas Fragrantica, khususnya distribusi target, nilai hilang, dan pencilan yang perlu ditangani sebelum pemodelan?
2. Bahan atau kelompok bahan manakah yang paling berpengaruh terhadap persepsi longevity parfum?
3. Sejauh mana tingkat konsentrasi parfum dapat diidentifikasi dari data yang tersedia, dan seberapa besar pengaruhnya terhadap longevity?
4. Algoritma regresi manakah di antara Ridge Regression, Random Forest Regression, dan Gradient Boosting Regression yang memberikan performa terbaik pada permasalahan ini?
5. Faktor apa saja yang membatasi kemampuan model dalam memprediksi longevity, dan bagaimana keterbatasan tersebut dijelaskan secara terukur?

### 1.3 Tujuan Project

1. Menganalisis karakteristik dataset penilaian parfum, mencakup distribusi target, nilai hilang, data duplikat, pencilan, serta korelasi antarvariabel.
2. Mengidentifikasi komposisi bahan yang paling berpengaruh terhadap longevity melalui analisis kepentingan fitur.
3. Menguji pengaruh tingkat konsentrasi terhadap longevity, termasuk mengukur cakupan identifikasi konsentrasi dari data yang tersedia.
4. Membangun dan membandingkan performa tiga algoritma regresi, yaitu Ridge Regression, Random Forest Regression, dan Gradient Boosting Regression, menggunakan metrik MAE, MSE, RMSE, dan R².
5. Menganalisis penyebab perbedaan performa antar model, termasuk indikasi overfitting, kesalahan prediksi, dan keterbatasan model.
6. Mengimplementasikan model terbaik ke dalam aplikasi web sederhana yang menerima input komposisi bahan dan menampilkan hasil prediksi longevity beserta interpretasinya.

### 1.4 Manfaat Project

**Manfaat teoretis:**

Project ini memberikan kontribusi pada kajian pemodelan atribut sensorik produk menggunakan machine learning. Sebagian besar penelitian terdahulu memodelkan atribut sensorik parfum pada tingkat molekul atau melalui analisis teks ulasan. Project ini menempuh jalur yang berbeda dengan memodelkan atribut sensorik pada tingkat produk jadi menggunakan representasi komposisi bahan yang terstruktur, sehingga memperluas khazanah pendekatan yang telah ada.

**Manfaat praktis:**

1. Bagi konsumen, model yang dihasilkan dapat digunakan sebagai alat bantu estimasi daya tahan parfum sebelum membeli, terutama pada transaksi daring yang tidak memungkinkan pengujian langsung.
2. Bagi pelaku usaha parfum, analisis kepentingan fitur memberikan gambaran mengenai bahan mana yang paling berkontribusi terhadap persepsi ketahanan aroma, sehingga dapat menjadi pertimbangan dalam penyusunan komposisi produk.
3. Bagi mahasiswa, project ini menjadi sarana penerapan menyeluruh tahapan machine learning, mulai dari eksplorasi data hingga implementasi aplikasi.

### 1.5 Batasan Masalah

1. Data yang digunakan merupakan hasil penilaian komunitas pada platform Fragrantica, bukan hasil pengukuran laboratorium. Nilai longevity yang diprediksi mencerminkan persepsi pengguna, bukan durasi penguapan yang terukur secara instrumental.
2. Project ini hanya menggunakan satu sumber data, yaitu dataset Fragrantica Perfumes dari Kaggle. Data dari platform lain tidak digabungkan karena perbedaan skala penilaian dan perbedaan penamaan bahan antarplatform.
3. Tingkat konsentrasi tidak tersedia sebagai atribut eksplisit pada dataset, sehingga nilainya diekstraksi dari nama produk dan deskripsi. Cakupan ekstraksi terbatas pada 34,4 persen baris, dan keterbatasan ini diperlakukan sebagai bagian dari analisis, bukan diasumsikan dapat diabaikan.
4. Model yang dibangun merupakan model tabular dengan algoritma regresi klasik. Pendekatan berbasis struktur molekul, jaringan saraf graf, maupun model bahasa besar tidak termasuk dalam lingkup project ini.
5. Aplikasi yang dikembangkan berupa aplikasi web sederhana yang menjalankan model secara lokal, bukan layanan produksi berskala besar.

## BAB II TINJAUAN PUSTAKA

### 2.1 Landasan Teori

#### 2.1.1 Parfum dan Longevity

Parfum merupakan campuran minyak esensial, senyawa aroma sintetis, dan pelarut yang dirancang untuk menghasilkan wangi tertentu. Campuran tersebut disusun mengikuti piramida aroma tiga lapis yang mencerminkan perbedaan laju penguapan masing-masing komponen. Lapisan pertama adalah top notes, yaitu senyawa dengan berat molekul rendah dan tekanan uap tinggi yang terdeteksi dalam beberapa menit pertama setelah penyemprotan dan umumnya bertahan kurang dari satu jam. Lapisan kedua adalah middle notes atau heart notes yang muncul setelah top notes memudar dan bertahan beberapa jam. Lapisan ketiga adalah base notes, yaitu senyawa berbobot molekul tinggi dengan titik didih tinggi yang menguap paling lambat dan menjadi penentu utama daya tahan aroma.

Longevity didefinisikan sebagai rentang waktu sejak parfum disemprotkan hingga aromanya tidak lagi terdeteksi secara jelas. Pada platform Fragrantica, longevity bukan diukur secara instrumental, melainkan dinilai melalui pemungutan suara pengguna dalam lima tingkat, yaitu Very Weak, Weak, Moderate, Long Lasting, dan Eternal. Nilai longevity yang tercatat pada dataset merupakan rata-rata dari seluruh suara yang masuk. Karena bersifat persepsi, nilai ini dipengaruhi pula oleh faktor di luar komposisi produk, seperti kimia kulit pemakai, suhu dan kelembapan lingkungan, serta cara penyimpanan parfum.

#### 2.1.2 Fragrance Notes dan Accords

Fragrance notes adalah daftar bahan aroma penyusun parfum, dikelompokkan menurut lapisan piramida aroma. Pada dataset Fragrantica, notes disimpan sebagai teks terstruktur yang memuat nama bahan beserta bobotnya, misalnya bentuk Sandalwood:24|Amber:13|Vanilla:12. Angka pada setiap pasangan menunjukkan seberapa menonjol bahan tersebut menurut pemungutan suara anggota komunitas, dengan skala 0 hingga 100.

Accords adalah representasi yang lebih ringkas dan lebih abstrak. Accord menyatakan kesan aroma secara keseluruhan, misalnya woody, sweet, powdery, floral, atau aromatic, bukan bahan tunggal penyusunnya. Satu parfum umumnya memiliki beberapa accord dengan bobot berbeda. Karena jumlah jenis accord jauh lebih sedikit dibandingkan jumlah jenis notes, representasi accord menghasilkan vektor fitur yang lebih padat dan lebih tahan terhadap masalah kelangkaan fitur.

Kedua representasi memiliki karakter yang saling melengkapi. Notes memberikan informasi granular mengenai bahan penyusun, sedangkan accords merangkum kesan aroma yang dirasakan pengguna. Project ini menggunakan keduanya sebagai fitur dan membandingkan kontribusi masing-masing.

#### 2.1.3 Tingkat Konsentrasi

Tingkat konsentrasi menyatakan persentase minyak wangi di dalam larutan. Perbedaan konsentrasi berimplikasi langsung pada daya tahan aroma karena jumlah molekul aroma yang tersedia untuk menguap berbeda. Tingkatan yang umum dikenal adalah sebagai berikut.

| Tingkatan | Nama Lengkap | Perkiraan Kadar Minyak | Perkiraan Daya Tahan |
|---|---|---|---|
| Extrait | Extrait de Parfum | 20-40 persen | 8 jam atau lebih |
| EDP | Eau de Parfum | 15-20 persen | 6-8 jam |
| EDT | Eau de Toilette | 5-15 persen | 4-6 jam |
| EDC | Eau de Cologne | 2-4 persen | 2-4 jam |
| EDF | Eau de Fraiche | 1-3 persen | kurang dari 2 jam |

Konsentrasi yang lebih tinggi tidak selalu berarti kualitas yang lebih baik, karena tingginya kadar minyak dapat membuat aroma terasa terlalu pekat pada sebagian pemakai. Namun untuk tujuan prediksi longevity, konsentrasi merupakan variabel penjelas yang penting dan seharusnya disertakan apabila tersedia.

#### 2.1.4 Regresi dalam Machine Learning

Regresi adalah cabang supervised learning yang bertujuan mempelajari pemetaan dari sekumpulan fitur masukan menuju satu atau beberapa variabel target kontinu. Berbeda dengan klasifikasi yang menghasilkan label diskret, regresi menghasilkan nilai numerik pada rentang tertentu. Pemilihan regresi sebagai pendekatan pada project ini didasarkan pada sifat target, yaitu longevity_avg yang berupa bilangan riil pada skala 1 hingga 5, bukan kategori terpisah.

Apabila target diperlakukan sebagai kelas diskret, informasi mengenai jarak antarnilai akan hilang. Perbedaan antara skor 3,1 dan 3,2 akan diperlakukan sama besarnya dengan perbedaan antara skor 3,1 dan 4,8. Perlakuan regresi mempertahankan informasi bertingkat tersebut, sehingga lebih sesuai dengan sifat data.

Tahapan umum dalam pembangunan model regresi mencakup eksplorasi data, praproses, pembagian data latih dan data uji, pelatihan model, evaluasi menggunakan metrik regresi, serta interpretasi hasil.

#### 2.1.5 Ridge Regression

Ridge Regression merupakan perluasan dari regresi linear yang menambahkan penalti berupa kuadrat dari besar koefisien ke dalam fungsi objektif. Penalti ini dikenal sebagai regularisasi L2. Tujuannya adalah membatasi besarnya koefisien agar model tidak terlalu sensitif terhadap perubahan kecil pada data masukan.

Regularisasi menjadi penting ketika jumlah fitur besar dan antarfitur terdapat korelasi tinggi, kondisi yang disebut multikolinearitas. Pada kondisi tersebut, regresi linear tanpa regularisasi dapat menghasilkan koefisien bernilai sangat besar dengan tanda berlawanan, sehingga model menjadi tidak stabil dan performanya pada data uji dapat memburuk hingga lebih buruk daripada sekadar memprediksi nilai rata-rata.

Pada project ini, kondisi tersebut benar-benar teramati. Ketika regresi linear tanpa regularisasi dilatih menggunakan 641 fitur base notes yang bersifat jarang, nilai R² yang diperoleh sebesar negatif 1,893. Setelah regularisasi L2 diterapkan melalui Ridge Regression, nilai R² meningkat menjadi negatif 0,394, atau sekitar lima kali lebih baik. Perbandingan ini menjadi dasar pemilihan Ridge Regression menggantikan regresi linear murni.

#### 2.1.6 Random Forest Regression

Random Forest Regression merupakan metode ensemble yang membangun banyak pohon keputusan regresi dan menggabungkan hasilnya melalui perata-rataan. Setiap pohon dilatih pada sampel data yang diambil secara acak dengan pengembalian (bootstrap aggregating atau bagging), dan pada setiap percabangan hanya sebagian fitur yang dipertimbangkan. Keragaman yang dihasilkan membuat gabungan pohon lebih stabil dibandingkan pohon tunggal.

Kelebihan utama metode ini adalah kemampuannya menangkap hubungan non-linear dan interaksi antarfitur tanpa memerlukan asumsi mengenai bentuk fungsi. Metode ini juga relatif tahan terhadap pencilan dan tidak menuntut normalisasi fitur, karena pemisahan dilakukan berdasarkan ambang nilai per fitur, bukan berdasarkan jarak.

Keterbatasan utamanya adalah kecenderungan overfitting apabila pohon dibiarkan tumbuh sangat dalam, khususnya pada dataset berukuran kecil hingga sedang. Overfitting tersebut terlihat dari selisih besar antara performa pada data latih dan data uji.

#### 2.1.7 Gradient Boosting Regression

Gradient Boosting Regression juga merupakan metode ensemble berbasis pohon keputusan, namun dibangun secara berurutan, bukan paralel. Model pertama dilatih untuk memprediksi target, kemudian model berikutnya dilatih untuk memprediksi sisa kesalahan (residual) dari model sebelumnya. Setiap model baru berkontribusi memperbaiki kesalahan yang belum tertangani, dan kontribusinya diperkecil melalui parameter learning rate.

Pendekatan bertahap ini sering menghasilkan performa yang lebih baik pada data tabular berukuran sedang, karena model secara bertahap memusatkan perhatian pada bagian data yang masih sulit diprediksi. Metode ini juga umumnya lebih stabil terhadap overfitting dibandingkan Random Forest, dengan catatan hyperparameter seperti jumlah pohon, kedalaman, dan learning rate diatur secara tepat.

Keterbatasannya adalah waktu pelatihan yang lebih lama karena prosesnya berurutan, serta kepekaan terhadap pemilihan hyperparameter.

#### 2.1.8 Metrik Evaluasi

Evaluasi model regresi pada project ini menggunakan empat metrik sesuai ketentuan tugas.

MAE (Mean Absolute Error) dihitung sebagai rata-rata nilai absolut selisih antara nilai aktual dan nilai prediksi. Metrik ini menyatakan besar kesalahan rata-rata dalam satuan yang sama dengan target, sehingga mudah ditafsirkan. Pada skala longevity 1 hingga 5, nilai MAE sebesar 0,28 berarti prediksi meleset sekitar 0,28 poin dari nilai sebenarnya.

MSE (Mean Squared Error) dihitung sebagai rata-rata kuadrat selisih. Karena selisih dikuadratkan, metrik ini memberi penalti yang lebih besar pada kesalahan besar dibandingkan kesalahan kecil.

RMSE (Root Mean Squared Error) merupakan akar kuadrat dari MSE. Metrik ini mengembalikan satuan ke satuan target sehingga dapat ditafsirkan langsung, sekaligus mempertahankan sifat pemberian penalti terhadap kesalahan besar.

R² (koefisien determinasi) dihitung sebagai satu dikurangi rasio antara jumlah kuadrat residual dan jumlah kuadrat total. Nilai R² menyatakan proporsi variasi target yang dapat dijelaskan oleh model. Nilai 1 berarti model sempurna, nilai 0 berarti model tidak lebih baik daripada memprediksi nilai rata-rata, dan nilai negatif berarti model lebih buruk daripada memprediksi nilai rata-rata.

Selain keempat metrik tersebut, project ini menggunakan perbandingan antara R² pada data latih dan R² pada data uji untuk mengidentifikasi indikasi overfitting. Selisih yang besar antara keduanya menunjukkan bahwa model menghafal data latih alih-alih mempelajari pola yang dapat digeneralisasi.

### 2.2 Studi Literatur

Bagian ini merangkum enam artikel ilmiah yang menjadi rujukan project. Seluruh artikel telah ditelusuri dan diverifikasi keberadaannya beserta rincian bibliografinya.

#### 2.2.1 Ringkasan Artikel Jurnal

**Artikel 1 - Nurmuthia, Imtiyaza, dan Sagala (2025).** Penelitian ini membangun sistem rekomendasi parfum yang dipersonalisasi berdasarkan deskripsi kebutuhan pengguna. Dataset yang digunakan memuat 24.760 parfum dengan 11 fitur yang bersumber dari Fragrantica. Kemiripan antara deskripsi pengguna dan profil parfum dihitung menggunakan Cosine Similarity dan Jaccard Similarity. Penelitian ini menunjukkan bahwa data Fragrantica dapat diolah menjadi layanan yang membantu konsumen memilih parfum, dan menjadi rujukan utama project ini dalam hal pemanfaatan dataset Fragrantica berskala besar.

**Artikel 2 - Kim, Oh, dan Oh (2024).** Penelitian ini mengestimasi komposisi notes parfum berdasarkan kalimat deskriptif menggunakan Sentence Transformer yang di-fine-tuning. Dataset terdiri atas 62 parfum dengan 255 jenis notes. Hasilnya menunjukkan peningkatan hit rate@5 dari kisaran 37,1 sampai 41,1 persen menjadi 72,6 sampai 79,0 persen, serta peningkatan Mean Reciprocal Rank dari 22,1 sampai 31,9 persen menjadi 57,3 sampai 63,2 persen. Artikel ini menjadi rujukan dalam hal pemodelan hubungan antara teks dan komposisi notes.

**Artikel 3 - Fichtelmann dan Westermayr (2026).** Penelitian ini memprediksi kekuatan bau komponen parfum berdasarkan struktur molekul, menggunakan lebih dari 2.300 molekul dari penggabungan dua sumber publik. Pendekatan yang digunakan adalah pemodelan ordinal dengan optimasi hyperparameter, disertai analisis kepentingan fitur melalui SHAP. Artikel ini menjadi rujukan dalam hal perlakuan atribut sensorik sebagai variabel bertingkat serta penggunaan analisis kepentingan fitur.

**Artikel 4 - Rodrigues, Santana, Queiroz, Rebello, dan Nogueira (2024).** Penelitian ini merancang formulasi parfum baru berdasarkan umpan balik konsumen menggunakan Graph Neural Network dan clustering. Model mampu mengelompokkan parfum berdasarkan profil aroma dan mengusulkan formulasi baru. Artikel ini menjadi rujukan dalam hal pemanfaatan representasi komposisi aroma sebagai masukan model machine learning.

**Artikel 5 - Nikolic dan Marjanovic (2025).** Penelitian ini menghubungkan komposisi notes parfum dengan respons emosional konsumen menggunakan ulasan pengguna Fragrantica. Metode yang digunakan mencakup VADER, DistilBERT, clustering, dan visualisasi statistik. Ditemukan pola hubungan antara profil aroma tertentu dan kelompok emosi konsumen. Artikel ini menjadi rujukan dalam hal eksplorasi data ulasan serta hubungan antara komposisi bahan dan persepsi pengguna.

**Artikel 6 - Nikolic, Marjanovic, dan Radenovic (2024).** Penelitian ini memprediksi popularitas parfum berdasarkan komposisi notes dan perilaku konsumen menggunakan algoritma machine learning. Hasilnya menunjukkan bahwa komposisi notes memiliki daya prediksi terhadap tingkat popularitas parfum. Artikel ini menjadi rujukan terdekat secara metodologis, karena sama-sama memprediksi atribut parfum dari komposisi notes menggunakan algoritma machine learning.

#### 2.2.2 Tabel Studi Literatur

| No | Penulis dan Tahun | Permasalahan | Dataset | Metode / Algoritma | Metrik Evaluasi | Hasil Utama | Perbedaan dengan Project |
|---|---|---|---|---|---|---|---|
| 1 | Nurmuthia, Imtiyaza dan Sagala (2025) | Memberikan rekomendasi parfum yang dipersonalisasi berdasarkan deskripsi kebutuhan pengguna | 24.760 parfum dengan 11 fitur dari Fragrantica | Cosine Similarity dan Jaccard Similarity | Tingkat relevansi hasil rekomendasi | Sistem mampu mencocokkan deskripsi pengguna dengan parfum yang sesuai | Project ini tidak melakukan rekomendasi, melainkan membangun model regresi untuk memprediksi nilai longevity secara numerik |
| 2 | Kim, Oh dan Oh (2024) | Mengestimasi komposisi notes parfum dari kalimat deskriptif | 62 parfum dengan 255 jenis notes | Sentence Transformer dengan fine-tuning | Hit rate@5 dan Mean Reciprocal Rank | Hit rate@5 naik dari 37,1-41,1 persen menjadi 72,6-79,0 persen | Project ini memakai notes yang sudah terstruktur sebagai input, bukan mengekstraksi notes dari teks bebas, dan outputnya berupa nilai kontinu |
| 3 | Fichtelmann dan Westermayr (2026) | Memprediksi kekuatan bau komponen parfum berdasarkan struktur molekul | Lebih dari 2.300 molekul dari dua sumber publik | Pemodelan ordinal dengan optimasi hyperparameter dan analisis SHAP | Metrik evaluasi ordinal dan kepentingan fitur | Model mampu memprediksi kekuatan bau secara ordinal, SHAP mengidentifikasi penentu fisikokimia utama | Project ini bekerja pada tingkat produk jadi dengan representasi komposisi notes, bukan pada tingkat struktur molekul individual |
| 4 | Rodrigues, Santana, Queiroz, Rebello dan Nogueira (2024) | Merancang formulasi parfum baru berdasarkan umpan balik konsumen | Data parfum komersial dan umpan balik konsumen | Graph Neural Network dan clustering | Metrik kualitas klaster dan evaluasi formulasi | GNN mampu mengelompokkan parfum berdasarkan profil aroma dan mengusulkan formulasi baru | Project ini memakai algoritma regresi tabular klasik, bukan graph neural network, dan bertujuan memprediksi longevity bukan merancang formula |
| 5 | Nikolic dan Marjanovic (2025) | Menghubungkan komposisi notes parfum dengan respons emosional konsumen | Ulasan pengguna platform Fragrantica | VADER, DistilBERT, clustering, visualisasi statistik | Akurasi klasifikasi sentimen dan analisis korelasi | Ditemukan pola hubungan antara profil aroma dan kelompok emosi konsumen | Project ini memprediksi parameter sensorik berupa longevity yang bersifat numerik, bukan mengklasifikasikan emosi dari teks ulasan |
| 6 | Nikolic, Marjanovic dan Radenovic (2024) | Memprediksi popularitas parfum berdasarkan komposisi notes dan perilaku konsumen | Data parfum dan perilaku konsumen | Algoritma machine learning untuk prediksi | Metrik evaluasi prediksi | Komposisi notes terbukti memiliki daya prediksi terhadap popularitas parfum | Project ini memprediksi atribut sensorik berupa longevity, bukan metrik popularitas, dan membandingkan tiga algoritma regresi secara eksplisit |

#### 2.2.3 Relevansi Artikel terhadap Project

| Kebutuhan project | Artikel pendukung |
|---|---|
| Penentuan permasalahan penelitian | Artikel 1, 5, 6 |
| Pemilihan dataset dan variabel | Artikel 1, 5, 6 |
| Metode praproses data | Artikel 2, 3 |
| Pemilihan algoritma machine learning | Artikel 3, 4, 6 |
| Metode evaluasi model | Artikel 3, 4 |
| Interpretasi kepentingan fitur | Artikel 3, 6 |

### 2.3 Posisi Penelitian

Berdasarkan keenam artikel tersebut, dapat diidentifikasi tiga kelompok besar penelitian yang telah dilakukan pada domain parfum. Kelompok pertama berfokus pada sistem rekomendasi dan pencocokan preferensi konsumen (Artikel 1). Kelompok kedua berfokus pada ekstraksi atau estimasi komposisi aroma, baik dari teks (Artikel 2) maupun dari struktur molekul (Artikel 3). Kelompok ketiga berfokus pada analisis perilaku konsumen dan popularitas produk (Artikel 5 dan 6).

Project ini mengambil posisi yang berbeda dari ketiganya. Alih-alih merekomendasikan produk atau mengekstraksi komposisi, project ini memprediksi satu atribut sensorik tertentu, yaitu longevity, pada tingkat produk jadi. Pendekatan yang ditempuh adalah regresi tabular menggunakan representasi komposisi bahan yang telah terstruktur.

Perbedaan lain terletak pada perlakuan terhadap tingkat konsentrasi. Sejauh penelusuran yang dilakukan, artikel yang dirujuk tidak memasukkan konsentrasi sebagai variabel penjelas, meskipun secara teori variabel tersebut merupakan penentu utama daya tahan aroma. Project ini secara eksplisit menguji pengaruh konsentrasi, termasuk mengukur cakupan identifikasi konsentrasi dari data yang tersedia dan keterbatasan yang ditimbulkannya.

Dengan demikian, kebaruan project ini terletak pada tiga hal, yaitu pemodelan longevity sebagai target regresi pada tingkat produk jadi, penggunaan gabungan notes dan accords sebagai representasi komposisi, serta pengujian pengaruh tingkat konsentrasi yang diekstraksi dari teks produk.

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
| Fattih Algie Maulana | Dataset, eksplorasi data, praproses | Sumber data, alasan filter vote_count, penanganan nilai hilang, ekstraksi konsentrasi, pencegahan kebocoran data |
| Aisyah Elfiyuni M.A | Pemodelan, evaluasi, analisis | Konfigurasi ketiga algoritma, alasan pemilihan, interpretasi metrik, analisis overfitting dan kepentingan fitur |
| Anggi Permana Putra | Implementasi aplikasi, dokumentasi, demo | Arsitektur aplikasi, alur input hingga output, penyimpanan model, penyusunan presentasi dan video |

Seluruh anggota wajib memahami keseluruhan alur project, karena penilaian presentasi dan tanya jawab bersifat individual.
