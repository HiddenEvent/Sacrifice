import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):
    result = np.arange(n ** 2, dtype=dtype).reshape(n, n)
    return result


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 0:
        result = np.zeros(shape=shape, dtype=dtype)
    return result


# zero_or_one_or_empty_ndarray((3,3))

def change_shape_of_ndarray(X, n_row):
    result = X.flatten() if n_row == 1 else X.reshape(n_row, -1)
    return result


X = np.ones((32, 32), dtype=np.int)
change_shape_of_ndarray(X, 4)


def concat_ndarray(X_1, X_2, axis):
    # 가장중요!! 백터형태 데이터인지 확인하는 방법 ndim =1
    try:
        if X_1.ndim == 1:
            X_1 = X_1.reshape(1, -1)
        if X_2.ndim == 1:
            X_2 = X_2.reshape(1, -1)
        result = np.concatenate((X_1, X_2), axis=axis)
        return result
    except ValueError as e:
        return False


X_1 = np.ones(8)
X_2 = np.ones(8)
concat_ndarray(X_1, X_2, 1)


def normalize_ndarray(X, axis=99, dtype=np.float32):
    X = X.astype(np.float32)
    n_row, n_column = X.shape
    if axis == 1:
        x_mean = np.mean(X, 1).reshape(n_row, -1)
        x_std = np.std(X, 1).reshape(n_row, -1)
        Z = (X - x_mean) / x_std
    if axis == 0:
        x_mean = np.mean(X, 0).reshape(1, -1)
        x_std = np.std(X, 0).reshape(1, -1)
        Z = (X - x_mean) / x_std
    if axis == 99:
        x_mean = np.mean(X)
        x_std = np.std(X)
        Z = (X - x_mean) / x_std
    return Z


X = np.arange(12, dtype=np.float32).reshape(4, 3)
normalize_ndarray(X)


def save_ndarray(X, filename="test.npy"):
    pass


def boolean_index(X, condition):
    result = eval("X" + condition)
    return np.where(result)


X = np.arange(32, dtype=np.float32)
condition = ">3"
boolean_index(X, condition)


def find_nearest_value(X, target_value):
    distance_list = X - target_value
    abs_replace = abs(distance_list)
    result = X[np.argmin(abs_replace)]
    return result
X = np.random.uniform(0, 1, 5)
target_value = 0.3
find_nearest_value(X, target_value)

def get_n_largest_values(X, n):
    X_desc = np.argsort(X)[::-1] # 값이 큰 순서대로 리스트에 인덱스로 바꿔 리턴해줌
    result = X[X_desc][:n]
    return result
X = np.random.uniform(0,1,5)
get_n_largest_values(X, 3)