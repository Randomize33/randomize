# -*- coding: utf-8 -*-
import simple_draw
# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_x=50
finish_x=350
start_y=50
finish_y=450

#for i in range(6):
#    color=rainbow_colors[i]
#    start_point=simple_draw.get_point(start_x,start_y)
#    end_point=simple_draw.get_point(finish_x,finish_y)
#    simple_draw.line(start_point,end_point,color=color,width=4)
#    start_x += 5
#    finish_x += 5
#    start_y += 5
#    finish_y += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

x=300
y=-300
for i in range(7):
    point = simple_draw.get_point(x, y)
    color=rainbow_colors[i]
    simple_draw.circle(point,radius=600,color=color,width=20)
    y-=20



sd.pause()
