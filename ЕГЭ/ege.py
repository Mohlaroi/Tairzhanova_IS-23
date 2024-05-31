#В файле содержится последовательность натуральных чисел.
#Её элементы могут принимать целые значения от 1 до 100 000 включительно.
#Определите количество пар последовательности,
# которых хотя бы одно число делится на минимальный элемент последовательности, кратный 19.
# Гарантируется, что такой элемент в последовательности есть.
# В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
count = 0
maxi = 0
file = open('1_17.txt')
list = [int(i) for i in file]
cratni = min([x for x in list if x % 19 == 0])
for i in range(len(list) - 1):
    if (list[i] % cratni == 0) or (list[i+1] % cratni == 0):
            count += 1
            maxi = max(maxi, list[i] + list[i+1])
print(count, maxi)