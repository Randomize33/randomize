# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def draw_figure(start_point,angle,length,color):
    if angle == 360:
        pass
    else:
        vector=sd.vector(start_point,angle,length,color)
        start_point=vector
        draw_figure(start_point,angle+angle_delta,length,color)

colors_list=['RED', 'ORANGE', 'YELLOW', 'GREEN', 'CYAN', 'BLUE', 'PURPLE']
print('''
1. Крайсный
2. Оранжевый
3. Жёлтый
4. Зелёный
5. Голубой
6. Синий
7. Фиолетовый''')
color_number = input("Введите номер цвета фигуры: ")
color=colors_list[int(color_number)-1]
angle_count = input("Введите количество углов у фигуры: ")
angle_delta = 360/float(angle_count)
draw_figure(sd.get_point(100,100),0,100,color)

sd.pause()
