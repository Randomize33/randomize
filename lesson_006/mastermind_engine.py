import random

number=[]
move=0

def think_number():
    for counter in range (0,4):
        while len(number) < 4:
            numeral=(random.randint(0, 9))
            if (counter == 0 and numeral == 0) or (numeral in number):
                continue
            else:
                number.append(numeral)

def сheck_number(quessed):
    bull=0
    cow=0
    for counter in range(0,4):
        if int(quessed[counter]) == number[counter]:
            bull=bull+1
        elif int(quessed[counter]) in number:
            cow=cow+1
    return (bull,cow)

def change_gamer(names,total_gamers,move):
    global gamer
    if move==total_gamers:
        move=0
        gamer=names[move]
    else:
        gamer=names[move]
    return (gamer,move+1)



