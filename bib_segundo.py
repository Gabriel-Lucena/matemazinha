import math
from decimal import Decimal


def verificar_soma(a, b):
    c = a + b

    if c < 0:
        print('Deu Ruim')
    elif c > 0:
        print('Deu bom')
    else:
        print('Deu meio')

    print('--------------')


def verificar_se_e_inteiro(numero_real):

    if isinstance(numero_real, int):

        return True

    else:

        return False


def interface_terminal_com_segundo_grau():

    print('Digite os coeficientes da função:')
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    segundo_grau_melhorada(a, b, c)


def simplificar_raiz(raiz):

    if isinstance(raiz ** 0.5, int):

        raiz = raiz ** 0.5

        return round(raiz)

    else:

        return raiz


def calcular_delta(a, b, c):

    delta = b ** 2 - 4 * a * c

    return delta


def verificar_idade(idade):

    if idade < 12:
        print('criança')
    elif idade < 18:
        print('adolescente')
    elif idade < 60:
        print('adulto')
    else:
        print('idoso')

    print('----------------------')


def segundo_grau_calcular_raiz_1(a, b, c):

    raiz_1 = (-b - math.sqrt(calcular_delta(a, b, c))) / (2 * a)

    return raiz_1


def segundo_grau_calcular_raiz_2(a, b, c):

    raiz_2 = (-b + math.sqrt(calcular_delta(a, b, c))) / (2 * a)

    return raiz_2


def segundo_grau_convertido_raiz_1(a, b, c):

    x1_convertido = Decimal(segundo_grau_calcular_raiz_1(a, b, c))

    return x1_convertido


def segundo_grau_convertido_raiz_2(a, b, c):

    x2_convertido = Decimal(segundo_grau_calcular_raiz_2(a, b, c))

    return x2_convertido


def segundo_grau_comparar_raizes(a, b, c):

    if segundo_grau_calcular_raiz_1(a, b, c) == segundo_grau_convertido_raiz_1(a, b, c) and segundo_grau_calcular_raiz_2(a, b, c) == segundo_grau_convertido_raiz_2(a, b, c):

        print('Há duas raízes diferentes:')
        print('x_1')
        print(segundo_grau_convertido_raiz_1(a, b, c))
        print('x_2')
        print(segundo_grau_convertido_raiz_2(a, b, c))

        return True

    else:

        print('Há duas raízes diferentes:')
        print('x_1')
        print(segundo_grau_calcular_raiz_1(a, b, c))
        print('x_2')
        print(segundo_grau_calcular_raiz_2(a, b, c))

        return False


def segundo_grau_calcular_raizes_complexas(a, b, c):

    delta_negativo = -calcular_delta(a, b, c)

    raiz_1 = (-b) / (2 * a)
    raiz_complexa_1 = (- math.sqrt(delta_negativo)) / (2 * a)
    raiz_2 = (-b) / (2 * a)
    raiz_complexa_2 = (+ math.sqrt(delta_negativo)) / (2 * a)

    print('Há duas raízes complexas:')
    print('x_1')
    print(' Parte real:', raiz_1)
    print(' Parte imaginária:', raiz_complexa_1)
    print('x_2')
    print(' Parte real:', raiz_2)
    print(' Parte imaginária:', raiz_complexa_2)

    return delta_negativo


def segundo_grau_calcular_raiz(a, b):

    # Versão simplificada em que se mostra somente o resultado em decimais

    raiz = (-b) / (2 * a)
    raiz_convertida = Decimal(raiz)

    if raiz == raiz_convertida:

        print('Há duas raízes iguais ou somente uma raiz:')
        print('x')
        print(raiz_convertida)

    else:

        print('Há duas raízes iguais ou somente uma raiz:')
        print('x')
        print(raiz)


def segundo_grau(a, b, c):

    # Delta maior que 0

    if calcular_delta(a, b, c) > 0:

        segundo_grau_comparar_raizes(a, b, c)

    # Delta menor que 0

    elif calcular_delta(a, b, c) < 0:

        segundo_grau_calcular_raizes_complexas(a, b, c)

    # Delta igual a 0

    else:

        segundo_grau_calcular_raiz(a, b)

    print('----------------------')

# Versão melhorada
# Aparece a resposta como se fosse feito à mão


def segundo_grau_melhorada(a, b, c):

    if calcular_delta(a, b, c) == 0:

        print('Há duas raízes iguais reais ou uma raiz real:')
        print('x_1:')
        print(-1 * b)
        print('----')
        print(' ', 2 * a, ' ')
        print('x_2:')
        print(-1 * b)
        print('----')
        print(' ', 2 * a, ' ')

    elif calcular_delta(a, b, c) > 0:

        if verificar_se_e_inteiro(simplificar_raiz(calcular_delta(a, b, c))) == True:

            print('Há duas raízes diferentes e reais:')
            print('x_1:')
            print(-1 * b, ' - ', calcular_delta(a, b, c) ** 0.5)
            print('--------------------------')
            print('         ', 2 * a, '        ')
            print('x_2:')
            print(-1 * b, ' + ', calcular_delta(a, b, c) ** 0.5)
            print('--------------------------')
            print('         ', 2 * a, '        ')

        else:

            print('Há duas raízes diferentes e reais:')
            print('x_1:')
            print(-1 * b, ' - sqrt(', calcular_delta(a, b, c), ')')
            print('--------------------------')
            print('         ', 2 * a, '        ')
            print('x_2:')
            print(-1 * b, ' + sqrt(', calcular_delta(a, b, c), ')')
            print('--------------------------')
            print('         ', 2 * a, '        ')

    else:

        print('Há duas raízes complexas conjugadas:')
        print('x_1:')
        print(-1 * b, ' - sqrt(', abs(calcular_delta(a, b, c)), ') i')
        print('--------------------------')
        print('         ', 2 * a, '        ')
        print('x_2:')
        print(-1 * b, ' + sqrt(', abs(calcular_delta(a, b, c)), ') i')
        print('--------------------------')
        print('         ', 2 * a, '        ')

    print('----------------------')


def exibir_maximo_ou_minimo(a, b, c):

    if a == 0:

        print('--------------------------------------')
        print('Esta não é uma função polinomial do segundo grau.')
        print('--------------------------------------')

    elif a > 0:

        print('--------------------------------------')
        print('A abscissa do ponto mínimo é:')
        print(determinar_ponto_do_maximo_ou_minimo(a, b, c)[0])
        print('--------------------------------------')

    else:

        print('--------------------------------------')
        print('A abscissa do ponto máximo é:')
        print(determinar_ponto_do_maximo_ou_minimo(a, b, c)[0])
        print('--------------------------------------')


def determinar_ponto_do_maximo_ou_minimo(a, b, c):

    if a == 0:

        return False

    else:

        abscissa_maximo_ou_minimo = - b * (2 * a) ** -1

        ordenada_do_ponto_maximo = -1 * calcular_delta(a, b, c) * (4 * a) ** -1

        ponto_do_maximo_minimo = [
            abscissa_maximo_ou_minimo, ordenada_do_ponto_maximo]

        return ponto_do_maximo_minimo


def teste_de_concavidade(a):

    if a == 0:

        return False

    elif a > 0:

        return 'A função tem a concavidade voltada para cima.'

    else:

        return 'A função tem a concavidade voltada para baixo.'


def area_sob_uma_equacao_do_segundo_grau_num_intervalo_fechado(a, b, c, x_1, x_2):

    if a == 0:

        return False

    else:

        area = (a * x_2 ** 3 - a * x_1 ** 3) / 3 + \
            (b * x_2 ** 2 - b * x_1 ** 2) / 2 + c * x_2 - c * x_1

        return area


def area_sob_equacao_do_segundo_grau(a, b, c):

    area = area_sob_uma_equacao_do_segundo_grau_num_intervalo_fechado(
        a, b, c, segundo_grau_calcular_raiz_1(a, b, c), segundo_grau_calcular_raiz_2(a, b, c))

    print('--------------------------------------')
    print('A área sob a função é:')
    print('--------------------------------------')
    print(area)
    print('--------------------------------------')


def teste_vetores(numero):

    vetor = [numero, numero ** 2]

    return vetor
