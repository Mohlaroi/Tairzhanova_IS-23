#Составить генератор (yield), который преобразует
# все буквенные символы в строчные.
def generator(yieldd):
    for el in yieldd:
        if el.isalpha():
            yield el.lower()
        else:
            yield el
str = input('введите элемент: ')
lowercas = ''.join(generator(str))

print(lowercas)