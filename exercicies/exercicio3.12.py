#Calcula tempo de viagem
#informações necessárias -> velocidade média, distância
print("CALCULAR O TEMPO DA VIAGEM")
velocidade_media = int(input("Qual a velocidade média que você vai andar? (km/h):"))
distancia = int(input("Qual a distância a ser percorrida? (km):"))
tempo = float(distancia)/float(velocidade_media)
if tempo < 1:
    tempo *= 60
    print(f"Levando em consideração as informações passadas, o tempo médio dessa viagem será de {tempo:.2f} minutos.")
else:    
    print(f"Levando em consideração as informações passadas, o tempo médio dessa viagem será de {tempo:.2f}hr.")