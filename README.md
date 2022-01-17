# 小測驗
題目：
到政府開放資料平台下載台股個股日成交資訊：https://data.gov.tw/dataset/11549
使用kmeans將資料做分群分成10個類別。
(使用套件不限、可以查資料)

# 解題概念
1. 下載資料：確認格式，檢查資料、補空值。
2. 將需要的資料欄位轉為nparray。
3. 使用sklearn.cluster.KMeans來實作分群。
4. 將分群結果整理為pandas DataFrame後輸出為csv檔。

### 參考資料
1. [sklearn.cluster.KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
2. https://ithelp.ithome.com.tw/articles/10242867
3. https://ithelp.ithome.com.tw/articles/10187314
4. https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html

