#Организовать и вывести последовательность на N произвольных целых
#элементов, сформировать новую последовательность куда поместить
#положительные четные элементы, найти их сумму и среднее арифметическое.
import random
from statistics import mean

N = int(input('задайте количество элементов: '))
seq = [random.randint(-100, 100) for num in range(N)]
poloz = [num for num in seq if num > 0 and num % 2 == 0]
summ = sum(poloz)
srednee = mean(poloz)

print("Сгенерированная последовательность из", N, "элементов:", seq)
print("Положительные четные элементы:", poloz)
print("Сумма положительных четных элементов:", summ, "Среднее арифметическое:", srednee)