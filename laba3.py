#Дружинина Дарья R3142 412936
import tkinter as tk
import random
import string

def close():
    window.destroy()
def generate_key():
    key = ''
    block_sum = 0
    block_size = 0

    while len(key) < 15:
        # Сгенерируем случайный символ
        symbol = random.choice(string.ascii_uppercase + string.digits)

        # Получим весовой коэффициент для символа
        weight = get_symbol_weight(symbol)

        # Проверим, если добавление символа не превышает заданный интервал
        if block_sum + weight <= 9:
            key += symbol
            block_sum += weight
            block_size += 1

        # Если добавление символа приводит к превышению заданного интервала, то сбросим блок
        else:
            block_sum = 0
            block_size = 0

    # Форматируем ключ в требуемый формат
    formatted_key = f"{key[:5]}-{key[5:9]}-{key[:4]}"
    key_field.delete(0, tk.END)
    key_field.insert(0, formatted_key)
def get_symbol_weight(symbol):
    return 1

window = tk.Tk()
window.geometry('750x422')
bg_img = tk.PhotoImage(file='mario.png')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

key_field = tk.Entry(window, font=("Arial", 16))
key_field.pack(pady=150)

btn_calc = tk.Button(frame, text='Calculate', command=generate_key)
btn_calc.grid(column=0, row=3, padx=10, pady=15)
btn_exit = tk.Button(frame, text='Cancel', command=close)
btn_exit.grid(column=2, row=3, padx=10, pady=15)

window.mainloop()