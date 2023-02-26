#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint

src=input('Введите город отправления: ')
dst=input('Введите город назначения: ')

print(src)
print(dst)

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

#Создаём списки с координатами городов
Moscow=sites['Moscow']
London=sites['London']
Paris=sites['Paris']

#Вычисляем расстояние между городами
moscow_london = ((Moscow[0]-London[0]) ** 2 + (Moscow[1]-London[1]) ** 2) ** 0.5
moscow_paris = ((Moscow[0]-Paris[0]) ** 2 + (Moscow[1]-Paris[1]) ** 2) ** 0.5
london_paris = ((London[0]-Paris[0]) ** 2 + (London[1]-Paris[1]) ** 2) ** 0.5

#Создаём словарь для каждого города
distances['Moscow']={}
distances['London']={}
distances['Paris']={}

#Заполняем словари
distances['Moscow']['London']=moscow_london
distances['Moscow']['Paris']=moscow_paris
distances['London']['Moscow']=moscow_london
distances['London']['Paris']=london_paris
distances['Paris']['Moscow']=moscow_paris
distances['Paris']['London']=london_paris

print('Расстояние в пути: ' + str(distances[src][dst]))



