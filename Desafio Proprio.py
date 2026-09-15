#login aplicativo

#Colocar cadastro e senha
#confirmar senah e cadastro
#se os dois estievrem certos validar a entrada
#se a senha estiver errada mas o cadastro certo, informar
#se for o contrario informar tbm
#caso os dois estiverem errados, negar acesso

cadastro = input("Coloque seu cadastro: ")
senha = int(input("Coloque sua senha: "))



while True:
    tentativa_cadastro = input("Confirme o seu cadastro: ")
    tentativa_senha = int(input("Confirme o seu senha: "))

    if cadastro == tentativa_cadastro and senha == tentativa_senha:
        print("Acesso Liberado")
        break
    elif cadastro == tentativa_cadastro and senha != tentativa_senha:
        print("Cadastro Correto, Senha Errada, Tente Novamente")

    elif senha == tentativa_senha and cadastro != tentativa_cadastro:
        print("Senha Correta, Cadasto Errado, Tente Novamente")
        
    else:
        print("Cadastro e Senha Errada, Tente Novamente")
        
