# -*- coding: utf-8 -*-
import random

import simple_draw as sd
def paint_snowflake():
    sd.snowflake(sd.get_point(200,200),50,color='WHITE')
    sd.pause()



# def snowfall():
#     factora_list=[]
#     factorb_list=[]
#     x_list=[]
#     point_list = []
#     for _ in range(0,5):
#         factora_list.append(random.random())
#         factorb_list.append(random.random())
#     sd.start_drawing()
#     diff_y=random.randrange(-5,-1,1)
#     print(diff_y)
#     size=random.randrange(10,30,1)
#     for _ in range(0,10,1):
#         for y in range(600,0,diff_y):
#             if y==600:
#                 for i in range(0,5):
#                     x_list.append(random.randrange(10, 600, 10))
#                     point_list.append(sd.get_point(x_list[i],y))
#             for i in range(0, 5):
#                 x_list[i]=x_list[i]+random.randrange(0,5,1)
#                 point_list.append(sd.get_point(x_list[i], y))
#                 point_list[i]=(sd.get_point(x_list[i], y))
#             sd.snowflake(point_list[0],size,color="WHITE",factor_a=factora_list[0],factor_b=factorb_list[0])
#             sd.snowflake(point_list[1], size, color="WHITE", factor_a=factora_list[1], factor_b=factorb_list[1])
#             sd.snowflake(point_list[2], size, color="WHITE", factor_a=factora_list[2], factor_b=factorb_list[2])
#             sd.snowflake(point_list[3], size, color="WHITE", factor_a=factora_list[3], factor_b=factorb_list[3])
#             sd.snowflake(point_list[4], size, color="WHITE", factor_a=factora_list[4], factor_b=factorb_list[4])
#             sd.sleep(0.04)
#             if y < 10:
#                 snowfall()
#             else:
#                 sd.snowflake(point_list[0], size, color=sd.background_color, factor_a=factora_list[0], factor_b=factorb_list[0])
#                 sd.snowflake(point_list[1], size, color=sd.background_color, factor_a=factora_list[1], factor_b=factorb_list[1])
#                 sd.snowflake(point_list[2], size, color=sd.background_color, factor_a=factora_list[2],factor_b=factorb_list[2])
#                 sd.snowflake(point_list[3], size, color=sd.background_color, factor_a=factora_list[3],factor_b=factorb_list[3])
#                 sd.snowflake(point_list[4], size, color=sd.background_color, factor_a=factora_list[4],factor_b=factorb_list[4])
#             sd.finish_drawing()
#
#
#
#
# snowfall()


# while True:
#     sd.clear_screen()
#     pass
#     pass
#     pass
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


