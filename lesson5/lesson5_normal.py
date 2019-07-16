# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# lesson5_normal.py param1 param2
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла/папки")
    print("rm <file_name> - удаляет указанный файл/папку")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


# def not_dir_name():
#     if not dir_name:
#         print("Необходимо указать имя директории вторым параметром")
#         return
#     return os.path.join(os.getcwd(), dir_name)


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f'директория {dir_name} создана')
    except FileExistsError:
        print(f'директория {dir_name} уже существует')


def ping():
    print("pong")


def file_copy():
    if not dir_name:
        print("Необходимо указать имя файла/папки вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        shutil.copyfile(dir_path, f'copy_{dir_name}')
        print(f'копия файла {dir_name} создана')
    except FileNotFoundError:
        print(f'файл {dir_name} не найден')
    except PermissionError:
        n = 0
        while True:
            n += 1
            try:
                shutil.copytree(dir_path, f'{dir_path}_copy{n}')
                print(f'копия папки {dir_name} создана')
            except FileExistsError:
                continue
            break


def file_del():
    if not dir_name:
        print("Необходимо указать имя файла/папки вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.remove(dir_path)
        print(f'файл {dir_name} упешно удалён')
    except FileNotFoundError:
        print(f'файл/папка {dir_name} не найдены')
    except PermissionError:
        shutil.rmtree(dir_path)
        print(f'папка {dir_name} упешно удалёна')


def cd_dir():
    if not dir_name:
        print("Необходимо указать имя файла/папки вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print(dir_path)
        print(os.getcwd())
    except FileNotFoundError:
        print(f'папка {dir_name} не найдена')
    except NotADirectoryError:
        pass


def list_dir():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": file_copy,
    "rm": file_del,
    "cd": cd_dir,
    "ls": list_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ\nУкажите ключ help для получения справки")