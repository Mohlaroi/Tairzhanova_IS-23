#Дано целое число N (>0).
# Найти произведение 1.1 • 1.2 • 1.3 •...
# (N сомножителей).

N = input('Введите целое число: ')
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Введите целое число: ')
        N = input('Введите целое число: ')
res = 1.1
K = 1.2
if N > 0:
    N = int(N)
    while N != 1:
        res = res + N
        K += 0.1
        N -= 1
    print('результат: ', res)
else:
    print('число не подходит')



