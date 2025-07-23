#Solicita o peso do usuario
peso = float(input("Digite seu peso (em kg): "))

#Solicita a altura do usuário (em metros)
altura = float(input("Digite sua altura (em metros): "))

#Calcula o IMC
imc = peso / (altura ** 2)

#Exibe o IMC com duas casas decimais
print(f"\nSeu IMC é: {imc:.2f}")

#Classifica o IMC com base nos critérios dados
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

#Mostra a classificação final
print(f"Classificação: {classificacao}")
