#dados ao usuário
valor = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

#Primeiro converte a temperatura para Celsius (se não for Celsius já)
if origem == "C":
    celsius = valor
elif origem == "F":
    celsius = (valor - 32) * 5 / 9
elif origem == "K":
    celsius = valor - 273.15
else:
    print("Unidade de origem inválida!")
    exit()  #Sai do programa se a unidade for inválida

#Depois, converte de Celsius para a unidade de destino
if destino == "C":
    resultado = celsius
elif destino == "F":
    resultado = (celsius * 9 / 5) + 32
elif destino == "K":
    resultado = celsius + 273.15
else:
    print("Unidade de destino inválida!")
    exit()

#Mostra o resultado final
print(f"\n{valor}°{origem} é igual a {resultado:.2f}°{destino}")
