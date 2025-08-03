print("=== Calculadora Simples ===")

try:
    #Solicita os dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    #Solicita a operação desejada
    operacao = input("Digite a operação (+, -, *, /): ")

    #Executa a operação escolhida
    if operacao == "+":
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")

    elif operacao == "-":
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")

    elif operacao == "*":
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")

    elif operacao == "/":
        if num2 == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")

    else:
        print("Erro: operação inválida. Use +, -, * ou /.")

except ValueError:
    print("Erro: você deve digitar números válidos.")

finally:
    print("Fim da operação.")
