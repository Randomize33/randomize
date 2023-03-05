# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

items_list=[]
items_list.append(goods.get('Лампа'))
items_list.append(goods.get('Стол'))
items_list.append(goods.get('Диван'))
items_list.append(goods.get('Стул'))

items = {}
for key, value in goods.items():
  items[value] = items.get(value, []) + [key]


for item in items_list:
    total_cost = 0
    total_quantity = 0
    good_lists=store.get(item)
    name_of_goods=items.get(item)[0]
    for quantity in good_lists:
        total_cost += quantity.get('quantity')*quantity.get('price')
        total_quantity += quantity.get('quantity')
    print('Количество товара ' + name_of_goods + ' на складе: ' + str(total_quantity) + 'шт' + ', стоимостью: ' + str(total_cost))






