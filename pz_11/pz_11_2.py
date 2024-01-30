# Из предложенного текстового файла (text18-29.txt)
# вывести на экран его содержимое, количество символов в тексте.
# Сформировать новый файл, в который поместить текст в
#стихотворной форме предварительно поставив последнюю
# строку между второй и третьей.

with open('text18-29.txt','r', encoding='utf-16')as file:
    ls = file.readlines()
    txt = "".join(ls)
    print("Изначальный текст:")
    print(txt)
    print(f"количество символов: {len(txt)}")
    last = ls.pop()
    ls.insert(2, last)

with open("new_text.txt", "w", encoding='utf-16') as new_file:
    new_file.writelines(ls)

