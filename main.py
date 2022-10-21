# This is a sample Python script.
from tkinter import *
from typing import List, Any
import random

#import ui

#from PyQt6.QtWidgets import QApplication, QWidget


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Игра: 8 точек")
        self.minsize(300, 300)


def get_dots(event):
    place_get1 = place_value.get()
    #amount_get = amount_value.get()
    print("new")
    place_get2 = StrIntoList(place_get1)
    print(place_get2)
    solve(place_get2)
    place_get2.clear()




    # match amount_get:
    #     case 0:
    #         change_dot_0(int(place_get1))
    #     case 1:
    #         change_dot_1(int(place_get1))
    #     case _:
    #         print("jopa")

    l1["text"] = "new", '\n', matrix[0], matrix[1], matrix[2], '\n', matrix[7], " ", matrix[3], '\n', matrix[6], matrix[5], matrix[4], '\n'


matrix = [0, 0, 0, 0, 0, 0, 0, 0]
winning_strategy = [0, 4, 2, 6, 1, 5, 7, 3]
newList: list[Any] = []

def StrIntoList(a):
    for u in a:
        newList.append(int(u))
        #print(newList)
    return newList

def solve(a):
    amount = a.count(1)
    print(amount)
    match amount:
        case 0:
            change_dot_0(random.randint(0, 7))
        case 1:
            change_dot_1(a.index('1'))
        case 2, 3, 4, 5, 6, 7:


        case _:
            print("jopa")


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



def change_dot_1(a):
    #matrix = [0, 0, 0, 0, 0, 0, 0, 0]
    if matrix[a] != 1:
        matrix[a] = 1
    else:
        matrix[a] = 0
    win_strat_1 = [1, 4, 7]
    for u in win_strat_1:
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
        print(matrix[0], " ", matrix[1], ' ', matrix[2], '\n')
        print(matrix[7], " ", " ", ' ', matrix[3], '\n')
        print(matrix[6], " ", matrix[5], ' ', matrix[4], '\n')
#matrix = [0, 0, 0, 0, 0, 0, 0, 0]
def change_singe_dot(k):
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

# solve with 0 placed
def change_dot_0(a):
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

def change_dot_any(a):
    while a.count(1) != 8 or a.count(0) != 8:
        for u in a:
            if u ==1 and u+1 == 1:
                change_singe_dot(a,)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # change_dot(int(input()))
    root = Root()

    #amount_value = IntVar()
    place_value = StringVar()
    b1 = Button(text="ok")
    l1 = Label(text="matrix")
    #l2 = Label(text="how much 1?")
    l3 = Label(text="type in whole circle")
    #e1 = Entry(textvariable=amount_value)
    e2 = Entry(textvariable=place_value)
    b1.bind('<Button-1>', get_dots)

    l1.pack()
    #l2.pack()
    #e1.pack()
    l3.pack()
    e2.pack()
    b1.pack()
#hhhhh
    root.mainloop()
    #
    # app = QApplication()
    # window = QWidget()
    # window.show()
    # app.exec()
    # ui.Ui_MainWindow.setupUi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
