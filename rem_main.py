from cProfile import label
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import pygame


def sett():
    rem=sd.askstring("Время напоминания",
                     "Введите напоминания время в формате ЧЧ:ММ")
    if rem:
        try:
            hour=int(rem.split(":")[0])
            minute=int(rem.split(":")[1])
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour,minute=minute)
            print(dt)
            dt=now.replace(hour=hour,minute=minute)
            print(dt)
            t=dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка {e}")



window = Tk()
window.title("Напоминальщик")
label=Label(text="Установите напоминание")
label.pack(pady=10)
set_button=Button(text="Установить напоминание", command=sett)
set_button.pack(pady=10)


window.mainloop()


