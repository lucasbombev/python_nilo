distancia = int(input("Qual a distância que você quer percorrer? (km): "))
passagem_curta = 0.50 * distancia
passagem_longa = 0.45 * distancia
if distancia >= 200:
    print(f"como sua viagem percorre {distancia}km. é considerada uma viagem curta, e a passagem custará R${passagem_curta}")
else:
    print(f"como sua viagem percorre {distancia}km. é considerada uma viagem longa, e a passagem custará R${passagem_longa}")