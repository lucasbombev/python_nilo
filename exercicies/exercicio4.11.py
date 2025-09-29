#Escreva um programa para aprovar um empréstimo bancário para compra de uma casa. O programa dever perguntar o valor da casa a comprar, o salário ou a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule a valor da prestação como sendo  o valor da casa a comprar dividido pelo número de meses a pagar.
print(20*"=", "EMPRÉSTIMO PARA COMPRAR CASA",20*"=")
valor_casa = float(input("Digite o valor da casa R$: "))
salario = float(input("Digite o seu salário R$: "))
anos_pagar = int(input("Digite a quantidade de anos a pagar: "))
meses_pagar = anos_pagar * 12
prestacao = valor_casa / meses_pagar
teto_prestacao = salario * 0.30

if prestacao > teto_prestacao:
    print("A casa é muito cara para comprar com seu salário de liso.")
    print(f"A prestação mensal ultrapassa 30% do seu salário e ficaria R${prestacao:.2f}")
else:
    print("Você consegue comprar essa casa! Parabéns!")
    print(f"A prestação mensal ficará R${prestacao:.2f}")
