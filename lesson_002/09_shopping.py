#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)

name1=shops.get('ашан')[0].get('name')
name2=shops.get('ашан')[1].get('name')
name3=shops.get('ашан')[2].get('name')
name4=shops.get('ашан')[3].get('name')

shop=[*shops]
print(shop[0])





sweets = {
    name1: [
        {'shop': shop[0], 'price': shops.get(shop[0])[0].get('price')},
        {'shop': shop[1], 'price': shops.get(shop[1])[0].get('price')},
        {'shop': shop[2], 'price': shops.get(shop[2])[0].get('price')},
    ],
    name2: [
        {'shop': shop[0], 'price': shops.get(shop[0])[1].get('price')},
        {'shop': shop[1], 'price': shops.get(shop[1])[1].get('price')},
        {'shop': shop[2], 'price': shops.get(shop[2])[1].get('price')},
    ],
    name2: [
        {'shop': shop[0], 'price': shops.get(shop[0])[2].get('price')},
        {'shop': shop[1], 'price': shops.get(shop[1])[2].get('price')},
        {'shop': shop[2], 'price': shops.get(shop[2])[2].get('price')},
    ],
    name3: [
        {'shop': shop[0], 'price': shops.get(shop[0])[3].get('price')},
        {'shop': shop[1], 'price': shops.get(shop[1])[3].get('price')},
        {'shop': shop[2], 'price': shops.get(shop[2])[3].get('price')},
    ]
}
# Указать надо только по 2 магазина с минимальными ценами


print(sweets)