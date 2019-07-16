import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

try:
    for i in range(1, 10):
        os.mkdir(f'dir_{i}')
except FileExistsError:
    print('Создать папки не удалось')
else:
    print('Папки успешно созданы')

try:
    for i in range(1, 10):
        os.rmdir(f'dir_{i}')
except FileNotFoundError:
    print('Папки для удаления не найдены')
else:
    print('Папки успешно удалены')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

for d in os.listdir(os.getcwd()):
    if os.path.isdir(d):
        print(os.path.basename(d))
    # print(os.path.basename(d) if os.path.isdir(os.path.basename(d)) else f'{d} - не является папкой')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

shutil.copyfile(__file__, f'copy_{os.path.basename(__file__)}')
