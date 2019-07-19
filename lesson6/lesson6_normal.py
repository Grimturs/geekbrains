# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random


class Person:
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def _attack(self, person2):
        def armor(damage):
            damage = int(damage / person2.armor)
            return damage
        person2.health -= armor(self.damage)
        print(f'HP {person2.name}: {person2.health}')
        return person2.health

    def battle(self, person2):
        while self.health >= 0 and person2.health >= 0:
            if random.randint(0, 1) > 0:
                Person._attack(self, person2)
            else:
                Person._attack(person2, self)
        if self.health < 0:
            print(f'Победил {person2.name}. Оставшееся кол-во HP: {person2.health}\n'
                  f'{person2.name}: {person2.victory_cry}')
        elif person2.health < 0:
            print(f'Победил {self.name}. Оставшееся кол-во HP: {self.health}\n'
                  f'{self.name}: {self.victory_cry}')


class Player(Person):
    def __init__(self, name, health, armor, damage, victory_cry):
        super().__init__(name, health, armor, damage)
        self.victory_cry = victory_cry


class Enemy(Player):
    pass


spider = Enemy('spider', 150, 1.3, 40, 'Пшаах! Кусссшшайте, детки мои')
hero = Player('Hero', 160, 1.2, 50, 'На одну тварь стало меньше!')

hero.battle(spider)
