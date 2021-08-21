import math
from decimal import Decimal

def classificar_triangulo_pelos_lados(lado_a,lado_b,lado_c):

    if lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:

        print('--------------------------------------')
        print('O triângulo é isóceles.')
        print('--------------------------------------')

    elif lado_a == lado_b and lado_b == lado_c and lado_c == lado_a:

        print('--------------------------------------')
        print('O triângulo é equilátero.')
        print('--------------------------------------')

    elif lado_a != lado_b and lado_c != lado_a and lado_c != lado_a:

        print('--------------------------------------')
        print('O triângulo é escaleno.')
        print('--------------------------------------')

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

    if isinstance(numero_real,int):

        return True

    else:

        return False

def verificar_se_triangulo_existe(lado_a,lado_b,lado_c,angulo_a,angulo_b,angulo_c):
    
    if math.fabs(lado_b - lado_c) < lado_a < lado_b + lado_c and math.fabs(lado_a - lado_c) < lado_b < lado_a + lado_c and math.fabs(lado_a - lado_b) < lado_c < lado_b + lado_a and angulo_a + angulo_b + angulo_c == 180:
      
        print('--------------------------------------')
        print('O triângulo existe.')
        print('--------------------------------------')

        return True

    else:

        print('--------------------------------------')
        print('Estas medidas não são de um triângulo.')
        print('--------------------------------------')

        return False

def verificar_se_triangulo_e_retangulo(lado_a,lado_b,lado_c,angulo_a,angulo_b,angulo_c):

    if (lado_a ** 2 + lado_b ** 2 == lado_c ** 2 or lado_b ** 2 + lado_c ** 2 == lado_a ** 2 or lado_a ** 2 + lado_c ** 2 == lado_b ** 2) and (angulo_a == 90 or angulo_b == 90 or angulo_c == 90):
          
        print('--------------------------------------')
        print('O triângulo é retângulo.')
        print('--------------------------------------')

        classificar_triangulo_pelos_lados(lado_a,lado_b,lado_c)

        return True

    else:

        return False

def verificar_se_triangulo_e_obtusangulo(lado_a,lado_b,lado_c,angulo_a,angulo_b,angulo_c):

    if (lado_a ** 2 + lado_b ** 2 > lado_c ** 2 or lado_c ** 2 + lado_b ** 2 > lado_a ** 2 or lado_a ** 2 + lado_c ** 2 > lado_b ** 2) and (angulo_a > 90 or angulo_b > 90 or angulo_c > 90):

        print('--------------------------------------')
        print('O triângulo é obtusângulo.')
        print('--------------------------------------')

        classificar_triangulo_pelos_lados(lado_a,lado_b,lado_c)

        return True

    else:

        return False

def verificar_se_triangulo_e_acutangulo(lado_a,lado_b,lado_c,angulo_a,angulo_b,angulo_c):

    if (lado_a**2 + lado_b**2 < lado_c**2 or lado_a**2 + lado_c**2 < lado_b**2 or lado_c**2 + lado_b**2 < lado_a**2) and (angulo_a < 90 or angulo_b < 90 or angulo_c < 90):

        print('--------------------------------------')
        print('O triângulo é acutângulo.')
        print('--------------------------------------')

        classificar_triangulo_pelos_lados(lado_a,lado_b,lado_c)

        return True

    else:

        return False

def interface_terminal():

    print('Digite os coeficientes da função:')
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    return a,b,c

def simplificar_raiz(raiz):

    if isinstance(raiz ** 0.5,int):

        raiz = raiz ** 0.5

        return round(raiz)
    
    else:

        return raiz

def calcular_delta(a,b,c):

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

# Versão simplificada em que se mostra somente o resultado em decimais

def segundo_grau(a, b, c):

    delta = b**2 - 4 * a * c

    # Delta maior que 0

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)

        x1Convertido = Decimal(x1)
        x2Convertido = Decimal(x2)

        if x1 == x1Convertido:

            print('Há duas raízes diferentes:')
            print('x_1')
            print(x1Convertido)
            print('x_2')
            print(x2Convertido)

        else:

            print('Há duas raízes diferentes:')
            print('x_1')
            print(x1)
            print('x_2')
            print(x2)

    # Delta menor que 0

    elif delta < 0:

        deltaNegativo = -delta

        x1 = (-b) / (2 * a)
        x1i = (- math.sqrt(deltaNegativo)) / (2 * a)
        x2 = (-b) / (2 * a)
        x2i = (+ math.sqrt(deltaNegativo)) / (2 * a)

        # Se x1 for igual ao aproximado apresenta-se o aproximado, senão apresenta-se o próprio x1

        print('Há duas raízes complexas:')
        print('x_1')
        print(' Parte real:', x1)
        print(' Parte imaginária:', x1i)
        print('x_2')
        print(' Parte real:', x2)
        print(' Parte imaginária:', x2i)

    # Delta igual a 0

    else:

        x = (-b) / (2 * a)
        xConvertido = Decimal(x)

        if x == xConvertido:
            print('Há duas raízes iguais ou somente uma raiz:')
            print('x')
            print(xConvertido)

        else:
            print('Há duas raízes iguais ou somente uma raiz:')
            print('x')
            print(x)

    print('----------------------')

# Versão melhorada
# Aparece a resposta como se fosse feito à mão

def segundo_grau_melhorada(a, b, c):

    if calcular_delta(a,b,c) == 0:

        print('Há duas raízes iguais reais ou uma raiz real:')
        print('x_1:')
        print(-1 * b)
        print('----')
        print(' ', 2 * a, ' ')
        print('x_2:')
        print(-1 * b)
        print('----')
        print(' ', 2 * a, ' ')

    elif calcular_delta(a,b,c) > 0:

        if verificar_se_e_inteiro(simplificar_raiz(calcular_delta(a,b,c))) == True:

            print('Há duas raízes diferentes e reais:')
            print('x_1:')
            print(-1 * b, ' - ', calcular_delta(a,b,c) ** 0.5)
            print('--------------------------')
            print('         ', 2 * a, '        ')
            print('x_2:')
            print(-1 * b, ' + ', calcular_delta(a,b,c) ** 0.5)
            print('--------------------------')
            print('         ', 2 * a, '        ')       

        else:

            print('Há duas raízes diferentes e reais:')
            print('x_1:')
            print(-1 * b, ' - sqrt(', calcular_delta(a,b,c), ')')
            print('--------------------------')
            print('         ', 2 * a, '        ')
            print('x_2:')
            print(-1 * b, ' + sqrt(', calcular_delta(a,b,c), ')')
            print('--------------------------')
            print('         ', 2 * a, '        ')

    else:

        print('Há duas raízes complexas conjugadas:')
        print('x_1:')
        print(-1 * b, ' - sqrt(', abs(calcular_delta(a,b,c)), ') i')
        print('--------------------------')
        print('         ', 2 * a, '        ')
        print('x_2:')
        print(-1 * b, ' + sqrt(', abs(calcular_delta(a,b,c)), ') i')
        print('--------------------------')
        print('         ', 2 * a, '        ')

    print('----------------------')


def triangulo(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c):

  if verificar_se_triangulo_existe(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c):

    if verificar_se_triangulo_e_retangulo(lado_a,lado_b,lado_c,angulo_a,angulo_b,angulo_c):

        return

    elif verificar_se_triangulo_e_obtusangulo(lado_a,lado_b,lado_c,angulo_a,angulo_b,angulo_c):

        return

    elif verificar_se_triangulo_e_acutangulo(lado_a,lado_b,lado_c,angulo_a,angulo_b,angulo_c):

        return


def triangulo_sem_angulo(a, b, c):

    if math.fabs(b - c) < a < b + c and math.fabs(a - c) < b < a + c and math.fabs(a - b) < c < b + a:

        print('--------------------------------------')
        print('O triângulo existe')
        print('--------------------------------------')

        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:

            print('--------------------------------------')
            print('O triângulo é retângulo.')
            print('--------------------------------------')

            if a == b or b == c or a == c:
                print('--------------------------------------')
                print('O triângulo é isóceles.')
                print('--------------------------------------')

        elif a**2 + b**2 > c**2 or c**2 + b**2 > a**2 or a**2 + c**2 > b**2:

            print('--------------------------------------')
            print('O triângulo é obtusângulo.')
            print('--------------------------------------')

        elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or c**2 + b**2 < a**2:

            print('--------------------------------------')
            print('O triângulo é acutângulo.')
            print('--------------------------------------')

        else:

            print('--------------------------------------')
            print('O triângulo não é retângulo.')
            print('--------------------------------------')

    else:

        print('--------------------------------------')
        print('Estas medidas não são de um triângulo.')
        print('--------------------------------------')
