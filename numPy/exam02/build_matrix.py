import numpy as np
import pandas as pd


def get_rating_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename)
    rating_matrix = df.groupby(["source","target"])["rating"].sum().unstack().fillna(0)
    return rating_matrix
filename = "./movie_rating.csv"
get_rating_matrix(filename)
# df = pd.read_csv("./movie_rating.csv")
# df = df.groupby(["source", "target"])["rating"].sum().unstack().fillna(0)
# print(df)


def get_frequent_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename)
    df["rating"] = 1  # rating column 1값으로 추가
    rating_sum = df.groupby(["source","target"])["rating"].sum() # 그룹으로 묶어 rating합계
    frequent_matrix = rating_sum.unstack().fillna(0)
    return frequent_matrix
filename = "./1000i.csv"
get_frequent_matrix(filename)