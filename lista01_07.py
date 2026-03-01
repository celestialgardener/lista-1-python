#receba os valores do comprimento largura e altura de um paralelepipedo e calcule seu volume
a: int = 0
l: int = 0
c: int = 0
volume: int = 0
a = int(input('entre a altura'))
l = int(input('entre a largura'))
c = int(input('entre comprimento'))
volume = (a*l*c)
print('seu volume é',volume)