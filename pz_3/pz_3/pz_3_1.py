#даны числа х,у, х1, у1, х2, у2.
#Проверить истинность высказывания:
# «Точка с координатами (х, у) лежит внутри прямоугольника,
# левая верхняя вершина которого имеет координаты (х1, у), правая нижняя (x2, у2),
# а стороны параллельны координатным осям».
# Определить, какая из двух последних точек (В или С) расположена ближе к А,
# и вывести эту точку и ее расстояние от точки А

x = input('Введите целое число: ')
y = input('Введите целое число: ')
x1 = input('Введите целое число: ')
y1 = input('Введите целое число: ')
x2 = input('Введите целое число: ')
y2 = input('Введите целое число: ')
while type(x) != int:
    try:
        x = int(x)
    except ValueError:
        print('Введите целое число: ')
        x = input()
while type(y) != int:
    try:
        y = int(y)
    except ValueError:
        print('Введите целое число: ')
        y = input()
while type(x1) != int:
    try:
        x1 = int(x1)
    except ValueError:
        print('Введите целое число: ')
        x1 = input()
while type(y1) != int:
    try:
        y1 = int(y1)
    except ValueError:
        print('Введите целое число: ')
        y1 = input()
while type(x2) != int:
    try:
        x2 = int(x2)
    except ValueError:
        print('Введите целое число: ')
        x2 = input()
while type(y2) != int:
    try:
        y2 = int(y2)
    except ValueError:
        print('Введите целое число: ')
        y2 = input()
if (x1 < x < x2) and (y1 > y > y2):
    print('входит в прямоугольник: ')
else:
    print("не входит в прямоугольник ")

# На числовой оси расположены три точки:
# А, В, С. Определить, какая из двух последних точек (В или С)
# расположена ближе к А, и вывести эту точку и eе расстояние от точки А.

a = input('Введите целое число: ')
b = input('Введите целое число: ')
c = input('Введите целое число: ')
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

ab = abs(a - b)
ac = abs(a - c)
if ac < ab:
    print(' a ближе ')
if ac > ab:
    print(' b ближе ')
if ac == ab:
    print(' на одинаковом расстоянии ')
