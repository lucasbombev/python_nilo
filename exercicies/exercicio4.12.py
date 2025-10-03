# Solicita os dados
consumo = int(input("Qual a quantidade de consumo em kWh? "))
instalation = input("Qual o tipo de instalação?\nR para residências\nI para indústrias\nC para comércios\n: ").strip().upper()

# Verifica se o tipo é válido
if instalation not in ["R", "C", "I"]:
    print("Tipo de instalação inválido!")
else:
    custo = 0

    # Consumo Residencial
    if instalation == "R":
        if consumo <= 500:
            custo = 0.40 * consumo
        else:
            custo = 0.65 * consumo

    # Consumo Comercial
    elif instalation == "C":
        if consumo <= 1000:
            custo = 0.55 * consumo
        else:
            custo = 0.60 * consumo

    # Consumo Industrial
    elif instalation == "I":
        if consumo <= 5000:
            custo = 0.55 * consumo
        else:
            custo = 0.60 * consumo

    # Dicionário para traduzir os tipos
    tipos = {
        "R": "Residencial",
        "C": "Comércio",
        "I": "Indústria"
    }

    # Exibe resultado
    print(f"Tipo de consumo: {tipos[instalation]}")
    print(f"Custo: R$ {custo:.2f}")
