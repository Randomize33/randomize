# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = random.randint(50, 550)
        self.y=600
    def draw(self):
        sd.snowflake(sd.get_point(self.x, self.y), 10, color='WHITE')
        sd.sleep(0.01)

    def clear_previous_picture(self):
        sd.snowflake(sd.get_point(self.x, self.y), 10, color=sd.background_color)

    def move(self):
        self.x += random.randint(-20, 20)
        self.y -= random.randint(5, 25)
        if 480<self.y<500:
            flakes.append(Snowflake())
        elif self.y<=0:
            self.y=600
        return (self.x, self.y)

    def can_fall(self):
        if self.y<0:
            return True


def get_flakes(count):
    global flakes
    for _ in range(0,count):
        flakes.append(Snowflake())

flakes = []
get_flakes(10)
print(flakes)

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        if flake.can_fall() == True:
            break
        sd.sleep(0.1)
    # if sd.user_want_exit():
    #     break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

#sd.pause()
