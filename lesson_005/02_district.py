# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import room_1
import room_2

room1=room_1.room_1()
room2=room_2.room_2()
district=room1+room2
print("На районе живут:", ", ".join(district))