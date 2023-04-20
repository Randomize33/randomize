# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Sort_char():

    def __init__(self,file_in):
        self.file_in=file_in
        self.stat_chars={}
        self.chars_total=0

    def pars_line(self):
        with open (self.file_in, mode='r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        self.chars_total+=1
                        if char in self.stat_chars:
                            self.stat_chars[char]+=1
                        else:
                            self.stat_chars[char]=1




kniga=Sort_char('voyna-i-mir.txt')
kniga.pars_line()
sort_chars=dict(sorted(kniga.stat_chars.items(), key=lambda item: item[1], reverse=True))
print("{}{}".format("+-----","+-------+"))
print("|{:<5}|{:^6}|".format("Буква","Частота"))
print("{}{}".format("+-----","+-------+"))
for char in sort_chars:
    print("|{:^5}|{:>7}|".format(char,sort_chars.get(char)))
print("{}{}".format("+-----","+-------+"))
print("|{:<5}|{:^6}|".format("Итого",kniga.chars_total))
print("{}{}".format("+-----","+-------+"))

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
