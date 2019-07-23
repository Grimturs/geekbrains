"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random
from sys import exit


# создание карточки
class Card:
    def __init__(self, name):
        self._name = name
        self._string_len = 9
        self._number_of_lines = 3
        self._number_per_line = 5
        self._scoreboard = []
        self.keg = [i for i in range(1, 91)]
        # self._keg_card = [i for i in range(1, 91)]
        self._footer = self._string_len * 2 + self._string_len - 1
        # print(name.center(self._footer, '-'))

        for i in range(self._number_of_lines):

            # ran = int(''.join(map(str, random.sample(self._keg_card, self._string_len))))
            # self._scoreboard.append(self._keg_card.pop(self._keg_card.index(ran)))

            self._scoreboard.append(random.sample(self.keg, self._string_len))  # нужно сделать буз дублей
            self._scoreboard[i].sort()
            a = 1
            while a <= self._string_len - self._number_per_line:    # добавление пустых мест в карточку
                i2 = random.randint(0, len(self._scoreboard[i]) - 1)
                if self._scoreboard[i][i2] == ' ':
                    continue
                else:
                    self._scoreboard[i][i2] = ' '
                    a += 1
        #     print(' '.join(str(x).rjust(2) for x in self._scoreboard[i]))
        # print('-'*self._footer)

    def show_card(self):
        print(self._name.center(self._footer, '-'))
        for i in range(self._number_of_lines):
            print(' '.join(str(x).rjust(2) for x in self._scoreboard[i]))
        print('-' * self._footer)


def funny(fan):
    if fan == 11:
        return print('\n\nБарабанные палочки')
    elif fan == 22:
        return print('\n\nУти-ути')
    elif fan == 25:
        return print('\n\nОпять — 25')
    elif fan == 27:
        return print('\n\nЛебедь с топором')
    elif fan == 45:
        return print('\n\n45- Баба ягодка опять')
    elif fan == 69:
        return print('\n\nТуда-сюда =)')
    elif fan == 80:
        return print('\n\nБабушка')
    elif fan == 87:
        return print('\n\nБабка с топором')
    elif fan == 90:
        return print('\n\nДед. А сколько деду лет?')


def step(card, card2):
    ran = int(''.join(map(str, random.sample(card.keg, 1))))
    keg = card.keg.pop(card.keg.index(ran))
    funny(keg)
    print(f"\nНовый бочонок: {keg} (осталось {len(card.keg)})")
    card.show_card()
    card2.show_card()
    answer = input('Зачеркнуть цифру? (y/n) ')

    # проверка ответа и вычёркивание чисел из карточкки пользователя (если оно есть)
    while answer != 'y' or 'Y' or 'n' or 'N':
        if answer == 'y' or answer == 'Y':
            if check_card(keg, card._scoreboard):
                for i in range(len(card._scoreboard)):
                    for j in range(len(card._scoreboard[i])):
                        if keg == card._scoreboard[i][j]:
                            card._scoreboard[i][j] = '-'
            else:
                print('Вы проиграли1')
                exit()
            break
        elif answer == 'n' or answer == 'N':
            if check_card(keg, card._scoreboard):
                print('Вы проиграли2')
                exit()
            else:
                pass
            break
        else:
            print('Вы ввели неверное значение')
        answer = input('Зачеркнуть цифру? (y/n) ')

    if check_card(keg, card2._scoreboard):
        for i in range(len(card2._scoreboard)):
            for j in range(len(card2._scoreboard[i])):
                if keg == card2._scoreboard[i][j]:
                    card2._scoreboard[i][j] = '-'


# проверка на наличия числа с бочонка в карточке
def check_card(keg, card):
    check = True
    for i in range(len(card)):
        if keg in card[i]:
            check = True
            break
        else:
            check = False
    return check


def check_card_win(card_win):
    check_kek_in_card = 0
    for i in range(len(card_win._scoreboard)):
        for j in range(len(card_win._scoreboard[i])):
            if '-' == card_win._scoreboard[i][j]:
                check_kek_in_card += 1
            if check_kek_in_card == card_win._number_per_line * 3:
                print(f'Победила, {card_win._name}')
                exit()  # нужно сделать возврат, чтобы не обрывать процесс


def go(card, card2):
    while True:
        step(card, card2)
        check_card_win(card)
        check_card_win(card2)


your_card = Card(' Ваша карточка ')
comp_card = Card(' Карточка компьютера ')


go(your_card, comp_card)
