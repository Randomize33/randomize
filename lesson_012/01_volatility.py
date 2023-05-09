# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>
import os
import time

def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate
class Parser():
    def __init__(self,dir,files):
        self.files=files
        self.dir=dir
        self.volatility_null = []
        self.volatility_list = {}

    @time_track
    def parsing(self):
        for file in self.files:
            self.ticker = ""
            self.dealtime = ""
            self.dealprice = ""
            self.countpaper = ""
            self.maxprice=0
            self.minprice=9999999
            self.volatility=0
            with open ((self.dir+file),mode='r',encoding='UTF8') as file_ticket:
                for line in file_ticket:
                    self.ticker,self.dealtime,self.dealprice,self.countpapaer=line.split(',')
                    if self.dealprice=="PRICE":
                        continue
                    self.dealprice=float(self.dealprice)
                    if self.minprice>self.dealprice:
                        self.minprice=self.dealprice
                    if self.maxprice<self.dealprice:
                        self.maxprice=self.dealprice
                self.average_price = (self.maxprice + self.minprice)/2
                self.volatility = ((self.maxprice - self.minprice)/self.average_price)*100
                if self.volatility==0:
                    self.volatility_null.append(self.ticker)
                else:
                    self.ticker=str(self.ticker)
                    self.volatility_list[self.ticker]=round(self.volatility,2)
        self.volatility_list=dict(sorted(self.volatility_list.items(), key=lambda item: item[1]))
        print("Максимальная волатильность")
        for i in range (1,4):
            print(list(self.volatility_list.keys())[len(self.volatility_list)-i],list(self.volatility_list.values())[len(self.volatility_list)-i],"%")
        print("Минимальная волатильность")
        for i in range (3):
            print(list(self.volatility_list.keys())[i],list(self.volatility_list.values())[i],"%")
        print("Нулевая волатильность:")
        for i in range (len(self.volatility_null)):
            print(self.volatility_null[i],end=", ")




class File():
    def __init__(self,dir):
        self.dir=dir
        self.list_files=[]
    def read_dir(self):
        self.list_files=os.listdir(self.dir)

path="C:/Users/Randomize/PycharmProjects/randomize/lesson_012/trades/"
files=File(path)
files.read_dir()
parser=Parser(dir=path,files=files.list_files)
parser.parsing()