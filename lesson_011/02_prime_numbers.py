# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n+1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


# class PrimeNumbers:
#     def __init__(self,n):
#         self.divisible=1
#         self.divider=1
#         self.n=n
#
#     def __iter__(self):
#         self.divisible=1
#         self.divider=1
#         if self != None:
#             return self
#
#     def __next__(self):
#         self.divisible += 1
#         self.divider = self.divisible
#         while self.divider>1:
#             if self.divisible>self.n:
#                 break
#             self.divider-=1
#             if self.divisible % self.divider == 0:
#                 break
#         if self.divider==1:
#             return self.divisible
#
#
#
#
#
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     if number:
#         print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


# def prime_numbers_generator(n,divisible,):
#     for _ in range(n):
#         divisible += 1
#         divider = divisible
#         while divider>1:
#             divider-=1
#             if divisible % divider == 0:
#                 break
#         if divider==1:
#             yield divisible
#
#
# divisible=2
# for number in prime_numbers_generator(n=10000,divisible=1):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def is_lucky(number):
    a = 0
    b = 0
    first_part=str(number)[0:(len(str(number))//2)]
    second_part=str(number)[-(len(str(number))//2):]
    for i in first_part:
        a+=int(i)
    for i in second_part:
        b+=int(i)
    return a==b

def palindrome(number):
    a = 0
    b = 0
    first_part=str(number)[0:(len(str(number))//2)]
    second_part=str(number)[-(len(str(number))//2):]
    for i in range(len(str(number))//2):
        if first_part[i] != second_part[-i-1]:
            return False
    return True

my_numbers=[1742651,234,3223,452101254]
# result=filter(is_lucky,my_numbers)
# print(list(result))
# result=filter(palindrome,my_numbers)
# print(list(result))

