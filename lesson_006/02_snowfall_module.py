# -*- coding: utf-8 -*-
import random

import simple_draw as sd
from snowfall import paint_some_snowflake, paint_color_snowflake, move_snowflake

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
# while True:
#     #  нарисовать_снежинки_цветом(color=sd.background_color)
#     #  сдвинуть_снежинки()
#     #  нарисовать_снежинки_цветом(color)
#     #  если есть номера_достигших_низа_экрана() то
#     #       удалить_снежинки(номера)
#     #       создать_снежинки(count)
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


x_list=[]
y_list=[]
y=0
snowdrift=0
for _ in range(0, 5):
    x = random.randint(50, 550)
    y=600
    x_list.append(x)
    y_list.append(y)
    paint_some_snowflake(x, y)
while True:
    counter=0
    snowdrift=1
    for x in x_list:
        y=y_list[counter]
        if y<=snowdrift:
            y=600
            x = random.randint(50, 550)
        paint_color_snowflake(x, y, sd.background_color)
        x,y=move_snowflake(x,y)
        x_list[counter]=x
        y_list[counter]=y
        paint_some_snowflake(x, y)
        counter+=1


# for x in x_list:
#
# paint_color_snowflake(x,y,size,sd.background_color)
# x,y=move_snowflake(x,y)
# paint_color_snowflake(x,y,size,'WHITE')
# sd.pause()
