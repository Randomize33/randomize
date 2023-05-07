# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_sides(point,angle,length):
        angle_count=0
        angle_delta=360/n
        while angle_count < n:
            point=sd.vector(start=point,angle=angle,length=length)
            angle_count+=1
            angle+=angle_delta
    return draw_sides

n=int(input("Введите количество сторон: "))
draw_figure = get_polygon(n)
draw_figure(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()

