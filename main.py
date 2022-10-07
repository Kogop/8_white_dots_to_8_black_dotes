# This is a sample Python script.
import random
from tkinter import *


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Игра: восемь точек")
        self.minsize(800, 600)





l = [0, 0, 0, 0, 0, 0, 0, 0]
winning_strategy = [0, 4, 2, 6, 1, 5, 7, 3]


def startORend(a):
    if (l[7] != 1):
        l[7] = 1
    else:
        l[7] = 0

    if (l[0] != 1):
        l[0] = 1
    else:
        l[0] = 0

    if a == 0:
        if (l[1] != 1):
            l[1] = 1
        else:
            l[1] = 0

    if a == 7:
        if (l[6] != 1):
            l[6] = 1
        else:
            l[6] = 0


def change_dot(a):
    # while (l.count(1) != 8 or l.count(0) != 8):
    for u in winning_strategy:
        # print(a)
        k = u + a
        while k >= 8:
            k = k - 8
        if k == 0 or k == 7:
            startORend(k)
        else:
            for o in range(0, 3):
                if l[k - 1 + o] != 1:
                    l[k - 1 + o] = 1
                else:
                    l[k - 1 + o] = 0
        # a = random.randint(0, 7)

        print(l[0], " ", l[1], ' ', l[2], '\n')
        print(l[7], " ", " ", ' ', l[3], '\n')
        print(l[6], " ", l[5], ' ', l[4], '\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    change_dot(int(input()))
    root = Root()
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
