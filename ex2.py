senha_correta = 5432
tentativas = 3

while tentativas > 0:
   senha = int(input("Digite a senha: "))
   if senha == senha_correta:
    print("Acesso liberado")
    break
   
   else: 
    tentativas -= 1
    print("Senha incorreta!")
   
   if tentativas == 0:
    print("Acesso bloqueado!")
