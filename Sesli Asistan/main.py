from komutlar import Komut
import speech_recognition as sr
import pygame
from tkinter import *
import tkinter as tk




def sesCal():
    # Bip müzik dosyasında bulunan sesi çalar.
    # Bu ses mikrofonun aktif hale geldiğini kullanıcıya bildirmiş olur.
    pygame.mixer.init()
    pygame.mixer.music.load("bip.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


def asistan():
    try:
        global root
        root.destroy()
    except:
        pass
    while True:
        sesCal()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, phrase_time_limit=6)
        try:
            data = ""
            data = r.recognize_google(audio, language='tr-TR')
            print(data)
            komut = Komut(data)
            komut.komutBul()
        except sr.UnknownValueError:
            i = "geçici"
            komut = Komut(i)
            komut.konusma("Anlayamadım")
        except sr.RequestError:
            i = "geçici"
            komut = Komut(i)
            komut.konusma("Sistem çalışmıyor")

def pencere2():
    pencere2 = tk.Toplevel()
    pencere2.geometry("1350x750")
    bg2 = PhotoImage(file="pencere2.png")
    label2 = Label(pencere2, image=bg2)
    label2.place(x=0, y=0)

    pencere2.mainloop()

pencere = tk.Tk()
pencere.geometry("1680x850")

bg = PhotoImage(file="resim3.png")
label1 = Label(pencere, image=bg)
label1.place(x=0, y=0)

resim = PhotoImage(file = r'kırp.png')
dugme1=tk.Button(pencere,text="Asistan", command=asistan, image=resim, width=125, height=160)
dugme1.place(x=1422, y=627)
resim2 = PhotoImage(file = r'kırp2.png')
dugme2=tk.Button(pencere,text="pencere2", command=pencere2, image=resim2, width=125, height=160)
dugme2.place(x=100, y=627)

pencere.mainloop()