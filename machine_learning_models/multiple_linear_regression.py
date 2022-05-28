import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def readfile_shorts():
    dataset = pd.read_csv(r'../csv/modified_female_shorts.csv')
    dataset.loc[:, 'Gender'] = 1

    X = dataset.iloc[0:, 0:9].values
    Y = dataset.iloc[0:, 9:12].values
    return X, Y


def split_data():
    X, Y = readfile_shorts()
    X_train, Y_train, X_test, Y_test = train_test_split(X, Y, test_size=0.4, random_state=0)
    return X_train, Y_train, X_test, Y_test


def model_train():
    X_train, Y_train, X_test, Y_test = split_data()
    
    X_train1 = np.reshape(X_train, (-1, 1))
    Y_train1 = np.reshape(Y_train, (-1, 1))

    X_test1 = np.reshape(X_test, (-1, 1))
    Y_test1 = np.reshape(Y_test, (-1, 1))

    linear_regression = LinearRegression()
    linreg_train = linear_regression.fit(X_train, Y_train)
    linreg_test = linear_regression.fit(X_test1, Y_test1)
    return linreg_train, linreg_test


if __name__ == '__main__':
    readfile_shorts()
    split_data()
    model_train()
