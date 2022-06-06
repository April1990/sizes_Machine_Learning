import numpy as np
from sklearn import *
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder


def shirts_tshirt(file_to_read):

    dataset = pd.read_csv(file_to_read)
    for column in dataset.columns:
        if dataset[column].dtype == type(object):

            label_encoder = LabelEncoder()
            dataset[column] = label_encoder.fit_transform(dataset[column])

    x = dataset.iloc[0:, 0:2].values
    y1 = dataset.iloc[0:, -1].values
    y = np.reshape(y1, (-1, 1))

    X_train, Y_train,  X_test, Y_test = train_test_split(x, y, test_size=0.5, random_state=0)

    linear_regressor = LinearRegression()
    linear_regressor.fit(X_train, Y_train)

    predictions = linear_regressor.predict(X_test)

    r_square = r2_score(Y_test, predictions)

    pred = linear_regressor.predict([[152, 45]])

    return pred


if __name__ == '__main__':
    shirts_tshirt(r'../csv/modified_female_shirts.csv')

'''
    for column in dataset.columns:
        if dataset[column].dtype == type(object):

            label_encoder = LabelEncoder()
            dataset[column] = label_encoder.fit_transform(dataset[column])

    X_train1 = np.reshape(X_train_female, (-1, 1))
    Y_train1 = np.reshape(Y_train_female, (-1, 1))

    X_test1 = np.reshape(X_test_female, (-1, 1))
    Y_test1 = np.reshape(Y_test_female, (-1, 1))
'''
#r'../csv/modified_female_tshirts.csv'