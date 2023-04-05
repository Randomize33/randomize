# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint
# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 50
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_feed(self):
        if self.house.money >= 50:
            cprint('{} купил коту еды'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.feed += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_up(self):
        cprint('{} прибрался в доме'.format(self.name), color='magenta')
        self.house.mess -= 100
        self.fullness -= 20

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def pick_up_a_cat(self, nickname):
        cat.house=self.house
        cprint('{} притащил в дом кота по имени {}'.format(self.name,cat.nickname), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.feed < 10:
            self.buy_feed()
        elif self.house.mess >100:
            self.clean_up()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

class Cat:
    def __init__(self,nickname):
        self.nickname = nickname
        self.fullness = 10
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.nickname, self.fullness)

    def sleep(self):
        cprint('{} поспал'.format(self.nickname), color='orange')
        self.fullness -= 10

    def eat(self):
        if self.house.feed >=10:
            cprint('{} поел'.format(self.nickname), color='orange')
            self.fullness += 20
            self.house.feed -= 10
        else:
            cprint('{} корма нет, дайте пожрать'.format(self.nickname), color='red')

    def tear_wallpaper(self):
        cprint('{} изодрал обои'.format(self.nickname), color='orange')
        self.fullness -= 10
        self.house.mess += 5

    def act (self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.nickname), color='red')
            return
        if self.fullness < 20:
            self.eat()
        elif self.house.feed < 10:
            self.sleep()
        else:
            self.tear_wallpaper()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.feed = 0
        self.mess = 0

    def __str__(self):
        return 'В доме еды осталось {}, корма для кота {}, денег осталось {}, а бардак в доме {}'.format(
            self.food, self.feed, self.money, self.mess)



citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]


my_sweet_home = House()
cat = Cat(nickname='Барсик')
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

citizens[0].pick_up_a_cat(nickname=cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    cat.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
