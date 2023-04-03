# -*- coding: utf-8 -*-

class water():
    def __init__(self):
        self.name='Вода'
    def __add__(self, element):
        if element.name=='Воздух':
            return('Шторм')
        elif element.name=='Огонь':
            return ('Пар')
        elif element.name=='Земля':
            return ('Грязь')

class air():
    def __init__(self):
        self.name='Воздух'
    def __add__(self, element):
        if element.name=='Вода':
            return('Шторм')
        elif element.name=='Огонь':
            return ('Молния')
        elif element.name=='Земля':
            return ('Пыль')

class fire():
    def __init__(self):
        self.name='Огонь'
    def __add__(self, element):
        if element.name=='Вода':
            return('Пар')
        elif element.name=='Воздух':
            return ('Молния')
        elif element.name=='Земля':
            return ('Лава')

class ground():
    def __init__(self):
        self.name='Земля'
    def __add__(self, element):
        if element.name=='Вода':
            return('Грязь')
        elif element.name=='Воздух':
            return ('Пыль')
        elif element.name=='Огонь':
            return ('Лава')

list_elements=[]
elements=[]
for _ in range (0,2):
    list_elements.append(input('Введите элемент: '))

for elem in list_elements:
    if elem=='Вода':
        elements.append(water());
    elif elem=='Воздух':
        elements.append(air());
    elif elem=='Огонь':
        elements.append(fire());
    elif elem == 'Земля':
        elements.append(ground());


print('Вы получили: ', elements[0]+elements[1])



# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
