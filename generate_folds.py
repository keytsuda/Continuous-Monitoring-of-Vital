import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import os

# E:\Data\Private\MIMIC_III\mimic_csv\Clean_data
dir_path="E:\\Data\\Private\\MIMIC_III\\mimic_csv\\Clean_data\\"
csv_path=dir_path+"GRU_ODE_Dataset.csv"
N = pd.read_csv(csv_path)["ID"].nunique()
full_idx = np.arange(N)
Nfolds = 5

np.random.seed(432)

for fold in range(Nfolds):
    train_idx, test_idx = train_test_split(np.arange(N),test_size=0.1)
    train_idx, val_idx = train_test_split(train_idx,test_size=0.2)
    fold_dir = f"fold_idx_{fold}/"
    if not os.path.exists(fold_dir):
        os.makedirs(fold_dir)
    np.save(fold_dir+f"train_idx.npy",train_idx)
    np.save(fold_dir+f"val_idx.npy",val_idx)
    np.save(fold_dir+f"test_idx.npy",test_idx)
