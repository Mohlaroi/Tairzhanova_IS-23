#Создайте класс «Календарь», который имеет атрибуты год, месяц и день.
# Добавьте методы для определения дня недели, проверки на високосный год
# и определения количества дней в месяце.
#Для задачи из блока 1 создать две функции, save_def и load_def,
# которые позволяют сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в бинарном формате.
import pickle
from calendar import monthrange, weekday, isleap
class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def day_week(self):
        return weekday(self.year, self.month, self.day)

    def visokosni(self):
        return isleap(self.year)

    def days_month(self):
        return monthrange(self.year, self.month)[1]

years = int(input("Введите год: "))
month = int(input("Введите месяц (1-12): "))
day = int(input("Введите день (1-31): "))

calendar = Calendar(years, month, day)

print("День недели:", calendar.day_week())
print("Високосный год:", calendar.visokosni())
print("Дней в месяце:", calendar.days_month())

def save_def(objects, filename):
    with open(filename, 'wb') as f:
        pickle.dump(objects, f)


def load_def(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


calendar1 = Calendar(2023, 3, 8)
calendar2 = Calendar(2024, 2, 29)
calendar3 = Calendar(2025, 12, 31)

save_def([calendar1, calendar2, calendar3], 'calendar_data.dat')

loaded_calendars = load_def('calendar_data.dat')
for calendar in loaded_calendars:
    print(f"Дата: {calendar.year}-{calendar.month}-{calendar.day}")
    print(f"День недели: {calendar.day_week()}")
    print(f"Високосный год: {calendar.visokosni()}")
    print(f"Количество дней в месяце: {calendar.days_month()}\n")