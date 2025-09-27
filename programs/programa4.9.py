valido = True
plano = input("Qual é o seu plano de celular? ").strip().lower()

if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.20
    preco = 50.0
elif plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15
    preco = 99.0
else:
    valido = False

if not valido:
    print("Erro, não conheço este plano")
else:
    try:
        minutos_consumidos = int(input("Quantos minutos consumiu? ").strip())
    except ValueError:
        print("Entrada inválida: digite um número inteiro para os minutos.")
    else:
        print("Você vai pagar:")
        print(f"Preço do plano R${preco:10.2f}")
        suplemento = 0.0
        if minutos_consumidos > minutos_no_plano:
            suplemento = extra * (minutos_consumidos - minutos_no_plano)
        print(f"Suplemento R${suplemento:10.2f}")
        print(f"Total R${preco + suplemento:10.2f}")
