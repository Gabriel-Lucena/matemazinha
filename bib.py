import math
from decimal import Decimal

def verificarsoma(a,b):
  c = a + b

  if c < 0:
    print('Deu Ruim')
  elif c > 0:
    print('Deu bom')
  else:
    print('Deu meio')
  
  print('--------------')

def verificaridade(idade):

  if idade < 12:
    print('criança')
  elif idade < 18:
    print('adolescente')
  elif idade < 60:
    print('adulto')
  else:
    print('idoso')

  print('----------------------')

#Versão simplificada em que se mostra somente o resultado em decimais

def segundograu(a,b,c):

  delta = b**2 - 4 * a * c

  #Delta maior que 0

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

  #Delta menor que 0

  elif delta < 0:

    deltaNegativo = -delta

    x1 = (-b) / (2 * a)
    x1i = ( - math.sqrt(deltaNegativo)) / (2 * a)
    x2 = (-b) / (2 * a)
    x2i = ( + math.sqrt(deltaNegativo)) / (2 * a)

    #Se x1 for igual ao aproximado apresenta-se o aproximado, senão apresenta-se o próprio x1

    print('Há duas raízes complexas:')
    print('x_1')
    print(' Parte real:',x1)
    print(' Parte imaginária:',x1i)
    print('x_2')
    print(' Parte real:',x2)
    print(' Parte imaginária:',x2i)

  #Delta igual a 0

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

#Versão melhorada
#Aparece a resposta como se fosse feito à mão

def segundograumelhorada(a,b,c):

  delta = b**2 - 4 * a * c

  if b == 0:
    print('+- sqrt(', delta, ')', ' / ' ,'(' , 2 * a , ')')
  else:
    print(-b, '+- sqrt(', delta, ')', ' / ' ,'(' , 2 * a , ')')

  if c == 0:
    print(-b, '+- ', b, ' / ' ,' (', 2 * a , ') ' )

  print('----------------------')

def triangulo(a,b,c,angulo1,angulo2,angulo3):

  if math.fabs(b - c) < a < b + c and math.fabs(a - c) < b < a + c and math.fabs(a - b) < c < b + a and angulo1 + angulo2 + angulo3 == 180:
    
    print('--------------------------------------')
    print('O triângulo existe')
    print('--------------------------------------')

    if a**2 + b**2 == c**2 and angulo1 == 90 or angulo2 == 90 or angulo3 == 90:

      print('--------------------------------------')
      print('O triângulo é retângulo.')
      print('--------------------------------------')

    elif a**2 + b**2 > c**2 and angulo1 > 90 or angulo2 > 90 or angulo3 > 90:

      print('--------------------------------------')
      print('O triângulo é obtusângulo.')
      print('--------------------------------------')

    elif a**2 + b**2 < c**2 and angulo1 < 90 or angulo2 < 90 or angulo3 < 90:

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


def triangulosemangulo(a,b,c):

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
