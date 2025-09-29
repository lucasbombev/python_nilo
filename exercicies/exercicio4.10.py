#Escreva um programa que leia dois números e pergunte qual operação o usuário deseja realizar. soma, subtração, multiplicação ou divisão.
# Exiba o resultado da operação solicitada.

valido = True
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operate = str(input("Digite a operação a ser realizada:\n Soma ( + )\n Subtração ( - )\n Multiplicação ( * )\n Divisão ( / )\n")).strip()

if operate == "+":
    print(f"A soma entre {numero1} e {numero2} é : {numero1+numero2}")
elif operate == "-":
    print(f"A subtração entre {numero1} e {numero2} é : {numero1-numero2}")
elif operate == "*":
    print(f"A multiplicação entre {numero1} e {numero2} é : {numero1*numero2}")
elif operate == "/":
    print(f"A divisão entre {numero1} e {numero2} é : {numero1/numero2}")
else:
    valido = False

if not valido:
    print("Erro! o operador digitado é inválido.")