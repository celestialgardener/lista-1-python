#receba o ano de nascimento e o ano atual calcule e mostre a sua idade e quantos anos tera daqui a 17 anos
an: int=0
aa: int=0
ad: int=0
id: int=0

an = int(input('entre o ano de nascimento'))
aa = int(input('entre o ano atual'))
id = (aa-an)
ad = (id +17)
print('voce atualemnte tem ',id,' e daqui a 17 anos tera',ad)