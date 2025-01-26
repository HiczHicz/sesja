def analiza():
    with open('pytania.txt', 'r') as plik:
        pytania=plik.readlines()
    import random
    tekst.configure(text=random.choice(pytania), fg='VioletRed4')

def algebra():
    with open('algebra.txt', 'r') as plik:
        pytania=plik.readlines()
    import random
    tekst.configure(text=random.choice(pytania), fg='darkgreen')

def stop():
    okno.destroy()

from tkinter import *
okno=Tk()
okno.title("Losowanie pytań")
okno.geometry("600x300")

okno.update_idletasks()
szerokosc_okna = 600
wysokosc_okna = 300
szerokosc_ekranu = okno.winfo_screenwidth()
wysokosc_ekranu = okno.winfo_screenheight()

# Obliczenie pozycji
x = (szerokosc_ekranu - szerokosc_okna) // 2
y = (wysokosc_ekranu - wysokosc_okna) // 2
okno.geometry(f"{szerokosc_okna}x{wysokosc_okna}+{x}+{y}")  # Ustawienie pozycji na środku

# Ustawienie okna na wierzchu
okno.attributes("-topmost", True)

tekst=Label(okno, text='Sesja, huh? Wybierz przedmiot, a w tym miejscu pojawi się pytanie!', justify=CENTER,
            height=6, wraplength=480)
tekst.pack(pady=20)

al = Button(text='Algebra', command=algebra, fg='darkgreen')
al.pack()

am = Button(text='Analiza', command=analiza, fg='VioletRed4')
am.pack()

koniec = Button(text='Koniec', command=stop)
koniec.pack()

okno.mainloop()