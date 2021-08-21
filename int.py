import math
from decimal import Decimal
from tkinter import *
from bib import *

janela = Tk()
janela.title("Triangulos")

texto_orientacao = Label(janela, text = "Clique no botão para ver a cotação das moedas" )
texto_orientacao.grid(column=0,row=0)

butao = Button(janela, text="Calcular", command=triangulo_sem_angulo)
butao.grid(column=0,row=1)

janela.mainloop()