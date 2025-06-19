#faça um programa que faça um aumento de salário, solicite o salário e a porcentagem de aumento e mostre o salário novo
salario = float(input("Digite o valor do salário: "))
percent = int(input("Digite a porcentagem de aumento que você quer receber: "))
salario_aumento = salario * (percent/100)
novo_salario = salario + salario_aumento
print(f"Um trabalhador que recebe R$:{salario} com um aumento de {percent}% passará a receber R$:{novo_salario}")