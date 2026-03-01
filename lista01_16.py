sb: int=0
sl:int=0
d:int=0
ht:int=0
vh:int=0
pd:int=0

ht =int(input('quantas horas voce trabalhou?'))
vh =int(input('qqal o valor por hora?'))
d =int(input('quantos descendentes voce tem?'))
pd =int(input('qual o percentual de desconto?'))
sl = ((ht*vh)-((ht*vh)*(pd/100)))
sb = (sl +(d*100))
print('seu salario apos todos os reajustes é',sb)