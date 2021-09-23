from bib_segundo import determinar_ponto_do_maximo_ou_minimo, segundo_grau_melhorada, teste_de_concavidade


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
        print(determinar_ponto_do_maximo_ou_minimo(self.a, self.b, self.c)[0])
        print('A ordenada:')
        print(determinar_ponto_do_maximo_ou_minimo(self.a, self.b, self.c)[1])
        print('--------------------------------------')
