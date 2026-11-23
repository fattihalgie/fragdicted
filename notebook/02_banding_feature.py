"""Bandingkan strategi feature engineering buat prediksi longevity."""
import pandas as pd, numpy as np
from collections import Counter
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv('perfumes.csv', low_memory=False)
d = df[df['longevity_avg'].notna() & (df['vote_count'] >= 500)].copy().reset_index(drop=True)
y = d['longevity_avg'].values
print(f"data: {len(d):,} baris | target mean {y.mean():.3f} std {y.std():.3f}")
print(f"baseline tebak-rata-rata  -> MAE {np.abs(y - y.mean()).mean():.3f}\n")


def parse(s):
    if pd.isna(s):
        return {}
    out = {}
    for p in str(s).split('|'):
        q = p.rsplit(':', 1)
        if len(q) == 2:
            try:
                out[q[0].strip()] = float(q[1])
            except ValueError:
                pass
    return out


for kolom, topn, label in [('notes_base', None, 'base notes SEMUA (641 kolom)'),
                           ('notes_base', 40,  'base notes TOP-40 saja'),
                           ('accords', 30,     'accords TOP-30'),
                           ('accords', None,   'accords SEMUA (81 kolom)')]:
    ser = d[kolom].apply(parse)
    if topn:
        cnt = Counter()
        for x in ser:
            cnt.update(x.keys())
        keep = {k for k, _ in cnt.most_common(topn)}
        ser = ser.apply(lambda x: {k: v for k, v in x.items() if k in keep})
    dv = DictVectorizer(sparse=False)
    M = dv.fit_transform(list(ser))
    X = pd.DataFrame(M)
    X['year'] = d['year'].fillna(d['year'].median()).values
    X['log_votes'] = np.log1p(d['vote_count']).values
    X = pd.concat([X, pd.get_dummies(d['gender'], prefix='g').reindex(
        columns=['g_male', 'g_female', 'g_unisex'], fill_value=0)], axis=1)
    X.columns = X.columns.astype(str)

    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"--- {label}  ({X.shape[1]} fitur)")
    for nama, m in [('Ridge', Ridge(alpha=1.0)),
                    ('RandomForest', RandomForestRegressor(n_estimators=150, random_state=42, n_jobs=-1)),
                    ('GradBoosting', GradientBoostingRegressor(random_state=42))]:
        m.fit(Xtr, ytr)
        p = m.predict(Xte)
        print(f"    {nama:14s} MAE {mean_absolute_error(yte,p):.3f} | RMSE {np.sqrt(mean_squared_error(yte,p)):.3f} | R2 {m.score(Xte,yte):+.3f} | R2train {m.score(Xtr,ytr):+.3f}")
    print()
