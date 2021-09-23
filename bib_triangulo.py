import math
from decimal import Decimal


def classificar_triangulo_pelos_lados(lado_a, lado_b, lado_c):

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


def verificar_se_triangulo_existe_com_angulos(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c):

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


def verificar_se_triangulo_existe_simples(lado_a, lado_b, lado_c):

    if math.fabs(lado_b - lado_c) < lado_a < lado_b + lado_c and math.fabs(lado_a - lado_c) < lado_b < lado_a + lado_c and math.fabs(lado_a - lado_b) < lado_c < lado_b + lado_a:

        print('--------------------------------------')
        print('O triângulo existe.')
        print('--------------------------------------')

        return True

    else:

        print('--------------------------------------')
        print('O triângulo não existe.')
        print('--------------------------------------')

        return False


def verificar_se_triangulo_e_retangulo_com_pitagoras(lado_a, lado_b, lado_c):

    if lado_a ** 2 + lado_b ** 2 == lado_c ** 2 or lado_b ** 2 + lado_c ** 2 == lado_a ** 2 or lado_a ** 2 + lado_c ** 2 == lado_b ** 2:

        print('--------------------------------------')
        print('O triângulo é retângulo.')
        print('--------------------------------------')

        return True

    else:

        print('--------------------------------------')
        print('O triângulo não é retângulo.')
        print('--------------------------------------')

        return False


def verificar_se_triangulo_e_retangulo(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c):

    if (lado_a ** 2 + lado_b ** 2 == lado_c ** 2 or lado_b ** 2 + lado_c ** 2 == lado_a ** 2 or lado_a ** 2 + lado_c ** 2 == lado_b ** 2) and (angulo_a == 90 or angulo_b == 90 or angulo_c == 90):

        print('--------------------------------------')
        print('O triângulo é retângulo.')
        print('--------------------------------------')

        classificar_triangulo_pelos_lados(lado_a, lado_b, lado_c)

        return True

    else:

        return False


def verificar_se_triangulo_e_obtusangulo(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c):

    if (lado_a ** 2 + lado_b ** 2 > lado_c ** 2 or lado_c ** 2 + lado_b ** 2 > lado_a ** 2 or lado_a ** 2 + lado_c ** 2 > lado_b ** 2) and (angulo_a > 90 or angulo_b > 90 or angulo_c > 90):

        print('--------------------------------------')
        print('O triângulo é obtusângulo.')
        print('--------------------------------------')

        classificar_triangulo_pelos_lados(lado_a, lado_b, lado_c)

        return True

    else:

        return False


def verificar_se_triangulo_e_acutangulo(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c):

    if (lado_a**2 + lado_b**2 < lado_c**2 or lado_a**2 + lado_c**2 < lado_b**2 or lado_c**2 + lado_b**2 < lado_a**2) and (angulo_a < 90 or angulo_b < 90 or angulo_c < 90):

        print('--------------------------------------')
        print('O triângulo é acutângulo.')
        print('--------------------------------------')

        classificar_triangulo_pelos_lados(lado_a, lado_b, lado_c)

        return True

    else:

        return False


def triangulo(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c):

    if verificar_se_triangulo_existe_com_angulos(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c):

        if verificar_se_triangulo_e_retangulo(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c):

          return

        elif verificar_se_triangulo_e_obtusangulo(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c):

          return

        elif verificar_se_triangulo_e_acutangulo(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c):

          return


def triangulo_sem_angulo(lado_a, lado_b, lado_c):

    if verificar_se_triangulo_existe_simples(lado_a, lado_b, lado_c):

        if verificar_se_triangulo_e_retangulo_com_pitagoras(lado_a, lado_b, lado_c):

            classificar_triangulo_pelos_lados(lado_a, lado_b, lado_c)

        else:

            return
