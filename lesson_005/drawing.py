# -*- coding: utf-8 -*-

import simple_draw as sd
def wall():

    for y in range (0,700,100):
        start_point = sd.get_point(250, y)
        end_point = sd.get_point(450, y)
        sd.line(start_point=start_point,end_point=end_point)
        for x in range (100,600,100):
            start_point = sd.get_point(x, y)
            end_point = sd.get_point(x, y+10)
            sd.line(start_point=start_point, end_point=end_point)

    for y in range (50,700,100):
        start_point = sd.get_point(0, y)
        end_point = sd.get_point(600, y)
        sd.line(start_point=start_point,end_point=end_point)
        for x in range (50,600,100):
            start_point = sd.get_point(x, y)
            end_point = sd.get_point(x, y+10)
            sd.line(start_point=start_point, end_point=end_point)


def tree():
        def draw_branches(point,angle,lenth):
            if lenth <5:
                return
            vector1=sd.get_vector(point,angle,lenth)
            vector2=sd.get_vector(point,angle,lenth)
            vector1.draw()
            vector2.draw()
            point1=vector1.end_point
            point2=vector1.end_point
            angle1=angle+35
            angle2=angle-35
            lenth=lenth*0.75
            draw_branches(point1,angle1,lenth)
            draw_branches(point2,angle2,lenth)
        point=sd.get_point(500,0)
        draw_branches(point,90,50)

def rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    start_x=50
    finish_x=550
    start_y=50
    finish_y=550

    x=300
    y=-100
    for i in range(7):
        point = sd.get_point(x, y)
        color=rainbow_colors[i]
        sd.circle(point,radius=600,color=color,width=10)
        y-=10


