import random
import math

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

print('\nЗадача-1:\n')
list1 = [random.randint(-9, 51) for i in range(8)]
print('Дано: ', list1)
list_new = []
for index in list1:
    if index > 0:
        a = math.sqrt(index)
        if index % a == 0:
            list_new.append(int(a))
print('Результат: ', list_new)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print('\nЗадача-2:\n')
days = {
        '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое', '06': 'шестое',
        '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцатое',
        '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое',
        '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое',
        '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвёртое', '25': 'двадцать пятое',
        '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое',
        '30': 'тридцатое', '31': 'тридцать первое'
        }

months = {
        '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
        '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
        }
day = input('Введите дату в формате dd.mm.yyyy; ')
list_day = day.split('.')
print(days[list_day[0]], months[list_day[1]], list_day[2], 'года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print('\nЗадача-3:\n')
n = int(input("Кол-во элементов в списке:"))
list3 = [random.randint(-100, 100) for i in range(0, n)]
print('список с произвольными целыми числами: ', list3)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print('\nЗадача-4:\n')
list4 = [random.randint(0, 8) for i in range(8)]
print('исходный список: ', list4)
list5 = set(list4)
print('неповторяющиеся элементы исходного списка: ', list5)
list6 = []
for x in list4:
    if not list4.count(x) > 1:
        list6.append(x)
# list6 = [x for x in list4 if not list4.count(x) > 1]
print('элементы исходного списка, которые не имеют повторений: ', list6)