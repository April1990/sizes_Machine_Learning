import LinearRegression
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from machine_learning_models import tkinter_templates

dataset = pd.read_csv(r'../csv/modified_female_shorts.csv')
dataset.loc[:, 'Gender'] = 1

X = dataset.iloc[0:, 9:12].values
Y = dataset.iloc[0:, 0:9].values

X_train, Y_train, X_test, Y_test = train_test_split(X, Y, test_size=0.4, random_state=0)

X_train1 = np.reshape(X_train, (-1, 1))
Y_train1 = np.reshape(Y_train, (-1, 1))

X_test1 = np.reshape(X_test, (-1, 1))
Y_test1 = np.reshape(Y_test, (-1, 1))

linear_regressor = LinearRegression()
linear_regressor.fit(X_train1, Y_train1)


def female_tshirt_prediction():
    height1 = entry1.get()
    height = int(height1)

    weight1 = entry2.get()
    weight = int(weight1)

    gender1 = entry3.get()
    gender = int(gender1)

    transform_variables = np.array([[height, weight, gender]])
    predict_size = linear_regressor.predict(transform_variables)
    predict_size = str(predict_size)

    label1 = Label(window, text=predict_size, fg='red', font=('Courier', 25))
    label1.pack()

    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)


if __name__ == '__main__':
    female_tshirt_prediction()




'''
    #this is to convert or transform the datatype if it is object it will transform to a numeric value.
    #for example Gender is either female or male. it will convert into numeric either 1 or 0.
    for column in dataset.columns:
        if dataset[column].dtype == type(object):

            label_encoder = LabelEncoder()
            dataset[column] = label_encoder.fit_transform(dataset[column])
'''
'''
y_predic = linear_regressor.predict(X_test1)
r_square = r2_score(Y_test1, y_predic)
'''
