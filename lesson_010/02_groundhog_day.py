# -*- coding: utf-8 -*-

import random
# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777

class IamGodError(Exception):
    pass
class DrunkError(Exception):
    pass
class CarCrashError(Exception):
    pass
class GluttonyError(Exception):
    pass
class DepressionError(Exception):
    pass
class SuicideError(Exception):
    pass

def groundhog_day():
    karma=0
    while karma<ENLIGHTENMENT_CARMA_LEVEL:
        try:
            rnd=random.randint(1,13)
            if rnd == 13:
                error=random.randint(1,6)
                if error==1:
                    raise IamGodError("Я не Бог!")
                elif error==2:
                    raise DrunkError("Напился")
                elif error==3:
                    raise CarCrashError("Разбился")
                elif error==4:
                    raise GluttonyError("Объелся")
                elif error==5:
                    raise DepressionError("Приуныл")
                elif error==6:
                    raise SuicideError("Самоубился")
        except Exception as exc:
            print(f"{exc}")
        finally:
            karma+=random.randint(1,7)
    print(karma)
groundhog_day()

# https://goo.gl/JnsDqu
