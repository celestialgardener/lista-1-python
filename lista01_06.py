#6 receba os valores em x e y efetue a troca de valores e mostre seus conteudos
x: int =0
y: int =0
z: int =0
x = int(input('entre o valor x'))
y = int(input('entre o valor y'))
z = x
x = x-x
x= x+y
y= y-y
y= y+z
print('x agora é',x)
print('y agora é',y)
