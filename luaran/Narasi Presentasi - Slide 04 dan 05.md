# Narasi Presentasi

**Bagian saya:** poin 3 (target dan tujuan) dan poin 4 (model yang dibandingkan)
**Total durasi:** sekitar 3 menit 30 detik

---

## Pembuka

"Terima kasih. Saya lanjut ke poin ketiga dan keempat, yaitu target yang ingin dicapai dan model yang kami bandingkan."

---

## Slide 04: Target yang ingin dicapai

**Waktu: sekitar 90 detik**

"Target yang ingin kami capai adalah memprediksi skor ketahanan parfum, atau longevity. Skalanya 1 sampai 5, dan skala ini bukan asumsi kami, tapi berasal dari penilaian pengguna Fragrantica.

Skor 1 artinya very weak, tahan kurang dari satu jam. Skor 2 weak, satu sampai dua jam. Skor 3 moderate, tiga sampai enam jam. Skor 4 long lasting, tujuh sampai dua belas jam. Dan skor 5 eternal, lebih dari dua belas jam.

Yang membedakan penelitian kami dengan sistem rekomendasi parfum biasa: kami tidak memprediksi parfum mana yang cocok untuk seseorang. Kami memprediksi ketahanannya, hanya berdasarkan komposisi, yaitu fragrance notes, accords, dan tingkat konsentrasi.

Karena itu kami memakai model regresi, bukan klasifikasi. Alasannya, ketahanan ini pada dasarnya sudah punya skor bertingkat dari 1 sampai 5, dan skornya bisa 3,8. Kalau dipaksa menjadi klasifikasi, model hanya bisa menjawab dua kemungkinan, dan informasi jarak antar skor hilang. Padahal model yang salah menebak 3,4 ketika nilai aslinya 3,5 seharusnya dinilai lebih baik daripada yang menebak 5.

Tujuan khusus kami ada tiga. Pertama, membangun model regresi yang memetakan notes, accords, dan tingkat konsentrasi ke skor ketahanan. Kedua, membandingkan tiga model memakai data latih, data uji, dan metrik yang sama, supaya perbandingannya adil. Ketiga, mengukur nilai tambah model dibanding tebakan rata-rata, sebagai patokan dasar.

Patokan itu penting. Tanpa pembanding, angka MAE 0,28 tidak berarti apa-apa, karena mungkin saja menebak rata-rata juga mendapatkan angka yang sama."

**Jeda.** Tarik napas, baru pindah slide.

---

## Slide 05: Model yang dibandingkan

**Waktu: sekitar 2 menit**

"Poin keempat, model yang kami bandingkan dan alasan pemilihannya. Ada tiga model, dan masing-masing punya peran berbeda.

Yang pertama Ridge Regression. Ini model linier dengan regularisasi L2. Kami memilihnya karena di data kami banyak notes dan accord yang saling berkorelasi, misalnya bergamot dengan citrus, atau musk dengan white musk. Pada kondisi seperti itu, regresi linier biasa menghasilkan koefisien yang tidak stabil. Regularisasi L2 menekan koefisien tersebut supaya hasilnya wajar. Nilai penaltinya kami cari lewat validasi silang, bukan ditentukan manual. Peran Ridge di sini sebagai pembanding linier. Hasilnya MAE 0,2896 dan R2 0,3494.

Yang kedua Random Forest. Ini kumpulan tiga ratus pohon keputusan yang hasilnya dirata-rata. Dipilih karena mampu menangkap hubungan yang tidak lurus, misalnya patchouli yang pengaruhnya kuat hanya jika muncul bersama amber. Hasilnya MAE 0,2784, paling rendah di antara ketiga model.

Tetapi ada catatan penting. R2 pada data latihnya 0,9118, sementara pada data uji 0,3855. Selisihnya 0,53. Artinya model ini menghafal data latihan, dan berisiko jatuh ketika menerima data baru.

Yang ketiga Gradient Boosting. Pohonnya dibangun berurutan, setiap pohon memperbaiki kesalahan pohon sebelumnya, dan kontribusi tiap pohon dibatasi oleh learning rate 0,05. Hasilnya MAE 0,2821 dan R2 uji 0,3783. Sedikit di bawah Random Forest, tetapi selisih R2 latih dan ujinya hanya 0,066. Artinya model ini jauh lebih stabil.

Dari perbandingan itu, model yang kami pakai di aplikasi adalah Gradient Boosting. Bukan karena angkanya paling bagus, karena MAE Random Forest lebih rendah. Tetapi karena kriteria kami bukan sekadar nilai tertinggi. Kami memakai aturan: selisih R2 latih dan uji harus di bawah 0,10, baru setelah itu dipilih MAE terkecil. Dari aturan tersebut, Gradient Boosting yang lolos dengan performa terbaik. Random Forest tidak lolos karena selisihnya 0,53.

Kriteria ini kami pilih karena aplikasi akan menerima input dari pengguna, yang komposisinya belum tentu ada di data latih. Untuk kondisi seperti itu, konsistensi lebih penting daripada kemenangan tipis pada data uji."

**Kalimat penutup.**

"Jadi yang kami pilih adalah model yang paling stabil, bukan model yang angkanya paling mengkilap di atas kertas. Terima kasih, saya kembalikan ke rekan saya."

---

## Versi 30 detik, kalau waktu dipotong

"Target kami skor ketahanan parfum skala 1 sampai 5, dikerjakan sebagai regresi karena targetnya berjenjang dan skornya bisa desimal. Kami membandingkan Ridge sebagai pembanding linier, Random Forest dan Gradient Boosting sebagai pembanding berbasis pohon. Hasilnya MAE turun dari 0,3699 pada baseline menjadi 0,2784 pada Random Forest. Namun Random Forest mengalami overfitting dengan selisih R2 latih dan uji 0,53, sehingga aplikasi memakai Gradient Boosting yang selisihnya hanya 0,066."

---

## Catatan penyampaian

Angka dibaca perlahan, jangan diburu. "Nol koma dua tujuh delapan empat" itu empat suku kata, kasih jeda. Kalau keburu, pendengar menangkapnya sebagai 0,27.

Waktu menyebut Random Forest, jangan berhenti di "MAE paling rendah". Langsung lanjut ke kelemahannya, supaya tidak didahului pertanyaan.

Kalau lupa satu angka, bilang "saya cek dulu". Jangan mengarang. Satu angka salah bisa meruntuhkan seluruh sesi tanya jawab.

Kalimat yang paling menentukan ada di bagian akhir slide 05: "bukan karena angkanya paling bagus". Ucapkan dengan tenang, jangan terburu-buru.

---

## Jawaban singkat kalau ditanya

**Kenapa regresi, bukan klasifikasi?**
Targetnya angka berjenjang dengan jarak bermakna. Kalau dijadikan kelas, jarak antar skor hilang dan kesalahan jauh tidak bisa dibedakan dari kesalahan dekat.

**Kenapa tiga model?**
Untuk membuktikan peningkatan performa berasal dari pemilihan model, bukan kebetulan. Ridge mewakili pendekatan linier, dua model pohon mewakili non-linier.

**Random Forest MAE-nya paling kecil, kenapa bukan itu?**
Karena R2 latihnya 0,9118 dan R2 ujinya 0,3855, selisih 0,53. Itu tanda menghafal data latihan. Gradient Boosting selisihnya 0,066, jadi lebih aman untuk aplikasi.

**Kenapa bukan XGBoost atau deep learning?**
XGBoost adalah implementasi lain dari algoritma yang sama, dan keunggulannya baru terasa pada data besar. Deep learning butuh data lebih banyak dan sulit dijelaskan. Cakupan penelitian kami dibatasi pada tiga model yang mewakili dua pendekatan.

**Apa arti MAE 0,28?**
Prediksi meleset rata-rata 0,28 poin dari skala 5. Kalau nilai aslinya 3,5, prediksi biasanya berada di kisaran 3,2 sampai 3,8.
