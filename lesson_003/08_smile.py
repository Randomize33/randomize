# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

list_x=[0]
list_y=[0]
for _ in range(10):
    x=simple_draw.random_number(50,550)
    y=simple_draw.random_number(50,550)
    for temp_x in list_x:
        if temp_x-25 < x < temp_x+25:
            pass
        else:
            for temp_y in list_y:
                if temp_y-25 < y < temp_y+25:
                    pass
                else:
                    list_x.append(x)
                    list_y.append(y)
                    point=simple_draw.get_point(x,y)
                    eye1=simple_draw.get_point(x-15,y+20)
                    eye2=simple_draw.get_point(x+15,y+20)
                    simple_draw.circle(point)
                    simple_draw.snowflake(eye1,length=1)
                    simple_draw.snowflake(eye2,length=1)
                    poinst_for_smile=[simple_draw.get_point(x-30,y),simple_draw.get_point(x-10,y-20),simple_draw.get_point(x+10,y-20),simple_draw.get_point(x+30,y)]
                    for _ in range(3):
                        simple_draw.lines(poinst_for_smile)

simple_draw.pause()
