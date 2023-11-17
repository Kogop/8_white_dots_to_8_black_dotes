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
    ltext(False)
    error_text("")
    place_get1 = place_value.get()
    print(type(place_get1))
    if len(place_get1) == 8:
        for i in place_get1:
            # print(i)
            if i != "0" and i != "1":
                print("Only 1's and 0's, pls")
                error_text("введите строку из 8 символов состоящую только из комбинаций 1 или 0")
                place_get1 = False
                break

        # amount_get = amount_value.get()
        print("new")
        if place_get1:
            place_get2 = StrIntoList(place_get1)
            print(place_get2)
            solve(place_get2)
            b1["text"] = "pop"
            place_get2.clear()
    else:
        error_text("введите строку из 8 символов состоящую только из комбинаций 1 или 0")


def error_text(error):
    l2["text"] = error


def ltext(li):
    print(li)
    if li:
        ftext = f"new \n {li[0]}, {li[1]}, {li[2]} \n {li[7]},  , {li[3]} \n {li[6]}, {li[5]}, {li[4]}, \n"
        # text = "".join(("new", '\n', li[0], li[1], li[2], '\n', li[7], " ", li[3], '\n', li[6], li[5], li[4], '\n'))
        l5["text"] = ftext
        # l5["text"] = "new", '\n', li[0], li[1], li[2], '\n', li[7], " ", li[3], '\n', li[6], li[5], li[4], '\n'
    else:

        l5["text"] = ""


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
    # print(amount)
    match amount:
        case 0:
            change_dot_0(random.randint(0, 7), a)
        case 1:
            change_dot_1(a.index(1), a)
        case _:
            change_dot_any(a)
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
        for o in range(0, 3):  # I can do only else statement since I always start with zeros now
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


def change_dot_any(li):
    while li.count(1) != 8 or li.count(0) != 8:
        counter = 0

        if li.count(1) >= 3:  # clear any 3 consecutive 1
            # print("vsmisle")
            for p in range(1, 7):
                # print(p)
                if li[p - 1] == 1 and li[p] == 1 and li[p + 1] == 1:
                    li[p - 1] = 0
                    li[p] = 0
                    li[p + 1] = 0
            if li[7] == 1 and li[0] == 1 and li[1] == 1:
                li[7] = 0
                li[0] = 0
                li[1] = 0
            if li[6] == 1 and li[7] == 1 and li[0] == 1:
                li[6] = 0
                li[7] = 0
                li[0] = 0
        print(li)
        if li.count(1) == 0:
            change_dot_0(0, li)
            break
        if li.count(1) == 1:
            change_dot_1(li.index(1), li)
            break
        for p in range(1, 7):  # change 2 consecutive 1 into 0 and 0 on the side to 1
            if li[p - 1] == 0 and li[p] == 1 and li[p + 1] == 1:
                change_singe_dot(p, li)
            if li[p - 1] == 1 and li[p] == 1 and li[p + 1] == 0:
                change_singe_dot(p, li)
            if li[p - 1] == 1 and li[p] == 0 and li[p + 1] == 1:
                change_singe_dot(p, li)
        if li.count(1) == 0:
            change_dot_0(0, li)
            break
        if li.count(1) == 1:
            change_dot_1(li.index(1), li)
            break
        for p in range(1, 7):  # change 1 consecutive 1 into 0 and 2 0 on the side to 1
            if li[p - 1] == 0 and li[p] == 0 and li[p + 1] == 1:
                change_singe_dot(p, li)
            # if li[p - 1] == 1 and li[p] == 0 and li[p + 1] == 1:
            # change_singe_dot(p, li)
        if li.count(1) == 0:
            change_dot_0(0, li)
            break
        if li.count(1) == 1:
            change_dot_1(li.index(1), li)
            break
        if li.count(1) == 2:
            # for p in range(1, 6):
            #     if li[p] == 1 and li[p + 1] == 1 and li[p - 1] == 0:
            #         change_singe_dot(p, li)
            #         change_dot_1(li.index(1), li)
            #         break
            #     if li[p - 1] == 1 and li[p] == 1 and li[p + 1] == 0:
            #         change_singe_dot(p, li)
            #         change_dot_1(li.index(1), li)
            #         break
            if li[0] == 1 and li[7] == 1:
                li[0] = 0
                li[7] = 0
                li[1] = 1
                change_dot_1(1, li)
                break
            if li[7] == 1 and li[0] == 0 and li[1] == 1:
                change_singe_dot(0, li)
            print(li[0], " ", li[1], ' ', li[2], '\n')
            print(li[7], " ", " ", ' ', li[3], '\n')
            print(li[6], " ", li[5], ' ', li[4], '\n')
        ltext(li)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # change_dot(int(input()))
    root = Root()

    # amount_value = IntVar()
    place_value = StringVar()
    b1 = Button(text="ok")
    l1 = Label(text="matrix")
    l2 = Label(text="")
    l3 = Label(text="type in whole circle")
    # e1 = Entry(textvariable=amount_value)
    e2 = Entry(textvariable=place_value)
    b1.bind('<Button-1>', get_dots)

    l5 = Label(text="")


    l1.pack()
    l2.pack()
    # e1.pack()
    l3.pack()
    e2.pack()
    b1.pack()
    l5.pack()

    # hhhhh
    root.mainloop()
    #
    # app = QApplication()
    # window = QWidget()
    # window.show()
    # app.exec()
    # ui.Ui_MainWindow.setupUi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
