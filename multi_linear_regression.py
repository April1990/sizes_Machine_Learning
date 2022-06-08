import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, LabelBinarizer

dataset = pd.read_csv(r'csv/modified_male_female.csv')
for column in dataset.columns:
    if dataset[column].dtype == type(object):
        label_encoder = LabelEncoder()
        dataset[column] = label_encoder.fit_transform(dataset[column])

x = dataset.drop('size', axis=1).values
y = dataset['size'].values


X_train, Y_train,  X_test, Y_test = train_test_split(x, y, test_size=0.5, random_state=0)

linear_regressor = LinearRegression()
linear_regressor.fit(X_train, Y_train)


def main():
    height1 = input("Enter your height (in cm): ")
    height = int(height1)
    weight1 = input("Enter your weight (in KG): ")
    weight = int(weight1)
    print('Your gender? M/F')
    gender1 = input('Press 1 for Male or 0 for Female: ')
    gender = int(gender1)

    trans_variable = np.array([[height, weight, gender]])
    pred_size = linear_regressor.predict(trans_variable)
    pred_size = str(pred_size)
    print(pred_size)


if __name__ == '__main__':
    main()
