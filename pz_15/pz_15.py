# приложение ХИМЧИСТКА для некоторой организации.
# БД должна содержать таблицу Услуги со следующей структурой записи:
# ФИО мастера, ФИО клиента, тип чистики, стоимость, скидкa
import sqlite3
conn = sqlite3.connect('химчистка.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS uslugi
                  (FIO_master TEXT,
                   FIO_client TEXT,
                   type_chistci TEXT,
                   cost REAL,
                   discount REAL)''')
conn.commit()

def input_data():
  data = []
  for _ in range(3):
    FIO_master = input("ФИО мастера: ")
    FIO_client = input("ФИО клиента: ")
    type_chistci = input("Тип чистки: ")
    cost = float(input("Стоимость: "))
    discount = float(input("Скидка: "))
    data.append((FIO_master, FIO_client, type_chistci, cost, discount))
    cursor.executemany("INSERT INTO uslugi VALUES (?, ?, ?, ?, ?)", data)
  conn.commit()

def search_data():
  print("Варианты поиска:")
  print("1. По ФИО мастера")
  print("2. По ФИО клиента")
  print("3. По типу чистки")
  change = input("Выберите вариант поиска: ")
  if change == '1':
    FIO_master = input("ФИО мастера: ")
    cursor.execute("SELECT * FROM uslugi WHERE FIO_master=?", (FIO_master,))
  elif change == '2':
    FIO_client = input("ФИО клиента: ")
    cursor.execute("SELECT * FROM uslugi WHERE FIO_client=?", (FIO_client,))
  elif change == '3':
    type_chistci = input("Тип чистки: ")
    cursor.execute("SELECT * FROM uslugi WHERE type_chistci=?", (type_chistci,))
  else:
    print("Неверный выбор")
    return
  res = cursor.fetchall()
  if res:
    for zapis in res:
      print(zapis)
  else:
    print("Записи нет")

def delete_data():
  print("Варианты удаления:")
  print("1. По ФИО мастера")
  print("2. По ФИО клиента")
  print("3. По типу чистки")
  change = input("Выберите вариант удаления: ")
  if change == '1':
    FIO_master = input("ФИО мастера: ")
    cursor.execute("DELETE FROM uslugi WHERE FIO_master=?", (FIO_master,))
  elif change == '2':
    FIO_client = input("ФИО клиента: ")
    cursor.execute("DELETE FROM uslugi WHERE FIO_client=?", (FIO_client,))
  elif change == '3':
    type_chistci = input("Тип чистки: ")
    cursor.execute("DELETE FROM uslugi WHERE type_chistci=?", (type_chistci,))
  else:
    print("Нет такого значения")
    return
  conn.commit()
  print("Записи удалены")

def update_data():
  print("Варианты редактирования:")
  print("1. По ФИО мастера")
  print("2. По ФИО клиента")
  print("3. По типу чистки")
  change = input("Выберите вариант редактирования: ")
  if change == '1':
    FIO_master = input("ФИО мастера (для поиска записи): ")
    new_znach = input("Новое значение стоимости: ")
    cursor.execute("UPDATE uslugi SET cost=? WHERE FIO_master=?", (new_znach, FIO_master))
  elif change == '2':
    FIO_client = input("ФИО клиента (для поиска записи): ")
    new_znach = input("Новое значение скидки: ")
    cursor.execute("UPDATE uslugi SET discount=? WHERE FIO_client=?", (new_znach, FIO_client))
  elif change == '3':
    type_chistci = input("Тип чистки (для поиска записи): ")
    new_znach = input("Новое значение ФИО мастера: ")
    cursor.execute("UPDATE uslugi SET FIO_master=? WHERE type_chistci=?", (new_znach, type_chistci))
  else:
    print("Неверный выбор")
    return
  conn.commit()
  print("Запись изменена")


while True:
  print("\nМеню:")
  print("1. Ввод данных")
  print("2. Поиск данных")
  print("3. Удаление данных")
  print("4. Редактирование данных")
  print("5. Выход")
  change = input("Выберите действие: ")
  if change == '1':
     input_data()
  elif change == '2':
    search_data()
  elif change == '3':
    delete_data()
  elif change == '4':
    update_data()
  elif change == '5':
    break
  else:
    print("Неверный выбор.")

conn.close()
