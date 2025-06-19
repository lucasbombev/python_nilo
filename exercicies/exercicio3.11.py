# faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. exiba o valor de desconto e o preço a pagar.
mercadoria = float(input("Digite o preço da mercadoria: "))
desconto = int(input("Digite o percentual de desconto. ex:15% "))
valor_descontado = mercadoria * (desconto/100)
novo_valor = mercadoria - valor_descontado
print(f"O desconto que você ganhou foi R${valor_descontado}")
print(f"O preço final do produto foi R${novo_valor}")
