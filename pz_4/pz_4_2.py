#Даны положительные числа А, В, С.
# На прямоугольнике размера А х В
# размещено максимально возможное количество
# квадратов со стороной С (без наложений).
# Найти количество квадратов, размещенных на прямоугольнике.
#Операции умножения и деления не использовать.
a = input('Введите целое число: ')
b = input('Введите целое число: ')
c = input('Введите целое число: ')
K = -1
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Введите целое число: ')
        a = input()
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Введите целое число: ')
        b = input()
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print('Введите целое число: ')
        c = input()
while a - c >= 0:
    a = a - c
    K = K + 1
    while b - c >= b:
        b = b - c
        K = K + 1
print(' количество квадратов: ' + str(K))