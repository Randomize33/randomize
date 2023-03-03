# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
#help(sd)
#center=sd.get_point(100,100)
#radius=50
#width=2
#for _ in range(3):
#    sd.circle(center_position=center,radius=radius, width=width)
#    radius += 5

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def buble(point, step):
    radius=50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)

#buble(sd.get_point(300,300),5)

# Нарисовать 10 пузырьков в ряд

#for x in range(100,1010,100):
#    buble(sd.get_point(x,100),5)
# Нарисовать три ряда по 10 пузырьков
#for x in range(100,1010,100):
#    for y in range (100,301,100):
#        buble(sd.get_point(x,y),5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range (1,101,1):
    point=sd.random_point()
    buble(point,5)
print(random.randint)
sd.pause()


