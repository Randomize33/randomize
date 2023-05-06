# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class ValueError(Exception):
    def __init__(self,line):
        self.line=line
        self.error_string = ""
        self.log()
    def __str__(self):
        return self.error_string
    def log(self):
        for element in self.line:
            self.error_string+=element+" "
        self.error_string+="- Error: Неполная анкета\n"

class NotNameError(Exception):
    def __init__(self,line):
        self.line=line
        self.error_string = ""
        self.log()
    def __str__(self):
        return self.error_string
    def log(self):
        for element in self.line:
            self.error_string+=element+" "
        self.error_string+="- Error: Ошибка в имени\n"
class NotEmailError(Exception):
    def __init__(self,line):
        self.line=line
        self.error_string = ""
        self.log()
    def __str__(self):
        return self.error_string
    def log(self):
        for element in self.line:
            self.error_string+=element+" "
        self.error_string+="- Error: Ошибка в email\n"
class log_report():
    def __init__(self,file):
        self.file=file
        self.name=""
        self.email=""
        self.age=""
        self.line=""
        self.good_log="registrations_good.log"
        self.bad_log = "registrations_bad.log"

    def parsing_file(self):
        with open(self.file, mode="r", encoding="UTF8") as file:
            for self.line in file:
                self.line=self.line.replace("\n","").split(" ")
                if self.line!=['']:
                    try:
                        result=self.parsing_line()
                    except Exception as exc:
                        self.wirte_to_log(self.bad_log,exc)
                    else:
                        self.wirte_to_log(self.good_log,result)
    def parsing_line(self):
        try:
            self.name=self.line[0]
            self.email=self.line[1]
            self.age=self.line[2]
        except IndexError:
            raise ValueError(self.line)
        if self.name.isalpha()==False:
            raise NotNameError(self.line)
        try:
            if 99<int(self.age) or int(self.age)<10:
                raise ValueError(self.line)
        except:
            raise ValueError(self.line)
        if ("." in self.email and "@" in self.email)==False:
            raise NotEmailError(self.line)
        string = (f"{self.name} {self.email} {self.age}\n")
        self.name,self.email,self.age='','',''
        return string

    def wirte_to_log(self,log_file,log_string):
        with open(log_file, mode="a", encoding="UTF8") as file:
            file.write(f"{log_string}")

        # else:
        #     try:
        #         if self.name.isalpha():
        #             raise NotNameError
        #     except NotNameError():
        #         with open (self.bad_log,mode="a",encoding="UTF8") as file:
        #             for element in self.line:
        #                 file.write(element+" ")
        #             file.write("- Error: Некорректное имя\n")


file="registrations.txt"
report=log_report(file)

report.parsing_file()