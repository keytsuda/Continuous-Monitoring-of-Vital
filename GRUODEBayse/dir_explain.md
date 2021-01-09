

C:\Users\182214\Documents\gru_ode_bayes-master
論文コード（モデルの回帰・分類の層に中間層を加えた）


E:\Data\Private\MIMIC_III\physionet.org
ソースデータ


E:\Data\Private\MIMIC_III\mimic_csv
mimic作業用フォルダ


E:\Data\Private\MIMIC_III\mimic_csv\Clean_data
前処理したソースと学習したモデルのファイル、学習ログ

E:\Data\Private\MIMIC_III\mimic_csv\Clean_data\Logs
ここからtensorboardを起動すると、学習の経過が追えるようになっている。

E:\Data\Private\MIMIC_III\mimic_csv\Clean_data/mimic_gruode.py
コマンドラインから実行するとモデルを学習する
- ファイル内の、ソースファイルのアドレスをPCに合うように変更
-　params_dict["lambda"]>0にすると死亡予測を行う

E:\Data\Private\MIMIC_III\mimic_csv\Clean_data\cross_val_gruODE_myuse.py
5fold用に作成したpyファイル
実際には論文コードは5foldできていないのでscikitでやってあげないといけない

trained_model_test.ipynb
学習したモデルを動かしている


E:\Data\Private\MIMIC_III\mimic_csv\MIMIC
モデルを使った予測の観測や潜在変数の調査、統計的な分析など
このフォルダ内に藤森さんが書いたスクリプト類が主にある。
今回作成したスクリプトの作業ディレクトリはClean_dataとなっている。

retrieve_ latent_variables.ipynb
retrieve_ latent_variables-Copy1.ipynb
DimComp_retrieve_ latent_variables.ipynb
学習したモデルで潜在変数を取得して観察する。ICDについて観察した。
ここだけleakageあり、潜在変数の次元圧縮などで可視化もあり。
ICDの大分類でもPlotしている。上手く別れないか試行錯誤した。

make_GRUODE_dataset.ipynb
time binごと、それぞれの患者ごとに縦積みで記載。
列名にパラメータと値の有無のマスクがついている。

makeGRUODE_tags_and_covs.ipynb
死亡タグ、診断のone-hotを作成。

他、頭が小文字のものはすべて、大文字が一部（下記）が藤森さん作成。
DIAGNOSES_Stats.ipynb
Precision_test.ipynb
LabEvents-Copy1.ipynb



