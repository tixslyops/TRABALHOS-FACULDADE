# 1) Menu de operações básicas (calculadora)
# Crie um menu com opções:
# 1) Somar
# 2) Subtrair
# 3) Multiplicar
# 4) Dividir
# 0) Sair
#Requisitos:
#- Use `while` para repetir o menu.
#- Use `match/case` para tratar a opção.
#- Use `if/else` para validar divisão por zero.
#- Mostre o resultado em cada operação.
 
import math
import random

print("CALCULADORA BÁSICA")

while True:
    
    operacao = ["1) Somar", "2) Subtrair", "3) Multiplicar", "4) Dividir", "0) Sair"]
    escolha = int(input("Selecione uma operação: "))

    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))

    if operacao in ["1) Somar", "2) Subtrair", "3) Multiplicar", "4) Dividir", "0) Sair"]:
        print(operacao)

    match escolha:
        case "1":
         if operacao == "1":
            print("Resultado: ", numero1 + numero2)

        case "2":
          if operacao == "2":
            print("Resultado: ", numero1 - numero2)

        case "3": 
          if operacao == "3":
            print("Resultado: ", numero1 * numero2)
        
        case "4":
          if operacao == "4":
            print("Resultado: ", numero1 / numero2)

          if numero2 >= 0:
            print("Resultado: ", numero1 / numero2)

          else:
            print("Divisão inválida!")

        case "0":
         if operacao == "0":
           print("Você saiu da calculadora.")
           break
