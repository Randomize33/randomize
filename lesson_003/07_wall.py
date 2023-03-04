# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


for y in range (0,700,100):
    start_point = simple_draw.get_point(0, y)
    end_point = simple_draw.get_point(600, y)
    simple_draw.line(start_point=start_point,end_point=end_point)
    for x in range (100,600,100):
        start_point = simple_draw.get_point(x, y)
        end_point = simple_draw.get_point(x, y+50)
        simple_draw.line(start_point=start_point, end_point=end_point)

for y in range (50,700,100):
    start_point = simple_draw.get_point(0, y)
    end_point = simple_draw.get_point(600, y)
    simple_draw.line(start_point=start_point,end_point=end_point)
    for x in range (50,600,100):
        start_point = simple_draw.get_point(x, y)
        end_point = simple_draw.get_point(x, y+50)
        simple_draw.line(start_point=start_point, end_point=end_point)

simple_draw.pause()
