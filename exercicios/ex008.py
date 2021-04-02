#Exercício Python 008: Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

print(5*'=','VAMOS CONVERTER AS UNIDADES MÉTRICAS',5*'=')

metro = float(input('Qual valor em metros? '))

dc = metro * 10
cm = metro * 100
mm = metro * 1000

print(f'{metro:.2f} metros representa {cm:.2f} centimetros')
print(f'{metro:.2f} metros representa {mm:.2f} milimetros')
print(f'{metro:.2f} metros representa  {dc:.2f} decimetros')