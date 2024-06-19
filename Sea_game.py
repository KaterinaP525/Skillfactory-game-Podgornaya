import random

def create_random_ship():
    return random.randint(0, 6), random.randint(0, 6)

def play_again():
    try_again = input("Сыграть снова? <Y>es or <N>o? >: ").lower()
    if try_again == "y":
        play_game()
    else:
        print("bye!")
        return

print("Добро пожаловать в игру, у вас есть 10 патронов, а на карте спрятаны 3 корабля. Чтобы попасть в них, вы должны ввести конкретные цифры для этого местоположения")

def play_game():
    game_board = [["O", "O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O", "O"]]

    for i in game_board:
        print(*i)

    ship1 = create_random_ship()
    ship2 = create_random_ship()
    ship3 = create_random_ship()
    ships_left = 8
    ammo = 12

    while ammo:
        try:
            row = int(input("Введите число строки от 1 до 6: "))
            column = int(input("Введите число столбца от 1 до 6: "))
        except ValueError:
            print("Можно ввести только число")
            continue

        if row not in range(1, 7) or column not in range(1, 7):
            print("\nЧисло должно быть в диапазоне 1-6")
            continue

        row = row - 1 # Приведение числа к нужному показателю.
        column = column - 1 # Приведение числа к нужному показателю.

        if game_board[row][column] == "-" or game_board[row][column] == "X":
            print("\nУже стреляли в это место\n")
            continue
        elif (row, column) == ship1 or (row, column) == ship2 or (row, column) == ship3:
            print("\nВы попали!!\n")
            game_board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print("Ты победил!")
                play_again()
        else:
            print("\nПромах!\n")
            game_board[row][column] = "-"
            ammo -= 1

        for i in game_board:
            print(*i)

        print(f"Осталось патронов: {ammo} | Осталось кораблей: {ships_left}")

    play_again()


if __name__ == "__main__":
    play_game()