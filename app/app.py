"""Fragdicted - prediksi ketahanan parfum dari komposisinya.
Jalankan dari folder proyek: streamlit run app/app.py
"""
import base64
import json
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "model" / "model_aplikasi.pkl"
INFO_PATH = ROOT / "model" / "model_info.json"
KATALOG_PATH = ROOT / "katalog_parfum.json"
CSS_PATH = Path(__file__).resolve().parent / "style.css"

st.set_page_config(
    page_title="Fragdicted - Prediksi Ketahanan Parfum",
    page_icon="◈",
    layout="wide",
)

st.markdown("<style>" + CSS_PATH.read_text(encoding="utf-8") + "</style>", unsafe_allow_html=True)


@st.cache_resource
def muat_model():
    return joblib.load(MODEL_PATH)


@st.cache_data
def muat_info():
    return json.load(open(INFO_PATH))


@st.cache_data
def muat_katalog():
    return json.load(open(KATALOG_PATH))


model = muat_model()
info = muat_info()
katalog = muat_katalog()

fitur = info["fitur"]
kolom_note = info["kolom_note"]
kolom_accord = info["kolom_accord"]

KONSENTRASI = {
    "Belum dipilih": 0,
    "Eau Fraiche": 1,
    "Eau de Cologne": 2,
    "Eau de Toilette": 3,
    "Eau de Parfum": 4,
    "Extrait de Parfum": 5,
}
LABEL = {1: "Very Weak", 2: "Weak", 3: "Moderate", 4: "Long Lasting", 5: "Eternal"}
DURASI = {1: "kurang dari 1 jam", 2: "1 sampai 2 jam", 3: "3 sampai 6 jam",
          4: "7 sampai 12 jam", 5: "lebih dari 12 jam"}


def nama_note(kolom):
    return kolom.replace("note_", "").replace("_", " ").title()


def nama_accord(kolom):
    return kolom.replace("accord_", "").replace("_", " ").title()


OPSI_NOTE = {nama_note(k): k for k in kolom_note}
OPSI_ACCORD = {nama_accord(k): k for k in kolom_accord}


def botol(warna, tinggi=132, lebar=76):
    """Ilustrasi botol parfum sederhana, dibuat dari bentuk vektor."""
    return f"""
<svg width="{lebar}" height="{tinggi}" viewBox="0 0 76 132" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="27" y="2" width="22" height="13" rx="3" fill="#2B2226" opacity=".82"/>
  <rect x="30" y="14" width="16" height="9" fill="#2B2226" opacity=".5"/>
  <rect x="8" y="23" width="60" height="106" rx="15" fill="{warna}"/>
  <rect x="8" y="23" width="60" height="106" rx="15" fill="url(#g{tinggi}{lebar})" opacity=".55"/>
  <rect x="16" y="34" width="13" height="86" rx="6.5" fill="#FFFFFF" opacity=".3"/>
  <rect x="24" y="60" width="28" height="33" rx="4" fill="#FFFDFB" opacity=".88"/>
  <text x="38" y="76" font-size="7" fill="{warna}" text-anchor="middle"
        font-family="Georgia, serif" font-weight="bold">FRAG</text>
  <text x="38" y="86" font-size="5" fill="#7A6A62" text-anchor="middle"
        font-family="Helvetica, sans-serif" letter-spacing="1">DICTED</text>
  <defs>
    <linearGradient id="g{tinggi}{lebar}" x1="8" y1="23" x2="68" y2="129">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity=".55"/>
      <stop offset="1" stop-color="#000000" stop-opacity=".12"/>
    </linearGradient>
  </defs>
</svg>"""


def gambar_b64(nama):
    p = Path(__file__).resolve().parent / "img" / (nama + ".png")
    if not p.exists():
        return ""
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode()


CATATAN_LATAR = [
    ("n_bergamot", "Bergamot", 3, 6, 96, -10, 0.50),
    ("n_lemon", "Lemon", 86, 3, 88, 8, 0.38),
    ("n_orange", "Orange", 3, 27, 80, 6, 0.32),
    ("n_rose", "Rose", 86, 25, 94, -8, 0.44),
    ("n_jasmine", "Jasmine", 3, 48, 84, 9, 0.40),
    ("n_vanilla", "Vanilla", 87, 46, 78, -9, 0.34),
    ("n_patchouli", "Patchouli", 3, 68, 92, -7, 0.42),
    ("n_oud", "Oud", 87, 66, 82, 8, 0.34),
    ("n_sandalwood", "Sandalwood", 4, 86, 76, -10, 0.30),
    ("n_cedar", "Cedar", 86, 84, 90, 6, 0.40),
]

# ============================== LATAR 3D ==============================
_LAPIS = ""
for _kode, _label, _x, _y, _w, _rot, _op in CATATAN_LATAR:
    _LAPIS += (
        '<img class="note3d" style="left:' + str(_x) + "%;top:" + str(_y) + "%;width:" + str(_w)
        + "px;--rot:" + str(_rot) + "deg;opacity:" + str(_op)
        + '" src="' + gambar_b64(_kode) + '" alt="' + _label + '">'
    )
ART = (
    '<div class="hero-art">'
    + '<img class="medali m1" src="' + gambar_b64("n_bergamot") + '" alt="Bergamot">'
    + '<img class="medali m2" src="' + gambar_b64("n_oud") + '" alt="Oud">'
    + '<img class="medali m3" src="' + gambar_b64("n_vanilla") + '" alt="Vanilla">'
    + '<div class="hero-art-label">Bergamot &middot; Oud &middot; Vanilla</div>'
    + "</div>"
)

st.markdown(
    '<div class="bg3d"><div class="bg3d-inner">' + _LAPIS + "</div></div>",
    unsafe_allow_html=True,
)

# ============================== HERO ==============================
st.markdown(
    f"""
    <div class="hero">
      <div class="hero-grid">
        <div>
          <div class="hero-eyebrow">Pembelajaran Mesin &middot; Kelompok 9</div>
          <div class="hero-title">Fragdicted<br><i>tahu wanginya,</i><br>tahu tahan berapa lama</div>
          <p class="hero-sub">Parfum dibeli tanpa bisa dicoba dulu, dan ketahanannya baru
          ketahuan setelah dipakai. Fragdicted memprediksi <b>skor ketahanan 1 sampai 5</b>
          hanya dari komposisi: fragrance notes, accords, dan tingkat konsentrasi.</p>
        </div>
        <div>{ART}</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="stat-row">
      <div class="stat-cell c1"><div class="stat-num">8.211</div><div class="stat-label">Parfum dilatih</div></div>
      <div class="stat-cell c2"><div class="stat-num">181</div><div class="stat-label">Fitur komposisi</div></div>
      <div class="stat-cell c3"><div class="stat-num">0,282</div><div class="stat-label">MAE uji</div></div>
      <div class="stat-cell c4"><div class="stat-num">0,38</div><div class="stat-label">R&sup2; uji</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================== PREDIKSI ==============================
st.markdown('<div class="sec"><span class="dot"></span>Prediksi ketahanan</div>', unsafe_allow_html=True)

mode = st.radio("Cara memasukkan data", ["Pilih dari katalog", "Isi manual"],
                horizontal=True, label_visibility="collapsed")

pilihan = None
if mode == "Pilih dari katalog":
    daftar = sorted({p["brand"] + " - " + p["nama"] for p in katalog})
    cari = st.selectbox("Cari parfum (" + str(len(daftar)) + " tersedia)", daftar, index=None, placeholder="Ketik nama parfum atau brand")
    if cari:
        brand, nama = cari.split(" - ", 1)
        kandidat = [p for p in katalog if p["brand"] == brand and p["nama"] == nama]
        if len(kandidat) > 1:
            opsi = [p["nama"] + " (" + p["konsentrasi"] + ")" for p in kandidat]
            idx = st.selectbox("Ada beberapa versi", range(len(opsi)), format_func=lambda i: opsi[i])
            pilihan = kandidat[idx]
        else:
            pilihan = kandidat[0]

if pilihan:
    note_awal = sorted(nama_note("note_" + k) for k in pilihan["notes"])
    accord_awal = sorted(nama_accord("accord_" + k) for k in pilihan["accords"])
    konsentrasi_awal = pilihan["konsentrasi"]
else:
    note_awal, accord_awal, konsentrasi_awal = [], [], "Belum dipilih"

indeks_konsentrasi = list(KONSENTRASI).index(konsentrasi_awal) if konsentrasi_awal in KONSENTRASI else 0

if pilihan and pilihan["level"] == 0:
    st.info("Konsentrasi parfum ini tidak tercatat di dataset. Pilih manual di bawah.")

with st.form("form_prediksi"):
    c1, c2 = st.columns(2)
    with c1:
        dipilih_note = st.multiselect("Fragrance notes", sorted(OPSI_NOTE), default=note_awal, placeholder="Pilih notes")
    with c2:
        dipilih_accord = st.multiselect("Accords", sorted(OPSI_ACCORD), default=accord_awal, placeholder="Pilih accords")
    c3, c4 = st.columns([1, 1])
    with c3:
        konsentrasi = st.selectbox("Tingkat konsentrasi", list(KONSENTRASI), index=indeks_konsentrasi)
    with c4:
        st.write("")
        st.write("")
        kirim = st.form_submit_button("Hitung ketahanan")

if kirim:
    if KONSENTRASI[konsentrasi] == 0:
        st.error("Tingkat konsentrasi wajib dipilih.")
    elif not dipilih_note and not dipilih_accord:
        st.error("Isi minimal satu fragrance note atau satu accord.")
    else:
        baris = {k: 0.0 for k in fitur}
        if pilihan:
            for k, v in pilihan["notes"].items():
                kolom = "note_" + k
                if kolom in baris:
                    baris[kolom] = float(v)
            for k, v in pilihan["accords"].items():
                kolom = "accord_" + k
                if kolom in baris:
                    baris[kolom] = float(v)
        else:
            for nm in dipilih_note:
                baris[OPSI_NOTE[nm]] = 0.5
            for nm in dipilih_accord:
                baris[OPSI_ACCORD[nm]] = 0.5
        baris["concentration_level"] = float(KONSENTRASI[konsentrasi])
        X = pd.DataFrame([baris])[fitur]
        nilai = max(1.0, min(5.0, float(model.predict(X)[0])))
        bulat = int(round(nilai))

        st.markdown('<div class="sec"><span class="dot"></span>Hasil prediksi</div>', unsafe_allow_html=True)
        kiri, kanan = st.columns([1, 1.35])

        with kiri:
            st.markdown(
                '<div class="score-wrap">'
                '<div class="score-num">' + f"{nilai:.2f}" + '<span class="score-den"> / 5</span></div>'
                '<div class="score-cat">' + LABEL[bulat] + '</div>'
                '<div class="score-note">' + DURASI[bulat] + '</div>'
                "</div>", unsafe_allow_html=True)
            st.write("")
            st.progress((nilai - 1) / 4)
            if pilihan:
                st.markdown(
                    '<div class="card" style="margin-top:16px">'
                    '<div class="card-brand">' + pilihan["brand"] + "</div>"
                    '<div class="card-name">' + pilihan["nama"] + "</div>"
                    '<div class="card-meta">' + str(len(pilihan["notes"])) + " notes &middot; "
                    + str(len(pilihan["accords"])) + " accords &middot; " + konsentrasi + "</div></div>",
                    unsafe_allow_html=True)

        with kanan:
            sumber_note = pilihan["notes"] if pilihan else {OPSI_NOTE[n].replace("note_", ""): 0.5 for n in dipilih_note}
            sumber_accord = pilihan["accords"] if pilihan else {OPSI_ACCORD[n].replace("accord_", ""): 0.5 for n in dipilih_accord}
            if sumber_accord:
                st.markdown('<div class="sec" style="margin-top:0"><span class="dot"></span>Accords dominan</div>',
                            unsafe_allow_html=True)
                h = ""
                for k, v in sorted(sumber_accord.items(), key=lambda x: -x[1])[:6]:
                    h += ('<div class="bar-row"><div class="bar-name">' + nama_accord("accord_" + k) + "</div>"
                          '<div class="bar-track"><div class="bar-fill" style="width:' + str(int(float(v) * 100))
                          + '%"></div></div><div class="bar-val">' + f"{float(v):.2f}" + "</div></div>")
                st.markdown(h, unsafe_allow_html=True)
            if sumber_note:
                st.markdown('<div class="sec"><span class="dot"></span>Fragrance notes</div>', unsafe_allow_html=True)
                chip = ""
                for k, v in sorted(sumber_note.items(), key=lambda x: -x[1])[:14]:
                    chip += ('<span class="' + ("chip chip-strong" if float(v) >= 0.7 else "chip") + '">'
                             + nama_note("note_" + k) + "</span>")
                st.markdown(chip, unsafe_allow_html=True)

# ============================== LATAR BELAKANG ==============================
st.markdown('<div class="sec"><span class="dot"></span>Kenapa masalah ini penting</div>', unsafe_allow_html=True)

st.markdown(
    """
    <p class="prose">Membeli parfum itu keputusan yang mahal dan tidak bisa diuji coba.
    Di toko, yang bisa dicium hanya <em>top notes</em> dalam lima menit pertama. Padahal
    sifat parfum yang paling menentukan kepuasan pemakai justru muncul belakangan:
    <strong>berapa lama wanginya bertahan</strong>. Pembeli baru tahu jawabannya setelah
    uang keluar dan botol dibuka.</p>

    <p class="prose">Masalahnya, informasi ketahanan sebenarnya sudah ada di permukaan
    botol. Setiap parfum mencantumkan komposisi bahan, dan setiap bahan punya sifat
    penguapan yang berbeda. Bahan berbobot molekul berat seperti musk, amber, dan
    patchouli menguap lambat. Bahan ringan seperti bergamot dan lemon menguap dalam
    hitungan menit. Artinya, <strong>komposisi membawa sinyal tentang ketahanan</strong>,
    hanya saja sinyal itu tersebar di ratusan bahan sekaligus dan tidak bisa dibaca
    dengan mata.</p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="point"><div class="point-num">1</div><div class="point-txt">
      <strong>Pembeli tidak punya alat ukur.</strong> Ulasan di internet subjektif dan
    sangat dipengaruhi kulit pemakainya. Satu parfum bisa bertahan 3 jam di satu orang
    dan 8 jam di orang lain. Tidak ada cara membandingkan secara adil.</div></div>

    <div class="point"><div class="point-num">2</div><div class="point-txt">
      <strong>Produsen kecil kesulitan merancang.</strong> Peracik pemula biasanya
    menebak-nebak komposisi lalu menguji berulang kali. Padahal arah pengaruh tiap bahan
    terhadap ketahanan bisa dipelajari dari data yang sudah terkumpul.</div></div>

    <div class="point"><div class="point-num">3</div><div class="point-txt">
      <strong>Belum ada model yang mencoba menjawabnya.</strong> Penelitian sebelumnya
    mengukur penguapan di laboratorium atau memprediksi notes dari teks deskripsi.
    Belum ada yang memprediksi skor ketahanan langsung dari komposisi, memakai data
    persepsi pengguna dalam jumlah besar.</div></div>
    """,
    unsafe_allow_html=True,
)

# ============================== SOLUSI ==============================
st.markdown('<div class="sec"><span class="dot"></span>Yang kami bangun</div>', unsafe_allow_html=True)

st.markdown(
    """
    <p class="prose"><strong>Fragdicted</strong> adalah model regresi yang memetakan
    komposisi parfum ke skor ketahanan pada skala 1 sampai 5. Masukannya 126 fragrance
    notes, 54 accords, dan tingkat konsentrasi. Keluarannya satu angka desimal, misalnya
    3,25, yang bisa langsung dibaca sebagai perkiraan durasi pemakaian.</p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="info-grid">
      <div class="info-card g1">
        <div class="info-card-title">Mengapa regresi, bukan klasifikasi</div>
        <div class="info-card-body">Target kami berasal dari penilaian pengguna yang
        berjenjang 1 sampai 5 dan bisa bernilai desimal. Kalau dipaksa menjadi kelas,
        <b>jarak antar skor hilang</b>. Model yang menebak 3,4 saat nilai aslinya 3,5
        seharusnya dinilai lebih baik daripada yang menebak 5, dan itu hanya bisa
        dihargai oleh regresi.</div>
      </div>
      <div class="info-card g2">
        <div class="info-card-title">Mengapa memakai data komunitas</div>
        <div class="info-card-body">Pengukuran laboratorium hanya mencakup belasan
        parfum. Kami memakai <b>8.211 parfum</b> yang masing-masing dinilai minimal 500
        orang. Bobot tiap bahan diambil dari frekuensi penyebutannya oleh komunitas,
        sehingga mencerminkan komposisi yang benar-benar dirasakan, bukan klaim
        pemasaran.</div>
      </div>
      <div class="info-card g3">
        <div class="info-card-title">Mengapa tiga model dibandingkan</div>
        <div class="info-card-body">Tiga model mewakili tiga cara berpikir berbeda:
        penjumlahan berbobot, pengelompokan berbasis aturan, dan perbaikan bertahap.
        Membandingkannya menunjukkan <b>pendekatan mana yang cocok</b> untuk data
        komposisi yang sangat jarang (91,2 persen sel bernilai nol).</div>
      </div>
      <div class="info-card g4">
        <div class="info-card-title">Untuk siapa alat ini</div>
        <div class="info-card-body">Untuk pembeli yang ingin memperkirakan ketahanan
        sebelum membeli, untuk penjual yang ingin menjelaskan produknya dengan angka,
        dan untuk peracik yang ingin tahu bahan mana yang paling menyumbang daya
        tahan.</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================== MODEL ==============================
st.markdown('<div class="sec"><span class="dot"></span>Model yang dipakai</div>', unsafe_allow_html=True)

st.markdown(
    """
    <p class="prose">Model yang berjalan di aplikasi ini adalah
    <strong>Gradient Boosting Regressor</strong>, 200 pohon dengan learning rate 0,05
    dan kedalaman maksimum 3. Model ini tidak memilih parfum terbaik, tetapi mempelajari
    pola dari 6.568 data latih, lalu menguji kemampuannya pada 1.643 data yang belum
    pernah dilihat, dengan pembagian 80 banding 20 dan seed tetap 42.</p>

    <p class="prose">Cara kerjanya bertahap. Model mulai dari tebakan awal berupa
    rata-rata seluruh data, yaitu 3,27395. Lalu 200 pohon dibangun satu per satu, dan
    setiap pohon baru bertugas membenahi sisa kesalahan pohon sebelumnya. Kontribusi
    tiap pohon sengaja dikecilkan oleh learning rate 0,05, supaya tidak ada satu pohon
    yang terlalu mendominasi. Hasil akhirnya adalah tebakan awal ditambah akumulasi
    koreksi dari 200 pohon tersebut.</p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="step"><div class="step-n">1</div><div class="step-body">
      <strong>Masukan.</strong> 181 angka untuk satu parfum: bobot 126 notes, bobot 54
      accords, dan satu angka tingkat konsentrasi. Sebagian besar bernilai nol, karena
      satu parfum hanya memakai belasan bahan.</div></div>
    <div class="step"><div class="step-n">2</div><div class="step-body">
      <strong>Tebakan awal.</strong> Model memulai dari rata-rata data latih, 3,27395.
      Ini sama dengan tebakan orang yang tidak tahu apa pun tentang parfum itu.</div></div>
    <div class="step"><div class="step-n">3</div><div class="step-body">
      <strong>Koreksi bertahap.</strong> 200 pohon kecil membaca kombinasi bahan, lalu
      masing-masing memberi koreksi. Koreksi dikali 0,05 supaya halus, lalu dijumlahkan.
      Inilah sebabnya parfum berbahan berat dan berkonsentrasi tinggi mendapat angka
      lebih besar.</div></div>
    <div class="step"><div class="step-n">4</div><div class="step-body">
      <strong>Keluaran.</strong> Satu angka desimal, dipotong ke rentang 1 sampai 5,
      lalu diterjemahkan menjadi kategori dan perkiraan durasi pemakaian.</div></div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p class="prose">Kenapa bukan model lain? <strong>Ridge Regression</strong> kami
    pakai sebagai pembanding linier, karena data kami mengandung banyak bahan yang
    saling berkorelasi sehingga regresi biasa menghasilkan koefisien tidak stabil.
    <strong>Random Forest</strong> kami pakai sebagai pembanding berbasis pohon, karena
    ia mampu menangkap kombinasi bahan. Keduanya diuji dengan data dan metrik yang sama
    persis, dan hasilnya ada di tabel bawah.</p>
    """,
    unsafe_allow_html=True,
)

# ============================== PERBANDINGAN ==============================
st.markdown('<div class="sec"><span class="dot"></span>Perbandingan tiga model</div>', unsafe_allow_html=True)

metrik = info["metrik"]


def baris_tabel(nama, kunci, kelas, tag):
    m = metrik[kunci]
    return (
        '<tr class="' + kelas + '"><td>' + nama + tag + "</td>"
        '<td class="num">' + f"{m['MAE']:.4f}".replace(".", ",") + "</td>"
        '<td class="num">' + f"{m['RMSE']:.4f}".replace(".", ",") + "</td>"
        '<td class="num">' + f"{m['R2']:.4f}".replace(".", ",") + "</td>"
        '<td class="num">' + f"{m['R2_latih']:.4f}".replace(".", ",") + "</td>"
        '<td class="num">' + f"{m['selisih_R2']:.4f}".replace(".", ",") + "</td></tr>"
    )


tabel = (
    '<table class="cmp"><thead><tr>'
    "<th>Model</th><th>MAE</th><th>RMSE</th><th>R&sup2; uji</th>"
    "<th>R&sup2; latih</th><th>Selisih</th></tr></thead><tbody>"
    + baris_tabel("Baseline rata-rata", "Baseline (rata-rata)", "", "")
    + baris_tabel("Ridge Regression", "Ridge", "", "")
    + baris_tabel("Random Forest", "Random Forest", "", '<span class="tag-no">overfitting</span>')
    + baris_tabel("Gradient Boosting", "Gradient Boosting", "pilih", '<span class="tag-pilih">dipakai</span>')
    + "</tbody></table>"
    '<p class="cmp-note">Diuji pada 1.643 parfum yang sama. MAE lebih kecil lebih baik, '
    "R&sup2; lebih besar lebih baik, selisih R&sup2; lebih kecil lebih baik.</p>"
)

st.markdown(tabel, unsafe_allow_html=True)

st.markdown(
    """
    <div class="warn-box">
    <b>Kenapa bukan Random Forest, padahal MAE-nya paling kecil?</b><br>
    Random Forest menang tipis di MAE, 0,2784 melawan 0,2821, selisihnya hanya 0,0037
    poin. Tetapi R&sup2; pada data latihnya 0,9118 sementara pada data uji 0,3855.
    Selisih 0,53 itu tanda model menghafal data latihan. Gradient Boosting selisihnya
    hanya 0,066. Aturan yang kami pakai: selisih R&sup2; harus di bawah 0,10, baru
    setelah itu dipilih MAE terkecil. Random Forest tidak lolos aturan itu.
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================== DATA ==============================
st.markdown('<div class="sec"><span class="dot"></span>Data yang dipakai</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="info-grid">
      <div class="info-card g2">
        <div class="info-card-title">Sumber</div>
        <div class="info-card-body">Dataset publik <b>Fragrantica Perfumes: Ratings,
        Notes, Votes and More</b> oleh Le Decanteur di Kaggle, diakses September 2026.
        Lisensi CC BY-NC-SA 4.0, dipakai hanya untuk keperluan akademik.</div>
      </div>
      <div class="info-card g1">
        <div class="info-card-title">Penyaringan</div>
        <div class="info-card-body">Dari 140.228 parfum, kami ambil yang punya minimal
        <b>500 suara pengguna</b>. Sisanya 8.211 parfum. Tanpa saringan ini, skor
        ketahanan dari parfum yang hanya dinilai 3 orang akan membuat data terlalu
        bising.</div>
      </div>
      <div class="info-card g3">
        <div class="info-card-title">Fitur</div>
        <div class="info-card-body"><b>126 notes</b> dan <b>54 accords</b>, masing-masing
        berupa bobot relatif 0 sampai 1 dari suara komunitas. Ditambah satu kolom
        tingkat konsentrasi. Total 181 fitur, dengan 91,2 persen sel bernilai nol.</div>
      </div>
      <div class="info-card g4">
        <div class="info-card-title">Target</div>
        <div class="info-card-body">Rata-rata penilaian ketahanan pengguna pada skala
        1 sampai 5. Sebarannya: skor 2 sebanyak 347 parfum, skor 3 sebanyak 5.245,
        skor 4 sebanyak 2.590, skor 5 sebanyak 29.</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================== KETERBATASAN ==============================
st.markdown('<div class="sec"><span class="dot"></span>Apa yang perlu diketahui sebelum memakai</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="point"><div class="point-num">1</div><div class="point-txt">
      <strong>Model hanya menjelaskan 38 persen.</strong> R&sup2; 0,38 berarti komposisi
      menjelaskan sekitar 38 persen variasi ketahanan. Sisanya dipengaruhi kulit pemakai,
      cuaca, cara penyemprotan, kualitas bahan baku, dan kandungan fixative yang tidak
      tercatat sebagai fragrance note.</div></div>

    <div class="point"><div class="point-num">2</div><div class="point-txt">
      <strong>Konsentrasi hanya terisi 33,95 persen.</strong> Dari 8.211 parfum, hanya
      2.788 yang mencantumkan tingkat konsentrasi di dataset. Untuk sisanya, pengguna
      harus memilih sendiri, dan pilihan itu memengaruhi hasil.</div></div>

    <div class="point"><div class="point-num">3</div><div class="point-txt">
      <strong>Prediksi tidak bisa melewati batas data.</strong> Model berbasis pohon tidak
      dapat memperkirakan nilai di luar rentang yang pernah dilihatnya. Karena skor 5
      hanya diwakili 29 parfum, prediksi tertinggi yang keluar mentok di sekitar 4,1
      walaupun nilai aktual mencapai 4,9.</div></div>

    <div class="point"><div class="point-num">4</div><div class="point-txt">
      <strong>Bobot manual itu kasar.</strong> Kalau memilih bahan secara manual, semua
      bahan diberi bobot seragam 0,5 karena tidak ada data suara komunitas. Mode katalog
      jauh lebih akurat karena memakai bobot asli.</div></div>
    """,
    unsafe_allow_html=True,
)

# ============================== FOOTER ==============================
st.markdown(
    """
    <div class="credit">
    <b>Fragdicted</b> &middot; Project Akhir Pembelajaran Mesin TEK1302 &middot; Kelas A,
    Kelompok 9<br>
    Fattih Algie Maulana (J0404241002), Aisyah Elfiyuni M.A (J0404241067),
    Anggi Permana Putra (J0404241154)<br><br>
    <b>Sumber data.</b> Le Decanteur. (2025). Fragrantica Perfumes: Ratings, Notes,
    Votes and More [Data set]. Kaggle. Lisensi CC BY-NC-SA 4.0.<br>
    <b>Arti nilai.</b> Angka notes dan accords adalah bobot relatif 0 sampai 1 dari suara
    pengguna, bukan persentase bahan. Hasil prediksi adalah perkiraan model
    (Gradient Boosting, MAE 0,2821, R&sup2; 0,3783), bukan jaminan daya tahan sebenarnya.<br><br>
    <b>Gambar notes.</b> Sepuluh bahan dipakai sebagai ilustrasi latar: bergamot, lemon,
    jeruk, rose, jasmine, vanilla, patchouli, oud, sandalwood, dan cedar. Fotonya
    diambil dari Wikimedia Commons dan Openverse dengan lisensi terbuka, lalu
    dipotong jadi medali bundar supaya menyatu dengan halaman. Fungsinya hiasan,
    bukan dokumentasi bahan asli tiap parfum.
    </div>
    """,
    unsafe_allow_html=True,
)
