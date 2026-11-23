# %% [markdown]
# # 03 - Pembagian Data
# Data dibagi 80 persen latih dan 20 persen uji dengan random_state tetap.

# %%
import pandas as pd
import json
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split

ROOT = Path.cwd().parent if Path.cwd().name == "notebook" else Path.cwd()
DATA = ROOT / "data"

clean = pd.read_csv(DATA / "clean.csv")
info = json.load(open(DATA / "feature_columns.json"))
fitur = info["kolom_fitur"]

X = clean[fitur].astype("float32")
y = clean["longevity_avg"].astype("float32")

print("Baris :", X.shape[0])
print("Fitur :", X.shape[1])

# %%
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Latih :", X_train.shape, "| Uji:", X_test.shape)
print("Rata-rata target latih :", round(float(y_train.mean()), 3))
print("Rata-rata target uji   :", round(float(y_test.mean()), 3))

# %%
# Baseline, selalu menebak nilai rata-rata data latih
from sklearn.metrics import mean_absolute_error

tebakan = np.full(len(y_test), float(y_train.mean()))
print("MAE baseline:", round(mean_absolute_error(y_test, tebakan), 3))

# %%
X_train.to_csv(DATA / "X_train.csv", index=False)
X_test.to_csv(DATA / "X_test.csv", index=False)
y_train.to_csv(DATA / "y_train.csv", index=False)
y_test.to_csv(DATA / "y_test.csv", index=False)

print("Tersimpan: X_train, X_test, y_train, y_test")
