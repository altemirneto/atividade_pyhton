#Solicita a idade do user
idade = int(input("Digite sua idade: "))

#Verifica e classifica a idade
if idade >= 0 and idade <= 12:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente.")
elif idade >= 18 and idade <= 59:
    print("Você é um adulto.")
elif idade >= 60:
    print("Você é um idoso.")
else:
    print("Idade inválida. Por favor, digite um número positivo.")
