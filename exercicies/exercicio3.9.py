#Escreva um programa que leia o total de dias, horas, minutos e segundos o usuário e calcule o total em segundos.
total = 0 
dias = int(input("Digite quantos dias: "))
total+= dias*86400
horas = int(input("Digite quantas horas: "))
total += horas*3600
minutos =  int(input("Digite quantos minutos: "))
total += minutos*60
segundos = int(input("Digite quantos segundos: "))
total += segundos
print(f"O total de tempo percorrido em segundos foi: {total}")