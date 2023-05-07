# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

def log_parser(file,find_str):
    prew_line=""
    with open(file, mode='r', encoding='utf8') as file:
        for line in file:
            if find_str in line:
                if line[1:17] in result:
                    result[line[1:17]] += 1
                else:
                    try:
                        result[line[1:17]] = 1
                        yield (prew_line,result[prew_line])
                        prew_line = line[1:17]
                    except KeyError:
                        prew_line = line[1:17]

file="events.txt"
find_str="NOK"
result = {}

for line in log_parser(file,find_str):
    print(line)