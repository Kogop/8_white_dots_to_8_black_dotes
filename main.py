# This is a sample Python script.
from tkinter import *

import ui
from ui import *
from PyQt6.QtWidgets import QApplication, QWidget
import sys

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Игра: 8 точек")
        self.minsize(200, 200)


def get_int(event):
    get = value.get()

    print("new")
    change_dot(int(get))
    l1["text"] = "new", '\n', matrix[0], matrix[1], matrix[2], '\n', matrix[7], " ", matrix[3], '\n', matrix[6],  matrix[5], matrix[4], '\n'

matrix = [0, 0, 0, 0, 0, 0, 0, 0]
winning_strategy = [0, 4, 2, 6, 1, 5, 7, 3]


def start_or_end(a):
    if matrix[7] != 1:
        matrix[7] = 1
    else:
        matrix[7] = 0

    if matrix[0] != 1:
        matrix[0] = 1
    else:
        matrix[0] = 0

    if a == 0:
        if matrix[1] != 1:
            matrix[1] = 1
        else:
            matrix[1] = 0

    if a == 7:
        if matrix[6] != 1:
            matrix[6] = 1
        else:
            matrix[6] = 0


def change_dot(a):
    # while (matrix.count(1) != 8 or matrix.count(0) != 8):
    for u in winning_strategy:
        # print(a)
        k = u + a
        while k >= 8:
            k = k - 8
        if k == 0 or k == 7:
            start_or_end(k)
        else:
            for o in range(0, 3):
                if matrix[k - 1 + o] != 1:
                    matrix[k - 1 + o] = 1
                else:
                    matrix[k - 1 + o] = 0
        # a = random.randint(0, 7)

        print(matrix[0], " ", matrix[1], ' ', matrix[2], '\n')
        print(matrix[7], " ", " ", ' ', matrix[3], '\n')
        print(matrix[6], " ", matrix[5], ' ', matrix[4], '\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # change_dot(int(input()))
    root = Root()

    value = IntVar()
    b1 = Button(text="ok")
    l1 = Label(text="white")
    e1 = Entry(textvariable=value)

    b1.bind('<Button-1>', get_int)

    l1.pack()
    e1.pack()
    b1.pack()

    root.mainloop()

    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exec()
    ui.Ui_MainWindow.setupUi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
