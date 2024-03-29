# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def triangle(start_point,angle,length):
    if angle > 360:
        pass
    else:
        v1=sd.vector(start_point,angle,length)
        start_point=v1
        triangle(start_point,angle+120,length)

def square(start_point,angle,length):
    if angle > 360:
        pass
    else:
        vector=sd.vector(start_point,angle,length)
        start_point=vector
        square(start_point,angle+90,length)

def pentagon(start_point,angle,length):
    if angle > 360:
        pass
    else:
        vector=sd.vector(start_point,angle,length)
        start_point=vector
        pentagon(start_point,angle+72,length)

def hexagon(start_point,angle,length):
    if angle > 360:
        pass
    else:
        vector=sd.vector(start_point,angle,length)
        start_point=vector
        hexagon(start_point,angle+60,length)

def draw_figure(start_point,angle,length):
    if angle == 360:
        pass
    else:
        vector=sd.vector(start_point,angle,length)
        start_point=vector
        draw_figure(start_point,angle+angle_delta,length)


# triangle(sd.get_point(100,100),0,100)
# square(sd.get_point(100,100),0,100)
# pentagon(sd.get_point(100,100),0,100)
#hexagon(sd.get_point(100,100),0,100)
angle_count = input("Введите количество углов у фигуры: ")
angle_delta = 360/float(angle_count)
draw_figure(sd.get_point(100,100),0,100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
