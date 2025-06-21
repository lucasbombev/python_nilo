# Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado pelo usuário, assim como quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
km_percorridos = int(input("Quantos km você percorreu? "))
dias_alugados = int(input("Quantos dias o carro foi alugado? "))
pagamento = (60 * dias_alugados) + (km_percorridos * 0.15)
print(f"O preço a pagar por {km_percorridos}KM durante {dias_alugados} dias é de R${pagamento:.2f}.")