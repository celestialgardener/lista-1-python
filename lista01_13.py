pessoas:int =0 
comida: int=0
dias: int=0
pessoas =int(input('quantas pessoas vao comer?'))
comida =int(input('quantos kilos de comida voce vai ter?'))
dias = (comida*1000)/(pessoas*50)
print('sua comida vai durar',dias,'dias') 
 