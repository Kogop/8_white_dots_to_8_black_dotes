# This is a sample Python script.
from tkinter import *
from typing import List, Any
import random

# import ui

import test_functions as f
import game_function as g


# from PyQt6.QtWidgets import QApplication, QWidget


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Игра: 8 точек")
        self.minsize(400, 400)


def get_dots(event):
    l5["text"] = f.ltext(False)
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
            place_get2 = f.StrIntoList(place_get1)
            print(place_get2)
            l5["text"] = f.solve(place_get2)
            # b1["text"] = "pop"
            place_get2.clear()
    else:
        error_text("введите строку из 8 символов состоящую только из комбинаций 1 или 0")


def error_text(error):
    l2["text"] = error


def game_btn_press(num):
    match num:
        case 1:
            g.change_text(gameFrame_b1)
            g.change_text(gameFrame_b2)
            g.change_text(gameFrame_b8)
        case 2:
            g.change_text(gameFrame_b1)
            g.change_text(gameFrame_b2)
            g.change_text(gameFrame_b3)
        case 3:
            g.change_text(gameFrame_b2)
            g.change_text(gameFrame_b3)
            g.change_text(gameFrame_b4)
        case 4:
            g.change_text(gameFrame_b3)
            g.change_text(gameFrame_b4)
            g.change_text(gameFrame_b5)
        case 5:
            g.change_text(gameFrame_b4)
            g.change_text(gameFrame_b5)
            g.change_text(gameFrame_b6)
        case 6:
            g.change_text(gameFrame_b5)
            g.change_text(gameFrame_b6)
            g.change_text(gameFrame_b7)
        case 7:
            g.change_text(gameFrame_b6)
            g.change_text(gameFrame_b7)
            g.change_text(gameFrame_b8)
        case 8:
            g.change_text(gameFrame_b7)
            g.change_text(gameFrame_b8)
            g.change_text(gameFrame_b1)
        case _:
            return 0


def game_btn_press_single(num):
    match num:
        case 1:
            g.change_text(placementFrame_b1)
        case 2:
            g.change_text(placementFrame_b2)
        case 3:
            g.change_text(placementFrame_b3)
        case 4:
            g.change_text(placementFrame_b4)
        case 5:
            g.change_text(placementFrame_b5)
        case 6:
            g.change_text(placementFrame_b6)
        case 7:
            g.change_text(placementFrame_b7)
        case 8:
            g.change_text(placementFrame_b8)
        case _:
            return 0

def solve_from_this_position(str1, str2, str3, str4, str5, str6, str7, str8):
    text = f"{str1}{str2}{str3}{str4}{str5}{str6}{str7}{str8}"
    text = text.replace("pop", "0")
    text = text.replace("ok", "1")

    print(text)
    # print(f.StrIntoList(text))
    f.solve(f.StrIntoList(text))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # change_dot(int(input()))
    root = Root()

    testFrame = Frame(root, height=500, background="gray")
    testFrame.pack()
    # amount_value = IntVar()

    l1 = Label(testFrame, text="matrix")
    l1.grid(row=1, column=1)

    l3 = Label(testFrame, text="type in whole circle")
    l3.grid(row=2, column=1, columnspan=2)

    place_value = StringVar()
    e2 = Entry(testFrame, textvariable=place_value)
    e2.grid(row=3, column=1, columnspan=2)

    b1 = Button(testFrame, text="ok")
    b1.bind('<Button-1>', get_dots)
    b1.grid(row=4, column=1, columnspan=2)

    l2 = Label(testFrame, text="place for error message")
    l2.grid(row=1, column=3)

    l5 = Label(testFrame, text="")
    l5.grid(row=5, column=1)

    # another frame
    placementFrame = Frame(root, height=200, background="white")
    placementFrame.pack()

    placementFrame_b1 = Button(placementFrame, text="ok", height=2, width=3, command=lambda: game_btn_press_single(1))
    # gameFrame_b1.bind('<Button-1>')
    placementFrame_b1.grid(row=1, column=1)

    placementFrame_b2 = Button(placementFrame, text="ok", height=2, width=3, command=lambda: game_btn_press_single(2))
    # gameFrame_b2.bind('<Button-1>', get_dots)
    placementFrame_b2.grid(row=1, column=2)

    placementFrame_b3 = Button(placementFrame, text="ok", height=2, width=3, command=lambda: game_btn_press_single(3))
    # gameFrame_b3.bind('<Button-1>', get_dots)
    placementFrame_b3.grid(row=1, column=3)

    placementFrame_b4 = Button(placementFrame, text="ok", height=2, width=3, command=lambda: game_btn_press_single(4))
    # gameFrame_b4.bind('<Button-1>', get_dots)
    placementFrame_b4.grid(row=2, column=3)

    placementFrame_b5 = Button(placementFrame, text="ok", height=2, width=3, command=lambda: game_btn_press_single(5))
    # gameFrame_b5.bind('<Button-1>', get_dots)
    placementFrame_b5.grid(row=3, column=3)

    placementFrame_b6 = Button(placementFrame, text="ok", height=2, width=3, command=lambda: game_btn_press_single(6))
    # gameFrame_b6.bind('<Button-1>', get_dots)
    placementFrame_b6.grid(row=3, column=2)

    placementFrame_b7 = Button(placementFrame, text="ok", height=2, width=3, command=lambda: game_btn_press_single(7))
    # gameFrame_b7.bind('<Button-1>', get_dots)
    placementFrame_b7.grid(row=3, column=1)

    placementFrame_b8 = Button(placementFrame, text="ok", height=2, width=3, command=lambda: game_btn_press_single(8))
    # gameFrame_b8.bind('<Button-1>', get_dots)
    placementFrame_b8.grid(row=2, column=1)
    # e1 = Entry(textvariable=amount_value)

    placementFrame_btn_solve = Button(placementFrame, text="solve from this position", height=2, width=24,
                                      command=lambda: solve_from_this_position(placementFrame_b1["text"],placementFrame_b2["text"],placementFrame_b3["text"],placementFrame_b4["text"],
                                                                             placementFrame_b5["text"],placementFrame_b6["text"],placementFrame_b7["text"],placementFrame_b8["text"]))

    placementFrame_btn_solve.grid(row=4, column=1, columnspan=6)
    # frame with actual game

    second = Toplevel()
    second.title("Game itself")
    second.geometry("500x500")
    second.focus()  # useless? how do i use this shit

    # gameFrame = Frame(second, height=500, width=500, background="blue", relief="groove")
    # gameFrame.grid(rowspan=9, columnspan=9)

    gameFrame_b1 = Button(second, text="ok", height=2, width=3, command=lambda: game_btn_press(1))
    # gameFrame_b1.bind('<Button-1>')
    gameFrame_b1.grid(row=1, column=1)

    gameFrame_b2 = Button(second, text="ok", height=2, width=3, command=lambda: game_btn_press(2))
    # gameFrame_b2.bind('<Button-1>', get_dots)
    gameFrame_b2.grid(row=1, column=2)

    gameFrame_b3 = Button(second, text="ok", height=2, width=3, command=lambda: game_btn_press(3))
    # gameFrame_b3.bind('<Button-1>', get_dots)
    gameFrame_b3.grid(row=1, column=3)

    gameFrame_b4 = Button(second, text="ok", height=2, width=3, command=lambda: game_btn_press(4))
    # gameFrame_b4.bind('<Button-1>', get_dots)
    gameFrame_b4.grid(row=2, column=3)

    gameFrame_b5 = Button(second, text="ok", height=2, width=3, command=lambda: game_btn_press(5))
    # gameFrame_b5.bind('<Button-1>', get_dots)
    gameFrame_b5.grid(row=3, column=3)

    gameFrame_b6 = Button(second, text="ok", height=2, width=3, command=lambda: game_btn_press(6))
    # gameFrame_b6.bind('<Button-1>', get_dots)
    gameFrame_b6.grid(row=3, column=2)

    gameFrame_b7 = Button(second, text="ok", height=2, width=3, command=lambda: game_btn_press(7))
    # gameFrame_b7.bind('<Button-1>', get_dots)
    gameFrame_b7.grid(row=3, column=1)

    gameFrame_b8 = Button(second, text="ok", height=2, width=3, command=lambda: game_btn_press(8))
    # gameFrame_b8.bind('<Button-1>', get_dots)
    gameFrame_b8.grid(row=2, column=1)

    # l1.pack()
    # l2.pack()
    # e1.pack()
    # l3.pack()
    # e2.pack()
    # b1.pack()
    # l5.pack()

    # hhhhh

    #
    # app = QApplication()
    # window = QWidget()
    # window.show()
    # app.exec()
    # ui.Ui_MainWindow.setupUi()

    root.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
