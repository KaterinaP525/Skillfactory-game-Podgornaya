field = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
# применение функции draw_field для вывода поля
# применение end='', чтобы значения не переносились на следующую строку
def draw_field(field):
    print(field[0], end=" ")
    print(field[1], end=" ")
    print(field[2])

    print(field[3], end=" ")
    print(field[4], end=" ")
    print(field[5])

    print(field[6], end=" ")
    print(field[7], end=" ")
    print(field[8])


# для возврата значения из take_input
def take_input(symbol):
    show = False
    while not show:
        step = input("Ход " + symbol + "? ")
        try: # обработать исключения ввода чисел
            step = int(step)
        except ValueError:
            print("Ввод предполагает только числа от 1 до 9")
            continue

        if 1 <= step <= 9:
            if str(field[step - 1]) not in "OX":
                field[step - 1] = symbol
                show = True
            else:
                print("Позиция занята")
        else:
            print("Введите число в диапазоне от 1 до 9")

def check_win(field):
    # Фиксирование выигрышных комбинаций
    victories = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]

    for each in victories:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False


def main(field):
    counter = 0
    win = False
    while not win:
        draw_field(field)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        tmp = check_win(field)
        if tmp:
            print(tmp, "выиграл")
            win = True
            break
        if counter == 9:
            print("Ничья")
            break
    draw_field(field)


main(field)

input("Конец игры")
