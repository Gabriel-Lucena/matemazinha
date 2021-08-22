import math
from decimal import Decimal
from tkinter import *
from bib import *

janela = Tk()
janela.title("Ματεμα")

janela.geometry('1000x1000+50+50')
janela.resizable(True, True)
janela.iconbitmap('img/favicon.ico')

texto_orientacao = Label(janela, text = "Raízes de uma equação do segundo grau:", font=("Helvetica", 16))
texto_orientacao.place(x=475,y=250)

label_1 = Label(janela, text='Digite aqui os coeficientes:', font=("Helvetica", 14))
label_1.place(relx=0, rely=0.2, relwidth=0.5, anchor='ne')

campo_de_texto_a = Text(janela, height=8, font=("Helvetica", 10))
campo_de_texto_a.place(x=475,y=300)


butao = Button(janela, text="Calcular", command=triangulo_sem_angulo, font=("Helvetica", 10))


janela.mainloop()