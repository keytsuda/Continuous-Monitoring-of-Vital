import os
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold,train_test_split


csv_path = "D:/mimic_iii/clean_data/GRU_ODE_Dataset.csv"
N = pd.read_csv(csv_path)["ID"].nunique()
Nfold = 5

## train test split
tar_idx, test_idx = train_test_split(np.arange(N), test_size=0.1)

## 5fold (train, validation split)
kf = KFold(n_splits=Nfold)
kf.get_n_splits(tar_idx)

i = 0

for t_idx, v_idx in kf.split(tar_idx):
    
    train_idx, val_idx = tar_idx[t_idx], tar_idx[v_idx]
    fold_dir = f"D:/mimic_iii/clean_data/fold_idx_{i}/"
    if not os.path.exists(fold_dir):
        os.makedirs(fold_dir)
    
    np.save(fold_dir+"train_idx.npy",train_idx)
    np.save(fold_dir+"val_idx.npy",val_idx)
    np.save(fold_dir+"test_idx.npy",test_idx)
    
    i += 1

