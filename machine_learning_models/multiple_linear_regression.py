import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder


def female_tshirt():

    dataset = pd.read_csv(r'../csv/modified_female_tshirts.csv')
    dataset.loc[:, 'gender'] = 1

    X_female = dataset.iloc[0:, 2:5].values
    Y_female = dataset.iloc[0:, 0:1].values

    X_train_female, Y_train_female,  X_test_female, Y_test_female = train_test_split(X_female, Y_female, test_size=0.5, random_state=0)

    linear_regressor_female = LinearRegression()

    linear_regressor_female.fit(X_train_female, Y_train_female)
    linear_regressor_female.fit(X_test_female, Y_test_female)

    y_predict_female = linear_regressor_female.predict(X_test_female).reshape((-1, 1))

    r_square = r2_score(Y_test_female, y_predict_female)

    return r_square


def male_tshirt():

    dataset = pd.read_csv(r'../csv/modified_male_tshirts.csv')
    dataset.loc[:, 'gender'] = 0

    X_male = dataset.iloc[0:, 2:5].values
    Y_male = dataset.iloc[0:, 0:1].values

    X_train_male, Y_train_male,  X_test_male, Y_test_male = train_test_split(X_male, Y_male, test_size=0.5, random_state=0)

    linear_regressor_male = LinearRegression()

    linear_regressor_male.fit(X_train_male, Y_train_male)
    linear_regressor_male.fit(X_test_male, Y_test_male)

    y_predict_male = linear_regressor_male.predict(X_test_male).reshape((-1, 1))
    r_square = r2_score(Y_test_male, y_predict_male)

    return r_square


if __name__ == '__main__':
    female_tshirt()
    male_tshirt()




 #X = dataset.iloc[0:, 5:].values
    #Y = dataset.iloc[0:, 0:3].values

    #X = dataset.iloc[0:, 0:3].values
    #Y = dataset.iloc[0:, 5:].values

#x = np.array([]).reshape((-1, 1))

