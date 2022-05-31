import DecisionTree as DecisionTree
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder


def female_tshirt():

    dataset = pd.read_csv(r'../csv/modified_female_tshirts.csv')
    dataset.loc[:, 'gender'] = 1

    X_female = dataset.iloc[0:, 2:5].values
    Y_female = dataset.iloc[0:, 0:1].values

    X_train_female, Y_train_female,  X_test_female, Y_test_female = train_test_split(X_female, Y_female, test_size=0.5, random_state=0)

    decision_tree_female = DecisionTreeRegressor()

    decision_tree_female.fit(X_train_female, Y_train_female)
    decision_tree_female.fit(X_test_female, Y_test_female)

    #y_predict_female = decision_tree_female.predict(X_test_female).reshape((-1, 1))

    #r_square = r2_score(Y_test_female, y_predict)

    return decision_tree_female


def male_tshirt():

    dataset = pd.read_csv(r'../csv/modified_male_tshirts.csv')
    dataset.loc[:, 'gender'] = 0

    X_male = dataset.iloc[0:, 2:5].values
    Y_male = dataset.iloc[0:, 0:1].values

    X_train_male, Y_train_male,  X_test_male, Y_test_male = train_test_split(X_male, Y_male, test_size=0.5, random_state=0)

    decision_tree_male = DecisionTreeRegressor()

    decision_tree_male.fit(X_train_male, Y_train_male)
    decision_tree_male.fit(X_test_male, Y_test_male)

    #y_predict_male = decision_tree_male.predict(X_test_male).reshape((-1, 1))
    #r_square = r2_score(Y_test_male, y_predict)

    return decision_tree_male


if __name__ == '__main__':
    female_tshirt()
    male_tshirt()


'''    
    X_train_male1 = np.reshape(X_train_male, (-1, 1))
    Y_train_male1 = np.reshape(Y_train_male, (-1, 1))

    X_test_male1 = np.reshape(X_test_male, (-1, 1))
    Y_test_male1 = np.reshape(Y_test_male, (-1, 1))
    
    transform_y_predict = y_predict.reshape((-1, 1))
'''
