#Дружинина Дарья R3142 412936
import tkinter as tk
from random import randint

def close():
    window.destroy()
def key(m,M):
    letters_list = '0123456789abcdefghijklmnopqrstuvwxyz'
    len(letters_list)
    s=0
    code = ''
    codes = ''
    for i in range(3):
        while True:
            a = randint(0, len(letters_list)-1)
            if (a+s)<M:
                s += a
                code += str(a)
                codes += letters_list[a]
                break
    while True:
        a=randint(0, len(letters_list)-1)
        if ((a+s)>m) and ((a+s)<M):
            s += a
            code += str(a)
            codes += letters_list[a]
            break
    return(codes)
def generate_key():
    global answer
    letters_list = '0123456789abcdefghijklmnopqrstuvwxyz'
    blok1 = ''
    for i in range(5):
        blok1 += letters_list[randint(0, len(letters_list)-1)]
    blok1 += '-'
    blok2 = ''
    for i in range(4):
        blok2 += letters_list[randint(0, len(letters_list)-1)]
    blok2 += '-'
    blok3 = key(30,120)
    answer = blok1 + blok2 + blok3
    canvas.itemconfig(key_canvas, text=answer)

window = tk.Tk()
canvas = tk.Canvas(window, width=750, height=422)
canvas.pack()

image = tk.PhotoImage(file="mario.png")
canvas.create_image(0, 0, anchor=tk.NW, image=image)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

btn_calc = tk.Button(frame, text='Calculate', command=generate_key)
btn_calc.grid(column=0, row=3, padx=10, pady=15)
btn_exit = tk.Button(frame, text='Cancel', command=close)
btn_exit.grid(column=2, row=3, padx=10, pady=15)

key_canvas = canvas.create_text(375, 50, text="Генерация ключа", fill="red", font=('Arial 30 bold'))

window.mainloop()
