# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
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
import os
import time
from multiprocessing import Process, Pipe, Queue
from collections import defaultdict
from queue import Empty

def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate

class Parser(Process):
    def __init__(self,file,conn,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.file=file
        self.conn=conn

    def run(self):
        self.ticker = ""
        self.dealtime = ""
        self.dealprice = ""
        self.countpaper = ""
        self.maxprice=0
        self.minprice=9999999
        self.volatility=0
        with open (self.file,mode='r',encoding='UTF8') as file_ticket:
            for line in file_ticket:
                self.ticker,self.dealtime,self.dealprice,self.countpapaer=line.split(',')
                if self.dealprice=="PRICE":
                    continue
                self.dealprice=float(self.dealprice)
                if self.minprice>self.dealprice:
                    self.minprice=self.dealprice
                if self.maxprice<self.dealprice:
                    self.maxprice=self.dealprice
            self.calculation()

    def calculation(self):
        self.average_price = (self.maxprice + self.minprice) / 2
        self.volatility = ((self.maxprice - self.minprice) / self.average_price) * 100
        self.conn.send([self.ticker, round(self.volatility, 2)])
        self.conn.close()



class File():

    def __init__(self,dir):
        self.dir=dir
        self.list_files=[]
        self.full_list_files = []
    def write_list_files(self):
        for file in os.listdir(self.dir):
            self.list_files.append(self.dir+file)


def output(volatility_null,volatility_list):
    volatility_list = dict(sorted(volatility_list.items(), key=lambda item: item[1]))
    print("Максимальная волатильность")
    for i in range(1, 4):
        print(list(volatility_list.keys())[len(volatility_list) - i],
              list(volatility_list.values())[len(volatility_list) - i], "%")
    print("Минимальная волатильность")
    for i in range(3):
        print(list(volatility_list.keys())[i], list(volatility_list.values())[i], "%")
    print("Нулевая волатильность:")
    for i in range(len(volatility_null)):
        print(volatility_null[i], end=", ")

path="C:/Users/Randomize/PycharmProjects/randomize/lesson_012/trades/"
extract_files=File(path)
extract_files.write_list_files()
volatility_null=[]
volatility_list={}

@time_track
def main():
    files,pipes=[],[]
    for file in extract_files.list_files:
        parent_conn, child_conn = Pipe()
        calc=Parser(file=file,conn=child_conn)
        files.append(calc)
        pipes.append(parent_conn)
    for calc in files:
        calc.start()
    for conn in pipes:
        data=conn.recv()
        ticker,volatility=data
        if volatility==0:
            volatility_null.append(ticker)
        else:
            volatility_list[ticker] = round(volatility, 2)
    for calc in files:
        calc.join()
    output(volatility_null,volatility_list)


if __name__ == '__main__':
    main()
