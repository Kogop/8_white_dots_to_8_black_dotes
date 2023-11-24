from typing import List, Any
import random

matrix = [0, 0, 0, 0, 0, 0, 0, 0]
winning_strategy = [0, 4, 2, 6, 1, 5, 7, 3]
winning_strategy_2 = [0, 1, 2, 3, 4, 5, 6, 7]
# newList: list[Any] = []


def ltext(li):
    print(li)
    if li:
        ftext = f"new \n {li[0]}, {li[1]}, {li[2]} \n {li[7]},  , {li[3]} \n {li[6]}, {li[5]}, {li[4]}, \n"
        # text = "".join(("new", '\n', li[0], li[1], li[2], '\n', li[7], " ", li[3], '\n', li[6], li[5], li[4], '\n'))
        # l5["text"] = ftext
        return ftext
        # l5["text"] = "new", '\n', li[0], li[1], li[2], '\n', li[7], " ", li[3], '\n', li[6], li[5], li[4], '\n'
    else:
        return ""
        # l5["text"] = ""


def StrIntoList(a):
    newList = []
    for u in a:
        newList.append(int(u))
        print(newList)
    return newList


def solve(a):
    # print(a)
    amount = a.count(1)
    # print(amount)
    match amount:
        case 0:
            return ltext(change_dot_0(random.randint(0, 7), a))
        case 1:
            return ltext(change_dot_1(a.index(1), a))
        case _:
            print("jopa")
            return ltext(change_dot_any(a))


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
    # ltext(li)
    return li


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
    # ltext(li)
    return li


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
            return change_dot_0(0, li)
            # break
        if li.count(1) == 1:
            return change_dot_1(li.index(1), li)
            # break
        for p in range(1, 7):  # change 2 consecutive 1 into 0 and 0 on the side to 1
            if li[p - 1] == 0 and li[p] == 1 and li[p + 1] == 1:
                change_singe_dot(p, li)
            if li[p - 1] == 1 and li[p] == 1 and li[p + 1] == 0:
                change_singe_dot(p, li)
            if li[p - 1] == 1 and li[p] == 0 and li[p + 1] == 1:
                change_singe_dot(p, li)
        if li.count(1) == 0:
            return change_dot_0(0, li)
            # break
        if li.count(1) == 1:
            return change_dot_1(li.index(1), li)
            # break
        for p in range(1, 7):  # change 1 consecutive 1 into 0 and 2 0 on the side to 1
            if li[p - 1] == 0 and li[p] == 0 and li[p + 1] == 1:
                change_singe_dot(p, li)
            # if li[p - 1] == 1 and li[p] == 0 and li[p + 1] == 1:
            # change_singe_dot(p, li)
        if li.count(1) == 0:
            return change_dot_0(0, li)
            # break
        if li.count(1) == 1:
            return change_dot_1(li.index(1), li)
            # break
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
                return change_dot_1(1, li)
                # break
            if li[7] == 1 and li[0] == 0 and li[1] == 1:
                return change_singe_dot(0, li)
            print(li[0], " ", li[1], ' ', li[2], '\n')
            print(li[7], " ", " ", ' ', li[3], '\n')
            print(li[6], " ", li[5], ' ', li[4], '\n')
        # ltext(li)
