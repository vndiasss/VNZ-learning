# nesse codigo o usuario deve acertar qual é o numero secreto
#é preciso sempre manter o loop até que o usuario acerte o numero
#dicas seram dadas, dizendo se é um numero maior ou menor
#quando acertar falara em quantas tentativas ele conseguiu acertar o numero

import random

numero_secreto = random.randint(1, 50)
tentativas = 0

print("adivinhe o número entre 1 e 100")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    
    if palpite == numero_secreto:
        print(f'parabens você acertou em {tentativas} tentativas.')
        
    elif palpite < numero_secreto:
        print("o numero secreto é maior")
    else:
        print("O numero secreto é menor")
