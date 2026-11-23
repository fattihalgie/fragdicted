"""Cek kelayakan dataset Fragrantica buat project prediksi longevity."""
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv('perfumes.csv', low_memory=False)
print("=" * 74)
print("1. UKURAN & KELENGKAPAN")
print("=" * 74)
print(f"total baris        : {len(df):,}")
print(f"longevity terisi   : {df['longevity_avg'].notna().sum():,} ({df['longevity_avg'].notna().mean()*100:.1f}%)")
print(f"notes_base terisi  : {df['notes_base'].notna().sum():,}")
print(f"accords terisi     : {df['accords'].notna().sum():,}")

print("\n2. PENGARUH AMBANG vote_count")
print("=" * 74)
for t in [0, 100, 500, 1000, 2000, 5000]:
    s = df[df['longevity_avg'].notna() & (df['vote_count'] >= t)]
    print(f"  vote_count >= {t:>5d} -> {len(s):>7,} baris | std target {s['longevity_avg'].std():.3f}")

d = df[df['longevity_avg'].notna() & (df['vote_count'] >= 500)].copy()
print(f"\n>>> dipakai: {len(d):,} baris (vote_count >= 500)")

print("\n3. UJI DATA LEAKAGE")
print("=" * 74)
for c in ['sillage_avg', 'price_value_avg', 'rating_avg']:
    r = d[['longevity_avg', c]].corr().iloc[0, 1]
    tanda = "  <-- LEAKAGE, JANGAN DIPAKAI" if r > 0.6 else ""
    print(f"  korelasi longevity vs {c:16s}: {r:.3f}{tanda}")

print("\n4. FEATURE ENGINEERING — notes jadi vektor biner")
print("=" * 74)
def parse_notes(s):
    if pd.isna(s):
        return {}
    out = {}
    for part in str(s).split('|'):
        p = part.rsplit(':', 1)
        if len(p) == 2:
            try:
                out[p[0].strip()] = float(p[1])
            except ValueError:
                pass
    return out

base = d['notes_base'].apply(parse_notes)
acc = d['accords'].apply(parse_notes)

from sklearn.feature_extraction import DictVectorizer
for nama, ser in [('base notes', base), ('accords', acc)]:
    dv = DictVectorizer(sparse=False)
    M = dv.fit_transform(list(ser))
    print(f"  {nama:12s}: {M.shape[1]} fitur")

dv = DictVectorizer(sparse=False)
notes_base_M = dv.fit_transform(list(base))
cols_nb = [f'nb_{c}' for c in dv.get_feature_names_out()]
X = pd.DataFrame(notes_base_M, columns=cols_nb, index=d.index)
X['vote_count'] = d['vote_count'].values
X['year'] = d['year'].fillna(d['year'].median()).values
X['log_votes'] = np.log1p(d['vote_count']).values
X = pd.concat([X, pd.get_dummies(d['gender'], prefix='g').reindex(columns=['g_male','g_female','g_unisex'], fill_value=0)], axis=1)
# fitur ordinal dari notes pyramid: jumlah notes per tier
for tier in ['notes_top', 'notes_middle', 'notes_base']:
    X[f'n_{tier}'] = d[tier].apply(lambda s: 0 if pd.isna(s) else len(str(s).split('|'))).values

y = d['longevity_avg'].values
print(f"\n  TOTAL fitur X  : {X.shape[1]}")
print(f"  TOTAL baris    : {X.shape[0]:,}")

print("\n5. LATIH 3 MODEL")
print("=" * 74)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"split 80:20 -> latih {Xtr.shape[0]:,} | uji {Xte.shape[0]:,}\n")
hasil = []
for nama, m in [('Linear Regression', LinearRegression()),
                ('Random Forest', RandomForestRegressor(n_estimators=150, random_state=42, n_jobs=-1)),
                ('Gradient Boosting', GradientBoostingRegressor(random_state=42))]:
    m.fit(Xtr, ytr)
    p = m.predict(Xte)
    hasil.append({'Model': nama,
                  'MAE': mean_absolute_error(yte, p),
                  'RMSE': np.sqrt(mean_squared_error(yte, p)),
                  'R2_test': m.score(Xte, yte),
                  'R2_train': m.score(Xtr, ytr)})
t = pd.DataFrame(hasil).round(3)
t['Gap'] = (t['R2_train'] - t['R2_test']).round(3)
print(t.to_string(index=False))

print("\n6. FITUR PALING BERPENGARUH (dari Random Forest)")
print("=" * 74)
rf = [h for h in hasil if h['Model'] == 'Random Forest'][0]
importances = pd.Series(RandomForestRegressor(n_estimators=150, random_state=42, n_jobs=-1)
                        .fit(Xtr, ytr).feature_importances_, index=X.columns)
print(importances.sort_values(ascending=False).head(12).round(4).to_string())
