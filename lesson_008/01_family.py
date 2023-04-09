# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint
from colorama import Fore, init
init(autoreset=True)

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько съедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money=100
        self.food=50
        self.mess=0
        self.total_expenses=0
        self.total_food_eaten=0
        self.total_fur=0

    def __str__(self):
        self.mess+=5
        return 'Денег в тумбочке {}, еды в холодильнике {}, грязи в доме {}'.format(
            self.money,self.food,self.mess
        )


class Human:
    def __init__(self,name,house):
        self.house=house
        self.name=name
        self.fullness=30
        self.happy=100
    def __str__(self):
        return 'Я {}, сытость {}, счастья {}'.format(self.name,self.fullness,self.happy)
    def eat(self):
        if self.house.food <=0:
            print("Еды в доме нет")
            self.fullness-=10
        else:
            if self.house.food<30:
                self.fullness += self.house.food
                self.house.food-=self.house.food
                self.house.total_food_eaten+=self.house.food
                cprint('{} поел'.format(self.name))
            else:
                self.house.food-=30
                self.fullness+=30
                self.house.total_food_eaten +=30
                cprint('{} поел'.format(self.name))
class Husband(Human):

    def __init__(self,name,house):
        super().__init__(name,house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness<=0:
            cprint('{} умер от голода'.format(self.name),'red')
        elif self.fullness<=30:
            self.eat()
        elif self.house.money<100:
            self.work()
        else:
            self.gaming()

    def work(self):
        self.house.money+=150
        self.fullness-=10
        cprint('{} сходил на работу'.format(self.name))

    def gaming(self):
        self.happy+=20
        self.fullness -= 10
        cprint('{} поиграл в WoT'.format(self.name))


class Wife(Human):

    def __init__(self,name,house):
        super().__init__(name,house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness<=0:
            cprint('{} умерла от голода'.format(self.name),'red')
        elif self.happy<=0:
            cprint('{} умерла от депрессии'.format(self.name), 'red')
        elif self.fullness <=30:
            self.eat()
        elif self.house.food <= 100:
            self.shopping()
        elif self.house.mess >=100:
            self.clean_house()
        else:
            self.buy_fur_coat()


    def shopping(self):
        if self.house.money<0:
            cprint('Денег нет','red')
        else:
            self.fullness-=10
            self.house.food+=30
            self.house.money-=30
            self.house.total_expenses+=30
            cprint('{} купила еды'.format(self.name),'yellow')

    def buy_fur_coat(self):
        if self.house.money<150:
            cprint('{}, тебе не хватает денег на шубу'.format(self.name),'red')
        else:
            self.fullness -= 10
            self.happy += 60
            self.house.money -= 150
            self.house.total_expenses +=150
            self.house.total_fur+=1
            cprint('{} купила себе шубу и радуется'.format(self.name), 'yellow')

    def clean_house(self):
        self.fullness -= 10
        self.house.mess -= 100
        cprint('{} убралась дома'.format(self.name), 'yellow')


home = House()
Alex = Husband(name='Саша',house=home)
Dasha = Wife(name='Даша',house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    Alex.act()
    Dasha.act()
    cprint(Alex, color='cyan')
    cprint(Dasha, color='cyan')
    cprint(home, color='cyan')

cprint('================== Итого ==================', color='red')
cprint('Денег потрачено {}, еды съедено {}, шуб куплено {}'.format(home.total_expenses,home.total_food_eaten,home.total_fur),'blue')
######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

