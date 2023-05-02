# -*- coding: utf-8 -*-

import os, time, shutil, zipfile
from os.path import join
import shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Files:
    def __init__(self,filename):
        self.filename=filename
        self.root_dir=""
    def unzip(self):
        zfile = zipfile.ZipFile(self.filename, 'r')
        for filename in zfile.namelist():
            self.root_dir=zfile.extract(filename)
        self.file_name = filename

    def take_date(self):
        self.root_dir=os.getcwd()+"\icons"
        for root, dirs, files in os.walk(self.root_dir):
            for name in files:
                year=str(time.gmtime(os.path.getmtime(join(root, name)))[0])
                month=str(time.gmtime(os.path.getmtime(join(root, name)))[1])
                now_file=join(root,name)
                self.create_dir(year,month,now_file)

    def create_dir(self,year,month,now_file):
        now_dir=join(self.root_dir+year+month)
        print(now_dir)
        if os.path.exists(now_dir):
            shutil.move(now_file,now_dir)
        else:
            os.mkdir(now_dir)
            shutil.move(now_file, now_dir)



icons=Files("icons.zip")
icons.unzip()
icons.take_date()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
