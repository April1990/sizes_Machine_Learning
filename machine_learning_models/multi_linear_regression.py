from sklearn.preprocessing import LabelEncoder
from tkinter import  *
from tkinter_templates.tkinter import window
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

dataset = pd.read_csv(r'../csv/modified_male_female.csv')
for column in dataset.columns:
    if dataset[column].dtype == type(object):

        label_encoder = LabelEncoder()
        dataset[column] = label_encoder.fit_transform(dataset[column])

X = dataset.drop('size', axis = 1).values
y = dataset['size'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, test_size = .5)

linear = LinearRegression()
linear.fit(X_train, y_train)

model_predict = linear.predict(X_test)


def main():
    height1 = input("Enter your height (in cm): ")
    height = int(height1)
    weight1 = input("Enter your weight (in KG): ")
    weight = int(weight1)
    print('Your gender? M/F')
    gender1 = input('Press 1 for Male or 0 for Female: ')
    gender = int(gender1)

    trans_variable = [[height, weight, gender]]
    pred_size = linear.predict(trans_variable)
    print(pred_size)


if __name__ == '__main__':
    main()
