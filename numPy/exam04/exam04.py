import numpy as np
import pandas as pd

patent = pd.read_csv("./sea_managing_raw.csv",encoding="cp949")
# null이 있는지 확인
patent["출원번호"].isnull().sum()

# 출원번호 분류기호 뽑아내자!
df_patent = patent[["출원번호","Original US Class All[US]"]]

# numpy를 안쓰고 tolist로 바꾼 이유는 split 했을 경우 크기가 일정하지 않기 때문에...
edge_list = []
for row in zip(df_patent["출원번호"], df_patent["Original US Class All[US]"].map(lambda x: x.split("|")).tolist()):
    for value in row[1]:
        edge_list.append([row[0], value.strip()]) # strip은 양쪽 공백 제거!! 엔터제거!!

# list를 pandas 형태로 만들어 주기
df_edge_list = pd.DataFrame(edge_list)

# rating값을 넣어 matrix 변환
df_edge_list["rating"] = 1
print(df_edge_list.groupby([0,1])["rating"].sum().unstack().fillna(0))