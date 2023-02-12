# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 150 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#     a) Добавьте игру против бота
#     б) Подумайте, как наделить бота "интеллектом"

from random import randint


def game_rules():
    print(
        f"\nНа столе лежит {total_sweets} конфет. Играют два игрока делая ход друг после друга. "
        "Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. "
        "Все конфеты оппонента достаются сделавшему последний ход."
    )


def how_many_players():
    global player_2
    print("1) Играть с ботом.\n2) Играть с другом.")
    num = int(input("Выберите режим игры, указав цифру варианта(1 или 2): "))
    while num < 1 or num > 2:
        num = int(input("Нужно ввести 1 или 2: "))
    if num == 1:
        player_2 = "Бот"
    who_first()


def who_first():
    if randint(0, 1):
        print(f"\nЖребий брошен, первым ходит {player_1}")
        turn_player(player_1)
    else:
        print(f"\nЖребий брошен, первым ходит {player_2}")
        turn_player(player_2)


def turn_player(player):
    global total_sweets
    match player:
        case "Бот":
            take_sweets = total_sweets % 29 if total_sweets % 29 != 0 else randint(1, 28)
            print(
                f"\n{player}.\nВсего кофет: {total_sweets}.\nСколько конфет берете: {take_sweets}"
            )
        case _:
            take_sweets = int(input(
                f"\n{player}.\nВсего кофет: {total_sweets}.\nСколько конфет берете: "
            ))
            while take_sweets < 1 or take_sweets > 28 or take_sweets > total_sweets:
                take_sweets = int(input(
                    "Число не должно быть больше 28.\nСколько конфет возьмете: "
                ))
    total_sweets -= take_sweets
    print(f"Осталось {total_sweets} конфет")
    if total_sweets <= 0:
        print(f"{player} победил!!!")
        return
    if player == player_1:
        turn_player(player_2)
    else:
        turn_player(player_1)


total_sweets = 150
player_1 = 'Игрок 1'
player_2 = 'Игрок 2'

game_rules()
how_many_players()
