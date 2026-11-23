# Naskah dan Materi Presentasi

**Bagian saya:** poin 3 (target/goal/tujuan) dan poin 4 (model yang dipilih dan alasannya)
**Durasi total:** sekitar 3 sampai 4 menit untuk dua slide

## Cara pakai file ini

Ada tiga bagian:

1. **Materi pemahaman.** Konsep yang harus lu ngerti, bukan hafal. Kalau penguji nanya di luar naskah, ini yang menyelamatkan lu.
2. **Naskah lisan.** Kalimat siap pakai per slide, dengan penanda waktu. Boleh dibaca, boleh diubah jadi bahasa sendiri.
3. **Tanya jawab.** Pertanyaan yang paling mungkin muncul, plus jawaban singkat.

Jangan hafalkan naskah kata per kata. Hafalkan **urutan** dan **angka**. Kalimat bisa mengalir sendiri.

---

# Bagian 1: Materi yang harus dipahami

## Apa yang sebenarnya diprediksi

Setiap parfum di dataset punya skor ketahanan yang dihitung dari rata-rata penilaian pengguna. Skornya 1 sampai 5, dengan makna:

| Skor | Arti |
|---|---|
| 1 | kurang dari 1 jam |
| 2 | 1 sampai 2 jam |
| 3 | 3 sampai 6 jam |
| 4 | 7 sampai 12 jam |
| 5 | lebih dari 12 jam |

Model kita menerima input komposisi parfum, lalu menebak skor itu sebelum parfumnya dipakai.

## Kenapa regresi, bukan klasifikasi

Bayangkan dua pilihan cara menilai. Cara pertama, model ditanya "ini tahan lama atau tidak", jawabannya cuma dua. Cara kedua, model ditanya "menurutmu skornya berapa", jawabannya angka.

Kita memilih cara kedua karena skornya memang berjenjang dan jaraknya bermakna. Skor 5 itu dua tingkat lebih tinggi dari skor 3, bukan sekadar "kelas berbeda". Kalau dipaksa jadi klasifikasi, informasi jarak itu hilang, dan model tidak bisa dihukum lebih berat saat salah jauh dibanding salah dekat.

Konsekuensi praktisnya: output model berupa angka desimal, misalnya 3,48. Bukan 4, bukan "long lasting".

## Apa itu fitur

Fitur adalah bahan masukan model. Di penelitian ini ada 181 fitur:

- 126 fitur fragrance notes, misalnya bergamot, patchouli, vanilla
- 54 fitur accords, misalnya citrus, woody, amber
- 1 fitur tingkat konsentrasi, nilainya 0 sampai 5 dari tidak diketahui sampai extrait

Nilai notes dan accords bukan gram atau persen. Itu bobot relatif 0 sampai 1 hasil pengolahan suara pengguna Fragrantica. Angka 1 berarti bahan itu paling menonjol di parfum tersebut. Sebutkan ini kalau ditanya, karena banyak yang salah kira itu persentase kandungan.

## Apa itu baseline dan kenapa perlu

Baseline adalah model paling bodoh yang mungkin: selalu menebak nilai rata-rata, tanpa melihat komposisi sama sekali.

Baseline ini wajib ada, karena tanpa dia kita tidak tahu apakah model pintar kita benar-benar pintar atau cuma kelihatan pintar. Baseline kita menghasilkan MAE 0,3699. Artinya, kalau asal tebak rata-rata, rata-rata meleset 0,37 poin.

Model kita paling bagus menghasilkan 0,2784. Jadi modelnya memang belajar sesuatu, bukan kebetulan.

## Apa itu MAE

MAE itu singkatan dari Mean Absolute Error, atau rata-rata kesalahan mutlak. Cara bacanya sederhana: berapa poin rata-rata tebakan kita meleset.

MAE 0,2784 di skala 1 sampai 5 berarti tebakan meleset sekitar 0,28 poin. Kalau parfum aslinya 3,5, tebakan kita biasanya ada di kisaran 3,2 sampai 3,8.

Kenapa MAE dipakai, bukan akurasi? Karena akurasi cuma cocok untuk klasifikasi. Kalau targetnya angka, akurasi tidak bisa dihitung.

## Apa itu R2

R2 mengukur seberapa besar variasi data yang berhasil dijelaskan model. Skalanya dari 0 sampai 1, makin tinggi makin baik.

R2 kita sekitar 0,38. Artinya, komposisi parfum menjelaskan sekitar 38 persen perbedaan ketahanan antar parfum. Sisanya 62 persen dijelaskan hal lain: kondisi kulit, cuaca, cara pemakaian, kualitas bahan baku, dan sebagainya.

Angka ini kelihatan kecil, tapi justru itu temuan penelitiannya. Kalau R2 nya 0,9, malah harus curiga, karena itu biasanya tanda kebocoran data.

## Apa itu overfitting

Overfitting itu kondisi ketika model terlalu hafal data latihan, sampai ikut menghafal kebetulan dan noise di dalamnya. Akibatnya, saat diberi data baru, performanya jatuh.

Cara mendeteksinya: bandingkan R2 di data latihan dengan R2 di data uji. Kalau selisihnya jauh, berarti overfitting.

Contoh nyata di penelitian kita:

| Model | R2 latih | R2 uji | Selisih |
|---|---|---|---|
| Ridge | 0,3653 | 0,3494 | 0,016 |
| Random Forest | 0,9118 | 0,3855 | 0,526 |
| Gradient Boosting | 0,4440 | 0,3783 | 0,066 |

Random Forest hafal data latihan sampai R2 0,91, tapi di data uji cuma 0,39. Itu contoh overfitting paling jelas.

## Apa itu regularisasi L2

Regresi linier biasa mencari garis yang paling pas. Masalahnya, kalau antar fitur saling berkorelasi, ada banyak garis berbeda yang sama-sama pas, dan model jadi bingung memilih. Koefisiennya bisa membengkak jadi angka aneh.

Regularisasi L2 menambahkan hukuman untuk koefisien yang terlalu besar. Jadi model dipaksa memilih koefisien yang wajar. Hasilnya lebih stabil dan lebih tahan kalau datanya berubah sedikit.

Analogi: kalau ada dua jalan sama-sama cepat, L2 membuat kita memilih jalan yang paling lurus, bukan jalan yang berbelit walau sama cepatnya.

## Apa bedanya Random Forest dan Gradient Boosting

Dua-duanya kumpulan pohon keputusan, tapi cara menyusunnya beda.

**Random Forest** membangun ratusan pohon secara bersamaan, masing-masing melihat sebagian data dan sebagian fitur, lalu hasilnya dirata-rata. Idenya: banyak pendapat independen kalau digabung jadi lebih baik.

**Gradient Boosting** membangun pohon satu per satu. Pohon pertama menebak, lalu dihitung sisa kesalahannya. Pohon kedua dibuat khusus untuk memperbaiki kesalahan itu, dan seterusnya. Idenya: belajar dari kesalahan sendiri, berulang.

Karena itu Random Forest cenderung cepat hafal data latihan, sementara Gradient Boosting lebih hati-hati dan lebih stabil di data baru. Ini sesuai dengan hasil kita: selisih latih-uji Random Forest 0,53, Gradient Boosting 0,066.

---

# Bagian 2: Naskah lisan

## Slide 04, Target yang ingin dicapai (sekitar 90 detik)

**Kalimat pembuka.**

"Masuk ke poin ketiga, yaitu target yang ingin dicapai."

**Bait 1, apa yang diprediksi.**

"Yang kami prediksi adalah skor ketahanan parfum, atau longevity. Skornya 1 sampai 5. Skor 1 berarti kurang dari satu jam, skor 3 berarti tiga sampai enam jam, dan skor 5 berarti lebih dari dua belas jam. Skala ini berasal dari penilaian pengguna Fragrantica, jadi bukan asumsi kami sendiri."

**Bait 2, jenis masalahnya.**

"Karena targetnya berupa angka yang berjenjang, penelitian ini kami kerjakan sebagai masalah regresi, bukan klasifikasi. Kalau dibuat klasifikasi, jarak antar level akan hilang, padahal jarak itu penting. Skor 5 itu dua tingkat di atas skor 3, dan itu perlu dipertahankan."

**Bait 3, tujuan khusus.**

"Ada tiga tujuan khusus. Pertama, membangun model regresi yang memetakan komposisi parfum ke skor ketahanan. Kedua, membandingkan tiga model memakai data latih, data uji, dan metrik yang sama, supaya perbandingannya adil. Ketiga, mengukur nilai tambah model dibanding tebakan rata-rata, sebagai patokan dasar."

**Kalimat penutup slide.**

"Jadi bukan hanya membuat model, tapi juga membuktikan bahwa modelnya memang lebih baik daripada sekadar menebak rata-rata."

**Yang harus diingat dari slide ini:** angka 1 sampai 5, kata regresi, dan tiga tujuan.

---

## Slide 05, Model yang dibandingkan (sekitar 2 menit)

**Kalimat pembuka.**

"Poin keempat, model yang kami bandingkan dan alasan pemilihannya. Ada tiga model, dan masing-masing punya peran berbeda."

**Bait 1, Ridge.**

"Yang pertama Ridge Regression. Ini model linier dengan regularisasi L2. Kami memilihnya karena di data kami banyak notes dan accord yang saling berkorelasi, misalnya bergamot dengan citrus, atau musk dengan white musk. Pada kondisi seperti itu, regresi linier biasa menghasilkan koefisien yang tidak stabil. Regularisasi L2 menekan koefisien tersebut supaya hasilnya wajar. Nilai penaltinya kami cari lewat validasi silang, bukan ditentukan manual. Perannya di sini sebagai pembanding linier."

**Bait 2, Random Forest.**

"Yang kedua Random Forest. Ini kumpulan ratusan pohon keputusan yang hasilnya dirata-rata. Dipilih karena mampu menangkap hubungan yang tidak lurus, misalnya patchouli yang pengaruhnya kuat hanya kalau muncul bersama amber. Hasilnya MAE 0,2784, paling rendah di antara ketiga model."

**Bait 3, jangan berhenti di angka bagus.**

"Tapi ada catatan penting. R2 di data latihnya 0,9118, sementara di data uji 0,3855. Selisihnya 0,53. Artinya model ini menghafal data latihan, dan itu berisiko saat menerima data baru."

**Bait 4, Gradient Boosting.**

"Yang ketiga Gradient Boosting. Pohonnya dibangun berurutan, setiap pohon memperbaiki kesalahan pohon sebelumnya. Hasilnya MAE 0,2821 dan R2 uji 0,3783. Sedikit di bawah Random Forest, tapi selisih R2 latih dan ujinya hanya 0,066. Artinya model ini jauh lebih stabil."

**Bait 5, keputusan.**

"Dari perbandingan ini, model yang kami pakai di aplikasi adalah Gradient Boosting. Bukan karena angkanya paling bagus, karena MAE Random Forest lebih rendah. Tapi karena kriterianya bukan sekadar nilai tertinggi. Kami memakai aturan: model harus punya selisih R2 latih dan uji di bawah 0,10, baru setelah itu dipilih MAE terkecil. Dari aturan itu, Gradient Boosting yang lolos dengan performa terbaik."

**Kalimat penutup slide.**

"Jadi yang kami pilih adalah model yang paling jujur, bukan model yang angkanya paling mengkilap di atas kertas."

**Yang harus diingat dari slide ini:** tiga model, satu pembanding linier dan dua berbasis pohon, lalu alasan Gradient Boosting dipilih.

---

## Kalau waktu lu dipotong

Kadang penguji memotong presentasi karena waktu habis. Kalau itu terjadi, sampaikan versi 30 detik ini:

"Target kami skor ketahanan parfum skala 1 sampai 5, dikerjakan sebagai regresi karena targetnya berjenjang. Kami membandingkan Ridge sebagai pembanding linier, Random Forest dan Gradient Boosting sebagai pembanding berbasis pohon. Hasilnya MAE turun dari 0,37 pada baseline menjadi 0,2784 pada Random Forest. Namun Random Forest mengalami overfitting dengan selisih R2 latih dan uji 0,53, jadi aplikasi memakai Gradient Boosting yang selisihnya hanya 0,066."

---

# Bagian 3: Angka yang wajib hafal

Ini saja. Kalau lupa angka lain, jawab "saya cek dulu", jangan mengarang.

| Angka | Artinya |
|---|---|
| 1 sampai 5 | skala target |
| 181 | jumlah fitur, 126 notes, 54 accords, 1 konsentrasi |
| 0,3699 | MAE baseline, tebakan rata-rata |
| 0,2784 | MAE Random Forest, paling rendah |
| 0,2821 | MAE Gradient Boosting, yang dipakai |
| 0,2896 | MAE Ridge |
| 0,9118 | R2 latih Random Forest, tanda overfitting |
| 0,066 | selisih R2 latih dan uji Gradient Boosting |
| 0,53 | selisih R2 latih dan uji Random Forest |

Nilai di bawah 0,4 itu skala poin, bukan persen. Jangan sampai salah sebut "MAE 28 persen".

---

# Bagian 4: Tanya jawab

**Kalau ditanya: kenapa regresi, kenapa bukan klasifikasi?**
Karena targetnya angka berjenjang dengan jarak yang bermakna. Kalau dijadikan kelas, informasi jarak hilang dan kita tidak bisa membedakan salah dekat dengan salah jauh. Untuk kasus ini, model yang salah menebak 3,4 padahal aslinya 3,5 harus dinilai lebih baik daripada yang menebak 5.

**Kalau ditanya: kenapa tiga model, bukan satu?**
Supaya peningkatan performa bisa dibuktikan berasal dari pemilihan model, bukan kebetulan. Ridge menjadi pembanding linier, dua model pohon menjadi pembanding non-linier. Kalau cuma satu model, tidak ada dasar untuk mengklaim model itu yang terbaik.

**Kalau ditanya: Random Forest MAE-nya paling kecil, kenapa bukan itu yang dipakai?**
Justru itu pertimbangannya. MAE kecil di data uji tidak otomatis berarti modelnya bagus, kalau di saat yang sama dia menghafal data latihan. Random Forest R2 latihnya 0,9118 dan R2 ujinya 0,3855. Selisih 0,53 itu terlalu besar. Gradient Boosting selisihnya 0,066. Untuk aplikasi yang akan menerima input dari pengguna, model yang stabil lebih penting daripada yang menang tipis di data uji.

**Kalau ditanya: kenapa tidak pakai deep learning?**
Karena datanya tabular dengan jumlah baris terbatas. Deep learning unggul pada data tidak terstruktur seperti gambar atau teks, dan butuh data jauh lebih banyak. Untuk data tabular seperti ini, tiga model yang kami pakai sudah mewakili pendekatan linier dan non-linier, dan lebih mudah dijelaskan.

**Kalau ditanya: kenapa tidak pakai XGBoost atau LightGBM?**
Kalau ditanya begini, jawab jujur: penelitian ini membatasi pada tiga model yang mewakili dua pendekatan, yaitu linier dan berbasis pohon. XGBoost adalah pengembangan Gradient Boosting dan bisa jadi lanjutan penelitian. Jangan bilang "lupa", jawab sebagai batasan cakupan.

**Kalau ditanya: apa arti R2 0,38, kok kecil?**
Artinya komposisi parfum menjelaskan sekitar 38 persen variasi ketahanan. Sisanya dipengaruhi faktor lain: kondisi kulit, cuaca, cara pemakaian, dan kualitas bahan baku. Angka ini wajar untuk data penilaian manusia. Kalau R2 mencapai 0,9 pada data seperti ini, malah perlu dicurigai ada kebocoran data.

**Kalau ditanya: kenapa tahun rilis dan gender tidak dipakai?**
Karena judul penelitian hanya menyebut notes, accords, dan tingkat konsentrasi, jadi fitur yang dipakai harus konsisten dengan judul. Selain itu kontribusinya kecil. Waktu diuji, membuang keduanya hanya menaikkan MAE dari 0,2770 ke 0,2821.

**Kalau ditanya: apakah model ini bisa dipakai untuk semua parfum?**
Tidak. Model dilatih pada parfum dengan komposisi yang tercatat, dan cara kerjanya bergantung pada notes dan accords yang tersedia. Parfum tanpa data komposisi tidak bisa diprediksi. Faktor kulit dan cuaca juga tidak masuk ke model.

**Kalau ditanya: apa tujuan praktisnya?**
Memberi perkiraan ketahanan sebelum membeli. Selama ini orang hanya tahu setelah memakai, dan ulasan yang ada bersifat subjektif.

**Kalau ditanya dan lu tidak tahu jawabannya.**
"Untuk itu saya belum punya datanya, saya cek dulu ya." Itu jauh lebih aman daripada mengarang. Mengarang satu angka bisa meruntuhkan seluruh presentasi.

---

# Bagian 5: Latihan 15 menit sebelum tampil

1. Baca tabel angka wajib hafal tiga kali. Tutup, lalu sebutkan dari ingatan.
2. Baca naskah slide 04 sekali dengan suara biasa, jangan dihafal.
3. Baca naskah slide 05 sekali. Pastikan kalimat "bukan karena angkanya paling bagus" keluar dengan lancar, karena itu inti pembelaan lu.
4. Latih versi 30 detik. Ini jaring pengaman kalau waktu dipotong.
5. Baca bagian tanya jawab sekali saja. Jangan dihafal, cukup tahu arah jawabannya.

Kalau ada satu hal yang paling menentukan, itu penjelasan kenapa Gradient Boosting dipakai walau Random Forest MAE-nya lebih rendah. Di situ lu kelihatan paham, bukan cuma melaporkan angka.
