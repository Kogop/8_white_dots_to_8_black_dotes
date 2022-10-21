# This is a sample Python script.
from tkinter import *
from typing import List, Any
import random


# import ui

# from PyQt6.QtWidgets import QApplication, QWidget


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Игра: 8 точек")
        self.minsize(300, 300)


def get_dots(event):
    place_get1 = place_value.get()
    # amount_get = amount_value.get()
    print("new")
    place_get2 = StrIntoList(place_get1)
    print(place_get2)
    solve(place_get2)
    place_get2.clear()


def ltext(li):
    l1["text"] = "new", '\n', li[0], li[1], li[2], '\n', li[7], " ", li[3], '\n', li[6], li[5], li[4], '\n'


matrix = [0, 0, 0, 0, 0, 0, 0, 0]
winning_strategy = [0, 4, 2, 6, 1, 5, 7, 3]
newList: list[Any] = []


def StrIntoList(a):
    for u in a:
        newList.append(int(u))
        # print(newList)
    return newList


def solve(a):
    amount = a.count(1)
    print(amount)
    match amount:
        case 0:
            change_dot_0(random.randint(0, 7), a)
        case 1:
            change_dot_1(a.index(1), a)
        case 2, 3, 4, 5, 6, 7:
            change_dot_any(a)
        case _:
            print("jopa")


def start_or_end(a, li):
    if li[7] != 1:
        li[7] = 1
    else:
        li[7] = 0

    if li[0] != 1:
        li[0] = 1
    else:
        li[0] = 0

    if a == 0:
        if li[1] != 1:
            li[1] = 1
        else:
            li[1] = 0

    if a == 7:
        if li[6] != 1:
            li[6] = 1
        else:
            li[6] = 0


def change_dot_1(x, li):
    # matrix = [0, 0, 0, 0, 0, 0, 0, 0]
    # if li[x] != 1:
    #     li[x] = 1
    # else:
    #     li[x] = 0
    win_strat_1 = [1, 4, 7]
    for u in win_strat_1:
        k = u + x
        while k >= 8:
            k = k - 8
        if k == 0 or k == 7:
            start_or_end(k, li)
        else:
            for o in range(0, 3):
                if li[k - 1 + o] != 1:
                    li[k - 1 + o] = 1
                else:
                    li[k - 1 + o] = 0
            # a = random.randint(0, 7)

        print(li[0], " ", li[1], ' ', li[2], '\n')
        print(li[7], " ", " ", ' ', li[3], '\n')
        print(li[6], " ", li[5], ' ', li[4], '\n')
    ltext(li)


# matrix = [0, 0, 0, 0, 0, 0, 0, 0]
def change_singe_dot(k, li):
    while k >= 8:
        k = k - 8
    if k == 0 or k == 7:
        start_or_end(k, li)
    else:
        for o in range(0, 3):
            if li[k - 1 + o] != 1:
                li[k - 1 + o] = 1
            else:
                li[k - 1 + o] = 0
    # a = random.randint(0, 7)


# solve with 0 placed
def change_dot_0(a, li):
    # while (matrix.count(1) != 8 or matrix.count(0) != 8):

    for u in winning_strategy:
        # print(a)
        k = u + a
        while k >= 8:
            k = k - 8
        if k == 0 or k == 7:
            start_or_end(k, li)
        else:
            for o in range(0, 3):
                if li[k - 1 + o] != 1:
                    li[k - 1 + o] = 1
                else:
                    li[k - 1 + o] = 0
        # a = random.randint(0, 7)

        print(li[0], " ", li[1], ' ', li[2], '\n')
        print(li[7], " ", " ", ' ', li[3], '\n')
        print(li[6], " ", li[5], ' ', li[4], '\n')
    ltext(li)


def change_dot_any(a):
    while a.count(1) != 8 or a.count(0) != 8:
        for u in a:
            counter = 0
            if u == 1 and a[u + 1] == 1:
                change_singe_dot(a, u)
            counter = counter + 1
    # ltext(a)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # change_dot(int(input()))
    root = Root()

    # amount_value = IntVar()
    place_value = StringVar()
    b1 = Button(text="ok")
    l1 = Label(text="matrix")
    # l2 = Label(text="how much 1?")
    l3 = Label(text="type in whole circle")
    # e1 = Entry(textvariable=amount_value)
    e2 = Entry(textvariable=place_value)
    b1.bind('<Button-1>', get_dots)

    l1.pack()
    # l2.pack()
    # e1.pack()
    l3.pack()
    e2.pack()
    b1.pack()
    # hhhhh
    root.mainloop()
    #
    # app = QApplication()
    # window = QWidget()
    # window.show()
    # app.exec()
    # ui.Ui_MainWindow.setupUi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
