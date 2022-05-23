from tkinter import *


def tkinter_window():
    window = Tk()
    window.geometry('600x700')
    window.title('Template Window')

    label1 = Label(window, text='Please enter your height in cm')
    label1.pack()
    height = StringVar()
    height.set('')

    entry1 = Entry(window, textvariable=height, fg='green', font=('Courier', 25))
    entry1.pack()

    label2 = Label(window, text='Please enter your weight in kg')
    label2.pack()
    weight = StringVar()
    weight.set('')

    entry2 = Entry(window, textvariable=weight, fg='green', font=('Courier', 25))
    entry2.pack()

    label3 = Label(window, text='Please enter your weight in kg')
    label3.pack()
    gender = StringVar()
    gender.set('')

    entry3 = Entry(window, textvariable=gender, fg='green', font=('Courier', 25))
    entry3.pack()


