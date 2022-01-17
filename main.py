import requests
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from io import StringIO

# 資料來源：https://data.gov.tw/dataset/11549
# 資料載點：
url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data"

response = requests.get(url)
# 載入資料
data = response.text

# 抓出個股資料的數據，轉成nparray
# data_array = np.array(data)
# print(data_array)

# DataFrame
my_string = StringIO(data)
df = pd.read_csv(my_string, header=None)
df = df.fillna(0)
# 用第一行的資料設定新的header
new_headers = df.iloc[0]
# 去掉原本的標題
df = df[1:]
# 放入新hearder
df.columns = new_headers
df_drop_name = df.drop(['證券代號', '證券名稱'], axis=1)
# print(df_drop_name)
raw_data = df_drop_name[1:]
data_array = np.asarray(raw_data)
# print(data_array)

# 用sklearn實作分群
cluster = KMeans(n_clusters=10)
cluster.fit(data_array)
# print(result)
df['labels'] = cluster.labels_
print(df)
