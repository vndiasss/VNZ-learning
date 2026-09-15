#Esse codigo deve verificar a idade do usuario e só liberar ele se sua idade for maior que 18

idade = int(input("Qual é a sua idade? "))

if idade >= 18:
    print("acesso liberado")
elif idade >= 13:
    print("acesso liberado somente com permissão dos pais")
else:
    print("acesso negado")