from tkinter import *

import LinearRegression
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from tkinter_templates import tkinter
from tkinter_templates.tkinter import window


def female_tshirt_prediction():
    entry1 = tkinter.height_label()
    height1 = entry1.get()
    height = int(height1)
    entry1.delete(0, END)
    return height


def weight_tshirt_predict():
    entry2 = tkinter.weight_label()
    weight1 = entry2.get()
    weight = int(weight1)
    entry2.delete(0, END)
    return weight


def gender_tshirt_predict():
    entry3 = tkinter.gender_label()
    gender1 = entry3.get()
    gender = int(gender1)
    entry3.delete(0, END)
    return gender


def trans_variables():

    transform_variables = [[female_tshirt_prediction()]]
    transform_variables = np.array(transform_variables)
    predict_size = linear_regressor.predict(transform_variables)
    predict_size = str(predict_size)

    label1 = Label(window, text=predict_size, fg='red', font=('Courier', 25))
    label1.pack()


if __name__ == '__main__':
    female_tshirt_prediction()
    weight_tshirt_predict()
    gender_tshirt_predict()
    trans_variables()

