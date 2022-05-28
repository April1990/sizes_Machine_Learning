from tkinter import *

window = Tk()


def tkinter_window():
    window.geometry('600x700')
    window.title('Template Window')


def height_label():
    label1 = Label(window, text='Please enter your height in cm')
    label1.pack()
    height = StringVar()
    height.set('')

    entry1 = Entry(window, textvariable=height, fg='green', font=('Courier', 25))
    return entry1


def weight_label():
    label2 = Label(window, text='Please enter your weight in kg')
    label2.pack()
    weight = StringVar()
    weight.set('')

    entry2 = Entry(window, textvariable=weight, fg='green', font=('Courier', 25))
    entry2.pack()


def gender_label():
    label3 = Label(window, text='Please enter your weight in kg')
    label3.pack()
    gender = StringVar()
    gender.set('')

    entry3 = Entry(window, textvariable=gender, fg='green', font=('Courier', 25))
    entry3.pack()


