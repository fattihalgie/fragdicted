# Cara Deploy Fragdicted ke Streamlit Community Cloud

Panduan ini ditulis untuk kondisi repo saat ini. Semua langkah bisa dikerjakan
dari terminal maupun dari web GitHub.

## 1. Siapkan isi repo

Yang wajib ikut terunggah:

| Path | Fungsi | Ukuran |
|---|---|---|
| `app/app.py` | aplikasi utama | 26 KB |
| `app/style.css` | seluruh tampilan | 14 KB |
| `app/img/n_*.png` | 10 gambar notes untuk latar | 172 KB total |
| `model/model_aplikasi.pkl` | model Gradient Boosting | 267 KB |
| `model/model_info.json` | daftar fitur dan metrik | 8 KB |
| `katalog_parfum.json` | 8.201 parfum untuk mode katalog | 3,2 MB |
| `requirements.txt` | daftar paket | 79 B |
| `.streamlit/config.toml` | tema terang dan port | 250 B |

Yang **tidak** ikut: folder `data/` berisi 181 MB, sudah dikecualikan lewat
`.gitignore`. Aplikasi tidak membacanya sama sekali, jadi aman.

Total repo jadi sekitar 3,5 MB. Jauh di bawah batas 100 MB GitHub.

## 2. Buat repo GitHub

Kalau repo belum ada:

1. Buka github.com, klik New repository.
2. Nama: `fragdicted`. Pilih Public, jangan centang README.
3. Salin perintah yang muncul, lalu jalankan di terminal dari folder proyek.

Kalau mau lewat terminal langsung:

```
cd "C:/Users/ThinkPad/Documents/Semester 5/Machine Learning/ML2026_A_Kelompok09_PrediksiLongevityParfum"
git init
git add .
git commit -m "Fragdicted - aplikasi prediksi ketahanan parfum"
git branch -M main
git remote add origin https://github.com/USERNAME/fragdicted.git
git push -u origin main
```

Ganti `USERNAME` dengan akun GitHub kamu. Saat push pertama, Git akan meminta
login. Pakai Personal Access Token, bukan password. Buat di Settings, Developer
settings, Personal access tokens, Fine-grained tokens, centang scope `repo`.

## 3. Deploy di Streamlit Cloud

1. Buka `share.streamlit.io`, login pakai akun GitHub.
2. Klik **Create app**, pilih **Deploy a public app from GitHub**.
3. Isi:
   - Repository: `USERNAME/fragdicted`
   - Branch: `main`
   - Main file path: `app/app.py`
4. Klik **Deploy**.

Build pertama sekitar 3 sampai 6 menit, karena memasang scikit-learn dan pandas.
Setelah selesai, aplikasi dapat alamat `https://fragdicted.streamlit.app`
atau nama lain kalau sudah dipakai.

## 4. Kalau build gagal

Penyebab paling sering:

**Versi Python.** Streamlit Cloud memakai Python 3.12 atau 3.13 secara default.
Kalau ada paket yang tidak punya wheel untuk versi itu, tambahkan berkas
`runtime.txt` di root berisi satu baris: `python-3.12`. Jangan pakai 3.14,
karena banyak paket belum menyediakan wheel-nya.

**Paket tidak ketemu.** Semua paket di `requirements.txt` sudah ditulis dengan
rentang versi, bukan versi kaku, supaya resolver bebas memilih versi yang
tersedia. Kalau tetap gagal, lihat tab **Logs** di dashboard aplikasi, cari baris
yang mengandung `ERROR`.

**Model gagal dimuat.** Berkas `.pkl` dibuat dengan scikit-learn 1.9.0. Kalau
cloud memasang versi yang berbeda jauh, muncul peringatan
`InconsistentVersionWarning`. Aplikasi masih jalan. Kalau benar-benar error,
kunci versinya dengan menulis `scikit-learn==1.9.0` di `requirements.txt`.

**Berkas tidak ditemukan.** Semua path di `app.py` dihitung relatif terhadap
lokasi berkas itu sendiri, bukan terhadap folder kerja. Jadi jangan pindahkan
`app.py` keluar dari folder `app/` tanpa menyesuaikan path.

## 5. Setelah live

Perbarui README dengan alamat aplikasi. Masukkan alamat itu ke slide presentasi
dan ke daftar luaran sebagai **link aplikasi/deployment**.

Kalau nanti mengubah kode, cukup `git add . && git commit -m "..." && git push`.
Streamlit Cloud otomatis memuat ulang dalam satu sampai dua menit.

## 6. Catatan penting untuk penilaian

Aplikasi ini berjalan tanpa server database dan tanpa API key, jadi tidak perlu
mengatur Secrets. Yang perlu dipastikan hanya tiga berkas ini ikut terunggah:
`model/model_aplikasi.pkl`, `model/model_info.json`, dan `katalog_parfum.json`.
Tanpa salah satunya, aplikasi akan gagal saat start.
