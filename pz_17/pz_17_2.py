#Задание предполагает, что у студента есть проект с практическими работами (NoNo 2-13), оформленный согласно требованиям.
#Все задания выполняются c использованием модуля OS:
#перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена вложенных подкаталогов выводить не нужно.
#перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку test1.
# В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
#Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере файлов в папке test.
#перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в консоль.
# Использовать функцию basename () (os.path.basename()).
#перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в привязанной к нему программе.
#Использовать функцию os.startfile().
#удалить файл test.txt.
import os
import subprocess

project_root = "/Users/mahisabirova/Documents/программирование"


pz11_path = os.path.join(project_root, "pz_11")
os.chdir(pz11_path)

print("Файлы в каталоге pz_11:")
for filename in os.listdir():
    if os.path.isfile(filename):
        print(filename)


test_dir = os.path.join(project_root, "test")
test1_dir = os.path.join(test_dir, "test1")
os.makedirs(test1_dir, exist_ok=True)


os.rename(os.path.join(project_root, "pz_6/pz_6_1.py"), os.path.join(test_dir, "pz_6_1.py"))
os.rename(os.path.join(project_root, "pz_6/pz_6_2.py"), os.path.join(test_dir, "pz_6_2.py"))
os.rename(os.path.join(project_root, "pz_7/pz_7_1.py"), os.path.join(test1_dir, "test.txt"))

print("\nРазмер файлов в папке test:")
for filename in os.listdir(test_dir):
    filepath = os.path.join(test_dir, filename)
    size = os.path.getsize(filepath)
    print(f"{filename}: {size} байт")

os.chdir(pz11_path)
shortest_filename = min(os.listdir(), key=len)
print(f"\nФайл с самым коротким именем в pz_11: {os.path.basename(shortest_filename)}")


pdf_path = os.path.join(project_root, "pz_10/отчет по пз10.pdf")
subprocess.call(['open', pdf_path])

os.remove(os.path.join(test1_dir, "test.txt"))

