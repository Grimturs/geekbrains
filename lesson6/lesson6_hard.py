# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.


class Plaything:
    def __init__(self, name, color, types):
        self.name = name
        self.color = color
        self.types = types

    def purchase(self):
        print(f'Закупка материала для игрушки {self.name} типа {self.types}')

    def sewing(self):
        print(f'Начался пошив ишрушки {self.name}')

    def coloring(self):
        print(f'Окраска игрушки {self.name} в {self.color} цвет')

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Plaything_animal(Plaything):
    def __init__(self, name, color, types):
        super().__init__(name, color, types)
        self.types = '"животное"'
        self.purchase()
        self.sewing()
        self.coloring()
        print(f'Игрушка {self.name}, типа {self.types} (цвет {self.color}) вышла с конвеера')


class Plaything_character(Plaything):
    def __init__(self, name, color, types):
        super().__init__(name, color, types)
        self.types = '"персонаж мультфильма"'
        self.purchase()
        self.sewing()
        self.coloring()
        print(f'Игрушка {self.name}, типа {self.types} (цвет {self.color}) вышла с конвеера')


bear = Plaything_animal('Бо-бо', 'коричневый', '')
mouse = Plaything_character('Джерри', 'серый', '')


