# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input('Digite o dia: '))
horas = int(input('Digite a hora: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))


total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print(f'Convertido em segundos é igual {total_em_segundos}')