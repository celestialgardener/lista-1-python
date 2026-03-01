litros:int=0
tempo:int=0
velocidade:int=0
distancia:int=0

tempo= int(input('quantas horas sua viagem durou?'))
velocidade= int(input('qual foi a velocidade media de sua viagem e km/h?'))
distancia = (tempo*velocidade)
litros = (distancia/12)
print('voce gastou',litros,'litros de gasolina em sua viagem')
