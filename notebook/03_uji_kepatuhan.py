"""Uji kepatuhan dataset & rencana terhadap ketentuan brief project akhir."""
import pandas as pd, numpy as np

df = pd.read_csv('perfumes.csv', low_memory=False)
d = df[df['longevity_avg'].notna() & (df['vote_count'] >= 500)].copy().reset_index(drop=True)

print("=" * 76)
print("A. DATASET — yang wajib dijelaskan menurut brief")
print("=" * 76)
print(f"Jumlah data (mentah)      : {len(df):,} baris x {df.shape[1]} kolom")
print(f"Jumlah data (dipakai)     : {len(d):,} baris")
print(f"Alasan filter             : vote_count >= 500 supaya target stabil")
print()
print("TIPE DATA fitur terpilih:")
for c in ['longevity_avg', 'vote_count', 'year', 'gender', 'brand', 'notes_base', 'accords']:
    print(f"  {c:16s}: {str(df[c].dtype):8s} | contoh: {str(df[c].dropna().iloc[0])[:52]}")
print()
print("MISSING VALUE (di data terpakai):")
for c in ['longevity_avg', 'vote_count', 'year', 'gender', 'brand', 'notes_base', 'notes_middle', 'notes_top', 'accords']:
    n = int(d[c].isna().sum())
    print(f"  {c:16s}: {n:>5,} ({n/len(d)*100:5.1f}%)")
print()
print("DISTRIBUSI TARGET (longevity_avg):")
print(d['longevity_avg'].describe().round(3).to_string())
skew = d['longevity_avg'].skew()
print(f"  skewness : {skew:+.3f}  -> {'normal' if abs(skew)<0.5 else 'miring'}")
print(f"  kurtosis : {d['longevity_avg'].kurt():+.3f}")
print()
q1, q3 = d['longevity_avg'].quantile([0.25, 0.75])
iqr = q3 - q1
lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
out = ((d['longevity_avg'] < lo) | (d['longevity_avg'] > hi)).sum()
print(f"OUTLIER target (IQR)      : {out} baris ({out/len(d)*100:.2f}%) | batas {lo:.2f} - {hi:.2f}")
vout = (d['vote_count'] > d['vote_count'].quantile(0.75) + 1.5*(d['vote_count'].quantile(0.75)-d['vote_count'].quantile(0.25))).sum()
print(f"OUTLIER vote_count (IQR)  : {vout:,} baris ({vout/len(d)*100:.1f}%) -> alasan dipakai log")
print()
print("DUPLIKAT:")
print(f"  baris duplikat penuh     : {int(d.duplicated().sum())}")
print(f"  nama+brand kembar        : {int(d.duplicated(subset=['name','brand']).sum())} (wajar: reformulasi)")
print()
print("KETIDAKSEIMBANGAN KELAS   : N/A - ini regression (target kontinu), bukan klasifikasi")
print()
print("=" * 76)
print("B. KANDIDAT FITUR — cek data leakage")
print("=" * 76)
kandidat = ['vote_count', 'year', 'gender', 'brand', 'notes_top', 'notes_middle',
            'notes_base', 'accords', 'rating_avg', 'sillage_avg', 'price_value_avg',
            'have', 'want', 'people', 'winter', 'summer']
for c in kandidat:
    if c in ('gender', 'brand', 'notes_top', 'notes_middle', 'notes_base', 'accords'):
        print(f"  {c:16s}: teks/kategorikal -> {'PAKAI (encode)' if c!='brand' else 'HATI-HATI (1288 brand)'}")
        continue
    r = d[['longevity_avg', c]].corr().iloc[0, 1]
    if abs(r) > 0.6:
        status = "TOLAK — LEAKAGE"
    elif c in ('rating_avg',):
        status = "TOLAK — target alternatif"
    elif c in ('price_value_avg',):
        status = "TOLAK — vote yang sama"
    else:
        status = "pakai"
    print(f"  {c:16s}: korelasi {r:+.3f} -> {status}")
print()
print("=" * 76)
print("C. TARGET vs ALGORITMA")
print("=" * 76)
print("Tema brief     : B. Regression (prediksi nilai numerik) -> DIIZINKAN")
print("Target         : longevity_avg (numerik kontinu 1-5)  -> SESUAI")
print("Metrik wajib   : MAE, MSE, RMSE, R2                    -> SEMUA TERSEDIA")
print("Algoritma brief: Linear Regression, Random Forest Regression,")
print("                 Gradient Boosting Regression          -> ADA DI DAFTAR")
print("Bonus          : Ridge (algoritma lain yang relevan, diizinkan)")
