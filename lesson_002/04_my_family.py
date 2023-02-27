#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Соня','Даша','Папа','Мама']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    [my_family[0],122],
    [my_family[1],153],
    [my_family[2],188],
    [my_family[3],158]
]

# Выведите на консоль рост отца в формате
print('Рост ' + my_family_height[0][0] + ' ' + str(my_family_height[0][1])+'см')
print('Рост ' + my_family_height[1][0] + ' ' + str(my_family_height[1][1])+'см')
print('Рост ' + my_family_height[2][0] + ' ' + str(my_family_height[2][1])+'см')
print('Рост ' + my_family_height[3][0] + ' ' + str(my_family_height[3][1])+'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
print('Общий рост моей семьи - ' + str(my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1]+my_family_height[3][1]) + 'см')

