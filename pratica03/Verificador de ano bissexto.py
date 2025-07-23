#Solicita o ano ao usuário
ano = int(input("Digite um ano: "))

#Verifica se o ano é bissexto usando if, elif e else
if ano % 400 == 0:
    print(f"{ano} é um ano bissexto.")
elif ano % 100 == 0:
    print(f"{ano} não é um ano bissexto.")
elif ano % 4 == 0:
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")