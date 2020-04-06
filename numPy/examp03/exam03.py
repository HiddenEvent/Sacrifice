import numpy as np
import pandas as pd

df_time_series = pd.read_csv("./Air.csv")
df_time_series["step"] = range(len(df_time_series))
# row에 해당하는 index까지의 합
df_time_series["cum_pass"] = df_time_series["#Passengers"].cumsum()
# row에 해당하는 index까지 가장 큰값을 추출
df_time_series["cum_max"] = df_time_series["#Passengers"].cummax()
# row에 해당하는 index까지 가장 작은값을 추출
df_time_series["cum_min"] = df_time_series["#Passengers"].cummin()

# 년,월 나누기
temp_date = df_time_series["Month"].map(lambda x: x.split("-"))
temp_date = np.array(temp_date.values.tolist())
df_time_series["year"] = temp_date[:,0]
df_time_series["month"] = temp_date[:,1]

# diff 이전 값과 현재값의 차이를 알려준다.
df_time_series["diff"] = df_time_series["#Passengers"].diff().fillna(0)

#  pct_change 이전 값과 현재값의 차이를 %로 나타냄
df_time_series["pct"] =  df_time_series["#Passengers"].pct_change().map(lambda x : x*100).map(lambda x: " %.2f" % x)

print(df_time_series.groupby(["year"]).sum())