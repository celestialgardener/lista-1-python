#receba os coeficientes a b e c de uma equação de 2 grau calcule e mostre as raizes reais 
a: int = 0
b: int = 0
c:int = 0
delta:int = 0
raiz1:int = 0
raiz2:int = 0

a = int(input('entre o valor a'))
b = int(input('entre o valor b'))
c = int(input('entre o valor c'))
delta= (b**2) -(4*a*c)
#print(delta)
raiz1 = (-b + (delta**0.5))/2*a
raiz2 = (-b - (delta**0.5))/2*a
#if(delta < 0):
 #   print('delta é menor que zero, nao existem raizes reais, tente outros numeros')
  #  exit()
#else:
print('raiz 1 ',raiz1,'raiz 2',raiz2)


