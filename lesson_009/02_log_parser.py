# -*- coding: utf-8 -*-


# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Parser():

    def __init__(self, file_in, find_str, file_out):
        self.file_in=file_in
        self.find_str=find_str
        self.file_out=file_out
        self.result={}
    def count_value(self):
        with open(self.file_in, mode='r', encoding='utf8') as file:
            for line in file:
                if self.find_str in line:
                    if line[1:17] in self.result:
                        self.result[line[1:17]]+=1
                    else:
                        self.result[line[1:17]]=1
        self.write_to_file()

    def write_to_file(self):
        with open(self.file_out, mode='w') as file:
            for date in self.result:
                file.write('[{}] {} \n'.format(date,self.result.get(date)))


collect_data=Parser('events.txt',' OK','log_result.txt')
collect_data.count_value()
collect_data.write_to_file()




# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
