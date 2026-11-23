# Persiapan Presentasi

**Bagian yang menjadi tanggung jawab saya:** poin 3 dan poin 4
**Judul:** Prediksi Tingkat Ketahanan (Longevity) Parfum Berdasarkan Komposisi Fragrance Notes, Accords, dan Tingkat Konsentrasi Menggunakan Perbandingan Ridge Regression, Random Forest, dan Gradient Boosting

Catatan: poin 1 (latar belakang), poin 2 (data), dan poin 5 (metrik evaluasi) dibahas oleh anggota lain, jadi tidak dimasukkan ke dokumen ini.

---

# Poin 3: Target, goal, dan tujuan

## Target yang diprediksi

Skor ketahanan (longevity) parfum, berupa angka 1 sampai 5.

Skala ini berasal dari penilaian pengguna Fragrantica:

| Skor | Kategori | Perkiraan daya tahan |
|---|---|---|
| 1 | Very Weak | kurang dari 1 jam |
| 2 | Weak | 1 sampai 2 jam |
| 3 | Moderate | 3 sampai 6 jam |
| 4 | Long Lasting | 7 sampai 12 jam |
| 5 | Eternal | lebih dari 12 jam |

## Jenis permasalahan

Termasuk regresi, bukan klasifikasi. Alasannya, target berupa angka berjenjang yang punya jarak antar level, sehingga diperlakukan sebagai nilai kontinu. Konsekuensinya, hasil model berupa angka desimal, misalnya 3,48, bukan kelas bulat.

## Tujuan umum

Memberi perkiraan ketahanan parfum sebelum dibeli, hanya berdasarkan komposisi dan tingkat konsentrasinya.

## Tujuan khusus

1. Membandingkan performa Ridge Regression, Random Forest, dan Gradient Boosting dalam memprediksi ketahanan parfum.
2. Mengukur seberapa besar fragrance notes, accords, dan tingkat konsentrasi mampu menjelaskan variasi ketahanan parfum.
3. Membangun aplikasi yang bisa menerima input komposisi lalu menampilkan perkiraan skor ketahanan.

## Manfaat yang bisa disampaikan

Selama ini ketahanan parfum hanya diketahui setelah membeli dan memakainya. Ulasan yang tersedia bersifat subjektif dan tersebar. Dengan model ini, perkiraan bisa diperoleh lebih awal dari data komposisi yang sudah tersedia di katalog parfum.

---

# Poin 4: Model yang dipilih dan alasannya

Ada tiga model, dipilih dengan peran yang berbeda. Yang penting disampaikan bukan hanya nama modelnya, tetapi alasan masing-masing ada di perbandingan ini.

## 1. Ridge Regression

**Peran:** pembanding berbasis model linier.

**Alasan dipilih:** jumlah fitur besar dan banyak notes yang saling berkorelasi, misalnya bergamot dengan jeruk, atau musk dengan white musk. Pada kondisi seperti itu, regresi linier biasa menghasilkan koefisien yang tidak stabil. Ridge menambahkan penalti pada koefisien sehingga hasilnya lebih tahan terhadap korelasi antar fitur.

**Detail teknis yang layak disebut:** nilai alpha ditentukan melalui GridSearchCV dengan validasi silang tiga lipatan, bukan ditentukan secara manual.

**Hasil:** MAE 0,2896 dan R2 uji 0,3494.

## 2. Random Forest

**Peran:** pembanding berbasis pohon yang dibangun paralel.

**Alasan dipilih:** mampu menangkap hubungan non-linier dan interaksi antar bahan, misalnya patchouli yang pengaruhnya kuat hanya ketika muncul bersama amber. Model ini juga relatif tahan terhadap fitur yang jarang muncul, dan menyediakan feature importance sehingga bisa dijelaskan fitur mana yang paling berpengaruh.

**Hasil:** MAE 0,2784 dan R2 uji 0,3855.

## 3. Gradient Boosting

**Peran:** pembanding berbasis pohon yang dibangun bertahap.

**Alasan dipilih:** pohon dibangun satu per satu, setiap pohon baru memperbaiki kesalahan pohon sebelumnya. Pada data tabular, pendekatan bertahap ini umumnya memberi generalisasi lebih baik dibandingkan pohon paralel.

**Hasil:** MAE 0,2821 dan R2 uji 0,3783.

## Tabel hasil perbandingan

| Model | MAE | R2 uji | R2 latih | Selisih R2 |
|---|---|---|---|---|
| Baseline (rata-rata) | 0,3699 | -0,0008 | 0,0000 | 0,0008 |
| Ridge Regression | 0,2896 | 0,3494 | 0,3653 | 0,0159 |
| Random Forest | 0,2784 | 0,3855 | 0,9118 | 0,5263 |
| Gradient Boosting | 0,2821 | 0,3783 | 0,4440 | 0,0657 |

Baris baseline adalah pembanding paling dasar, yaitu selalu menebak nilai rata-rata. Ketiga model harus lebih baik dari baris ini agar perbandingannya bermakna.

## Model yang dipakai pada aplikasi

Gradient Boosting.

**Alasannya:** Random Forest memang punya MAE paling kecil, tetapi R2 latihnya 0,9118 sementara R2 ujinya 0,3855. Selisih sebesar 0,53 menunjukkan model menghafal data latihan. Gradient Boosting hanya memiliki selisih 0,066, sehingga lebih stabil ketika menerima data baru. Kriteria pemilihan yang dipakai adalah selisih R2 latih dan uji di bawah 0,10, lalu dari yang lolos dipilih MAE terkecil.

## Kenapa membandingkan tiga model, bukan satu

Supaya peningkatan performa bisa dibuktikan berasal dari modelnya, bukan kebetulan. Ridge berperan sebagai batas bawah pendekatan linier, sedangkan dua model pohon menunjukkan apakah hubungan non-linier memberi tambahan yang berarti. Kalau hanya memakai satu model, tidak ada dasar untuk mengatakan model tersebut yang terbaik.

## Kenapa tidak memakai deep learning

Data berbentuk tabular dan jumlah baris latihnya relatif kecil. Deep learning umumnya butuh data jauh lebih banyak untuk memberi keunggulan, dan hasilnya sulit dijelaskan kepada penguji. Tiga model yang dipakai sudah mewakili pendekatan linier dan non-linier, sekaligus tetap bisa dijelaskan alasan pemilihannya.

---

# Isi slide bagian saya

Sesuai kesepakatan kelompok, total slide tiga halaman dan setiap orang mengisi satu halaman. Bagian saya mencakup poin 3 dan poin 4.

## Slide bagian saya, isi wajib

- Target yang diprediksi: skor ketahanan 1 sampai 5, dengan skala singkatnya
- Alasan memakai regresi, bukan klasifikasi
- Tiga tujuan khusus, ditulis singkat dalam bentuk poin
- Tiga model dengan satu kalimat alasan masing-masing
- Tabel hasil: baseline, Ridge, Random Forest, Gradient Boosting, kolom MAE dan R2
- Satu kalimat penutup: model yang dipakai di aplikasi adalah Gradient Boosting, karena selisih latih dan ujinya paling kecil

## Yang sebaiknya tidak dimasukkan ke slide

- Penjelasan panjang tentang dataset dan proses pembersihan, karena itu bagian anggota lain
- Rumus matematis Ridge, Random Forest, atau Gradient Boosting
- Tabel hasil lengkap dengan kolom RMSE dan selisih R2, cukup MAE dan R2 saja
- Teks panjang, karena slide hanya alat bantu, penjelasan disampaikan lisan

## Alur penyampaian lisan, sekitar dua menit

1. Sebut target yang diprediksi dan skalanya
2. Sebut tiga tujuan khusus
3. Sebut tiga model beserta peran masing-masing
4. Tunjuk tabel hasil, sebut satu angka penting: MAE turun dari 0,3699 pada baseline menjadi 0,2784 pada model terbaik
5. Tutup dengan alasan pemilihan Gradient Boosting untuk aplikasi

---

# Pertanyaan penguji yang perlu disiapkan

**Kenapa regresi, bukan klasifikasi?**
Targetnya berjenjang dan punya jarak antar level, sehingga lebih tepat diperlakukan sebagai angka kontinu. Kalau dibuat klasifikasi, informasi jarak antar level hilang dan kesalahan prediksi tidak bisa diukur seberapa jauh.

**Kenapa membandingkan tiga model, bukan satu saja?**
Untuk membuktikan bahwa performa yang diperoleh berasal dari pemilihan model, bukan kebetulan. Ridge menjadi pembanding linier, dua model pohon menjadi pembanding non-linier.

**Kalau Random Forest MAE-nya paling kecil, kenapa aplikasinya memakai Gradient Boosting?**
Karena MAE kecil saja tidak cukup. Random Forest memiliki R2 latih 0,9118 dan R2 uji 0,3855, selisihnya 0,53. Itu tanda model menghafal data latihan. Gradient Boosting selisihnya hanya 0,066, jadi lebih aman dipakai pada data baru.

**Kenapa tidak memakai deep learning?**
Data tabular dengan jumlah baris terbatas. Deep learning butuh data lebih banyak, dan hasilnya sulit dijelaskan.

**Apa tujuan praktis penelitian ini?**
Memberi perkiraan ketahanan parfum sebelum dibeli, sehingga pembeli tidak perlu menebak dari ulasan yang subjektif.

**Apa yang tidak bisa dilakukan model ini?**
Model hanya berlaku untuk parfum dengan komposisi yang tercatat. Parfum tanpa data notes dan accords tidak bisa diprediksi. Faktor kondisi kulit, cuaca, dan cara pemakaian juga tidak masuk ke model.

---

# Prioritas belajar jika waktu terbatas

1. Hafalkan tabel hasil perbandingan, khususnya kolom MAE dan R2
2. Hafalkan alasan pemilihan Gradient Boosting untuk aplikasi
3. Hafalkan tiga tujuan khusus
4. Siapkan jawaban untuk pertanyaan regresi versus klasifikasi

Empat hal tersebut menutup sebagian besar pertanyaan yang mungkin muncul pada dua poin ini.
