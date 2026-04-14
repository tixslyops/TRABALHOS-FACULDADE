import random

vida_jogador = 100
vida_inimigo = 100

print("RPG DE BATALHA")

acoes = ["1 - Atacar", "2 - Defender", "3 - Fugir"]
while True:
    print("\nSua vida:", vida_jogador)
    print("\nVida do inimigo:", vida_inimigo)
    print("\nEscolha sua ação:")

    for acao in acoes:
        print(acao)

    escolha = input("Selecione a ação: ")

    match escolha:
     case "1":
        dano_jogador = random.randint(10, 25)
        dano_inimigo = random.randint(7, 23)

        print(f"\nVocê atacou e causou {dano_jogador} de dano!")
        vida_inimigo -= dano_jogador

        if vida_inimigo > 0:
            print(f"O inimigo revidou com {dano_inimigo} de dano!")
            vida_jogador -= dano_inimigo
        else:
            print("Você derrotou o inimigo!")
    
     case "2":
        defesa = random.randint(1, 10)
        dano_inimigo = random.randint(5, 20)
        
        print(f"\nVocê se defendeu e reduziu {defesa} de dano!")

        dano_final = dano_inimigo - defesa

        if dano_final < 0:
            dano_final = 0

        vida_jogador -= dano_final
        print(f"Você recebeu {dano_final} de dano!")

     case "3":
        chance = random.randint(1, 10)
        if chance > 5:
            print("\nVocê fugiu com sucesso!")
            break
        else:
            print("\nFalha ao fugir!")
            dano_inimigo = random.randint(5, 15)
            vida_jogador -= dano_inimigo
            print(f"O inimigo te atacou e causou {dano_inimigo} de dano!")

     case _:
         print("Opção inválida!")

    if vida_jogador <= 0:
      print("\nVocê foi derrotado!")
      break
    elif vida_inimigo <= 0:
      print("\nParabéns! Você venceu a batalha!")
      break