import DecisionTree as DecisionTree
from sklearn import *
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import DecisionTree as DecisionTree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder


def female_tshirt():
    dataset = pd.read_csv(r'../csv/modified_female_shirts.csv')
    dataset.loc[:, 'gender'] = 1

    for column in dataset.columns:
        if dataset[column].dtype == type(object):

            label_encoder = LabelEncoder()
            dataset[column] = label_encoder.fit_transform(dataset[column])

    X = dataset.iloc[0:, 3:6].values
    y = dataset.iloc[0:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.5)

    X_train1 = np.reshape(X_train, (-1, 1))
    y_train1 = np.reshape(y_train, (-1, 1))

    X_test1 = np.reshape(X_test, (-1, 1))
    y_test1 = np.reshape(y_test, (-1, 1))

    clf_dt = DecisionTreeRegressor(random_state=42)
    clf_dt = clf_dt.fit(X_train1, y_train1)
    training_sets = []

    for i in range(1, 10):
        #X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=i, test_size=0.55)
        training_sets.append([X_train1, X_test1, y_train1, y_test1])
    person = [[85, 65, 55]]
    clf_dt.predict(person)

    return person


if __name__ == '__main__':
    female_tshirt()

'''    
    X = dataset[['waist(cm)', 'height(cm)', 'weight(kg)']].values
    y = dataset[['chest(cm)']].values
    dataset.loc[:, 'gender'] = 1
'''
