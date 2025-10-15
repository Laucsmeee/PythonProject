import tkinter as tk

def on_click():
    try:
        celsius = float(entry.get())
        fahrenheit = celsius * 1.8 + 32
        result_label.config(text=f"{celsius:.2f} °C = {fahrenheit:.2f} °F")
    except ValueError:
        result_label.config(text="❌ Введи правильне число!")

def on_click2():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32.0) / 1.8
        result_label.config(text=f"{fahrenheit:.2f} °F = {celsius:.2f} °c")
    except ValueError:
        result_label.config(text="❌ Введи правильне число!")



root = tk.Tk()
root.title("Моє перше вікно")
root.geometry("500x400")  # ширина x висота

entry_label = tk.Label(root, text="Введи температуру")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

label = tk.Label(root, text="Натисни кнопку 👇")
label.pack(pady=10)

button = tk.Button(root, text="°C → °F", command=on_click)
button.pack(pady=10)
button2 = tk.Button(root, text="°F → °C", command=on_click2)
button2.pack(pady=10)

result_label = tk.Label(root, text="Результат з'явиться тут")
result_label.pack(pady=10)



# Запускаємо головний цикл
root.mainloop()