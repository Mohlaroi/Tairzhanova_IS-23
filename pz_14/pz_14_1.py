#В исходном текстовом файле(hotlinel.txt) найти всеномера телефонов,
# соответствующих шаблону 8(000)000-00-00. Посчитать количество полученных элементов.
# После фразы «Горячая линия» добавить фразу «Министерства образования Ростовской области»,
# выполнив манипуляции в новом файле.

import re
def number(hotline):
    nomera = r'\b\d{10}\b|\b\d{11}\b|\b\d{9}-\d{2}\b'
    count = 0
    for phone_number in re.findall(nomera, hotline):
        yield phone_number
        count  += 1
    return count
with open('hotline.txt', 'r', encoding='utf-8') as file:
    data = file.read()

gener = number(data)

new_word = data.replace('«Горячая линия»','«Горячая линия Министерства образования Ростовской области»')

with open('new_hotline.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(new_word)
count_number = sum(1 for _ in gener)
print("данные в новом файле")
print('количество найденных номеров: ', count_number)