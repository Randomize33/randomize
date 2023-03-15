# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def draw_figure(start_point,angle,length):
    if angle == 360:
        pass
    else:
        vector=sd.vector(start_point,angle,length)
        start_point=vector
        draw_figure(start_point,angle+angle_delta,length)

figure_list=[3, 4, 5, 6]
print('''
1. Треугольник
2. Квадрат
3. Пятиугольник
4. Шестиугольник
''')
figure_number = int(input("Введите номер фигуры: "))
angle_delta = 360/int(figure_list[figure_number-1])
draw_figure(sd.get_point(250,250),0,100)

sd.pause()
