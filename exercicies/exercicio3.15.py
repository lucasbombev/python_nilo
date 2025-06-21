# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro e calcule quantos dias de vida um fumante perderá, mostre a quantidade de dias.

cigarros_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumante = int(input("Você é fumante há quantos anos? "))
print("Considere que a cada cigarro que você fuma, você chupa a piroca de um demônio.")
total_cigarros = cigarros_dia * 365 * anos_fumante
print(f"Você já chupou {total_cigarros} pirocas de demônio.")
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / (60 * 24)

print(f"Você perderá aproximadamente {dias_perdidos:.2f} dias de vida devido ao fumo.")