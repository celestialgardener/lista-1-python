#receba os valores de 2 catetos de um triangulo e calcule a hipotenusa
a: int= 0
b: int =0
c:int = 0

a = int(input('entre o valor do cateto a'))
b = int(input('entre o valor do cateto b'))
c= (a*a) + (b*b)
c=c**0.5
print('sua hipotenusa é igual a ',c)