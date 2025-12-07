import random
import os

dimension = 4
if dimension == 1:
    exit("the dimension must be > 1")

max_size = len(str(dimension ** 2 - 1))
spaces = f"{' ' * max_size}"

def create_right_field(dimension):
    values = [" "]
    for i in range((dimension ** 2 - 1), 0, -1):
        values.append(i)
    right_field = []
    for i in range(dimension):
        raw = []
        for j in range(dimension):
            if len(str(values[-1])) < max_size:
                raw.append(f"{' ' * (max_size - len(str(values[-1])))}{values[-1]}")
            else:
                raw.append(str(values[-1]))
            values.pop()
        right_field.append(raw)
    return right_field


right_field, field = create_right_field(dimension), create_right_field(dimension)

def get_indexes(field, rand: bool):
    if rand == False:
        choice = int(input("Number -> "))
        for i in range(len(field)):
            for j in range(len(field[i])):
                if field[i][j] != spaces:
                    if choice == int(field[i][j]):
                        num = [i, j]
                else:
                    blank = [i, j]
    else:
        for i in range(len(field)):
            for j in range(len(field[i])):
                if field[i][j] == spaces:
                    blank = [i, j]
                    flag = True
                    while flag != False:
                        rand = random.randint(0, 3)
                        if rand == 0:
                            num = [blank[0], blank[1]+1]
                        elif rand == 1:
                            num = [blank[0], blank[1]-1]
                        elif rand == 2:
                            num = [blank[0]+1, blank[1]]
                        elif rand == 3:
                            num = [blank[0]-1, blank[1]]
                        if num[0] >= 0 and num[0] <= dimension-1 and num[1] >= 0 and num[1] <= dimension-1:
                            choice = field[num[0]][num[1]]
                            flag = False
    return num, blank, choice

def logic(field, rand):
    num, blank, choice = get_indexes(field, rand)
    if num[0] == blank[0]:
        if abs(num[1] - blank[1]) == 1:
            field[num[0]][num[1]] = spaces
            if len(str(choice)) < max_size:
                choice = f"{' ' * (max_size - len(str(choice)))}{choice}"
            else:
                choice = str(choice)
            field[blank[0]][blank[1]] = choice
    elif num[1] == blank[1]:
        if abs(num[0] - blank[0]) == 1:
            field[num[0]][num[1]] = spaces
            if len(str(choice)) < max_size:
                choice = f"{' ' * (max_size - len(str(choice)))}{choice}"
            else:
                choice = str(choice)
            field[blank[0]][blank[1]] = choice

def create_random_field(field):
    for i in range(dimension ** 4):
        logic(field, True)


create_random_field(field)

def print_field(field):
    os.system("clear")
    for i in field:
        print(*i)


while field != right_field:
    try:
        print_field(field)
        logic(field, False)
    except (UnboundLocalError, ValueError):
        pass
else:
    print_field(field)
    print("Win!")

