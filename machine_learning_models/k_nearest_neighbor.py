import numpy as np
from sklearn import *
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder


dataset = pd.read_csv(r'../csv/modified_female_shirts.csv')
dataset.loc[:, 'gender'] = 1

x = dataset.iloc[0:, 1:4].values
y = dataset.iloc[0:, :1].values

X_train_female, Y_train_female,  X_test_female, Y_test_female = train_test_split(x, y, test_size=0.5, random_state=0)
