#aqui eu tenho que criar um codigo que verifique se a palavra é um palindromo ou n
#ou seja se ela ela é a mesma de frente pra tras

entrada = input("Qual a sua palavra? ")
padronizado = entrada.lower()

palavra_invertida = padronizado[::-1]

if padronizado == palavra_invertida:
    print("é um palindromo")
else: 
    print('não é um palindromo')





