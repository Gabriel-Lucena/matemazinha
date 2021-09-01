from bib import segundo_grau_melhorada
from bib import teste_de_concavidade
from bib import determinar_abscissa_do_ponto_maximo_ou_minimo
from bib import determinar_ordenada_do_ponto_maximo_ou_minimo


class FuncaoSegundoGrau:

    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

    def encontrar_raizes(self):

        print('--------------------------------------')
        segundo_grau_melhorada(self.a, self.b, self.c)
        print('--------------------------------------')
        
    def encontrar_concavidade(self):

        print('--------------------------------------')
        print(teste_de_concavidade(self.a))
        print('--------------------------------------')

    def encontrar_ponto_de_maximo_ou_minimo(self):

        print('--------------------------------------')
        print('A abscissa:')
        print(determinar_abscissa_do_ponto_maximo_ou_minimo(self.a, self.b))
        print('A ordenada:')
        print(determinar_ordenada_do_ponto_maximo_ou_minimo(self.a, self.b, self.c))
        print('--------------------------------------')
