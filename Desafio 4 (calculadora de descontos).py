#cria uma calculadora que calcula o desconto aplicado em cima do preço original

preço_original = float(input("Digite o preço da sua compra: "))

if preço_original < 100:
    print("Não há descontos")

elif preço_original > 500:
    desconto_de_20 = preço_original * 0.20
    final = preço_original - desconto_de_20
    print(f"O valor da sua compra é de {final}, desconto de R$ {desconto_de_20}")

else:
    desconto_de_10 = preço_original * 0.10
    final2 = preço_original - desconto_de_10
    print(f"O valor da sua compra é de {final2}, desconto de R$ {desconto_de_10}")