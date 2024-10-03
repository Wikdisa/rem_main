import time
from cProfile import label
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import pygame

t = None
music = False

def set():
    global t
    rem=sd.askstring("Время напоминания",
                     "Введите напоминания время в формате ЧЧ:ММ")
    if rem:
        try:
            hour=int(rem.split(":")[0])
            minute=int(rem.split(":")[1])
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour,minute=minute, second=0, microsecond=0)
            label.config(text=f"Напоминание установлено на: {hour:02}:{minute:02}")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка {e}")

def check():
    global t
    if t:
        now=time.time()
        if now>=t:
            play_snd()
            t=0
    window.after(10000, check)

def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("zvuk.mp3")
    pygame.mixer.music.play()

def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text="Установить напоминание")

t=0


window = Tk()
window.title("Напоминальщик")
label=Label(text="Установите напоминание")
label.pack(pady=10)
set_button=Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)
stop_button = Button(text="Остановить музыку", command=stop_music)
stop_button.pack(pady=5)

check()


window.mainloop()


