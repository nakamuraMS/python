import pandas as pd
# 以下のデータを使用
# https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200521&tstat=000001011777&cycle=0&tclass1=000001094741&stat_infid=000031523105
df = pd.read_csv("c03.csv", sep="," ,encoding="SHIFT-JIS")
print(df.dropna())