#Описать функцию Swap(X, Y),
# меняющую содержимое переменных Х и Y
# (Х и Y = вещественные параметры,
# являющиеся одновременно входными и выходными).
# С ее помощью для данных переменных А, B, C, D
# последовательно поменять содержимое следующих пар:
# А и В, С и D, В и С и вывести новые значения А, В, С, D.

def Swap(X, Y):
    return Y, X

A = input('Введите целое число: ')
B = input('Введите целое число: ')
C = input('Введите целое число: ')
D = input('Введите целое число: ')

A, B = Swap(A, B)
C, D = Swap(C, D)
B, C = Swap(B, C)
print('новые значения переменных: ')
print('A = ', A)
print('B = ', B)
print('C = ', C)
print('D = ', D)
