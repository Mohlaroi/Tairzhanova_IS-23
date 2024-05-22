#Разработать программу с применением пакета tk,
# взяв в качестве условия одну любую задачу из ПЗ №2-9.
import tkinter as tk
def calculate():
    global res
    K = entry.get()
    while type(K) != int:
        try:
            K = int(K)
            weekday_jan = 1
            res = (K - 1 + weekday_jan) % 7
            result_label.config(text=res)
            break
        except ValueError:
            result_label.config(text="Введите число")
            K = entry.get()

window = tk.Tk()
window.title("Определение дня недели")

label = tk.Label(window, text="Введите число от 1 до 365: ")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

calculate_button = tk.Button(window, text="Рассчитать", command=calculate)
calculate_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()