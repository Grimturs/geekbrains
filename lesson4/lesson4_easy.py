# Все задачи текущего блока решены с помощью генераторов списков!
import random
# Задание-1:
# Дан список, заполненный нежелательными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] -> [1, 4, 16, 0]

print('\nЗадание-1:\n')
old_list = [random.randint(0, 10) for i in range(0, 8)]
new_list = []
for index in old_list.copy():
    index *= index
    new_list.append(index)
print(old_list)
print(new_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('\nЗадание-2:\n')
fruits_all = ["яблоко", "банан", "киви", "арбуз", "апельсин", "груша", "авокадо", "алыча", "абрикос", "нектарин"]
fruits_list1 = random.sample(fruits_all, 6)
fruits_list2 = random.sample(fruits_all, 6)
print(fruits_list1)
print(fruits_list2)
print(list(set(fruits_list1) & set(fruits_list2)))

# Задание-3:
# Дан список, заполненные нежелательными числами.
# Получить список из элементов исходного, удовлетворяющего следующими условиями:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('\nЗадание-3:\n')
o_list = [random.randint(-100, 100) for i in range(0, 40)]
n_list = []
print(o_list)
for num in o_list:
    if num % 3 == 0 and num > 0 and num % 4 != 0:
        n_list.append(num)
print(n_list)