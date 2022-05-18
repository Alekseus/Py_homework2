# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

print('Добро пожаловать в игру "Забери конфеты!"\nЗа один ход можно брать от 1 до 28 конфет.\n'
      'Побеждает тот, кто сделает последний ход.\nВсего конфет 2021.\nНачнем!')
candies = 2021
mode = int(input('Если хотите сыграть с человеком, нажмите 1, если с компьютером, нажмите 2: '))

if mode == 1:
    gamer_1, gamer_2 = input('Введите имя 1 игрока: '), input('Введите имя 2 игрока: ')
    x = [gamer_1, gamer_2]
    current_gamer = random.choice(x)
    while candies != 0:
        print(f'Конфет осталось: {candies}')
        while True:
            try:
                number_to_delete = int(input(f'Ход игрока {current_gamer} (1 - 28): '))
            except ValueError:
                print(f'Игрок {current_gamer}, возьмите от 1 до 28 конфет!')
            if number_to_delete >= 1 and number_to_delete <= 28:
                break
            else:
                print(f'Игрок {current_gamer}, возьмите от 1 до 28 конфет!')
        candies -= number_to_delete
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    print(f'Победил {current_gamer}')

else:
    gamer_1, gamer_2 = input('Введите имя 1 игрока: '), 'Mr. Bot'
    x = [gamer_1, gamer_2]
    current_gamer = random.choice(x)
    number_to_delete = 1
    while candies != 0:
        print(f'Конфет осталось: {candies}')
        while True:
            if current_gamer == gamer_2:
                if candies > 28:
                    number_to_delete = 29 - number_to_delete
                else:
                    number_to_delete = candies
                print(f'Mr. Bot взял {number_to_delete} конфет')
            else:
                try:
                    number_to_delete = int(input(f'Ход игрока {current_gamer} (1 - 28): '))
                except ValueError:
                    print(f'Игрок {current_gamer}, возьмите от 1 до 28 конфет!')
            if number_to_delete >= 1 and number_to_delete <= 28:
                break
            else:
                print(f'Игрок {current_gamer}, возьмите от 1 до 28 конфет!')
        candies -= number_to_delete
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    print(f'Победил {current_gamer}')