# Реалізувати код для підрахунку кількості можливих маршрутів для доставки N клієнтам.


def Routes(n):
    if n <= 0 or n == 1:
        return 1
    else:
        return n * Routes(n - 1)

print(Routes(int(input("Напишитоь кількості можливих маршрутів для доставки N клієнтам: ")))) 