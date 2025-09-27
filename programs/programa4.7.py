minutos = int(input("Quantos minutos você utilizou esse mês: "))
if minutos < 200:
    preco = 0.20
elif minutos < 400:
    preco = 0.18
else:
    preco = 0.15
print(f"Você vai pagar esse mês {minutos*preco:6.2f} ")
