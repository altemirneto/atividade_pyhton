try:
    valor_conta = float(input("Digite o valor da conta (ex: 100.00): ").replace(",", "."))
    porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10, 15, 20): "))

    valor_gorjeta = valor_conta * (porcentagem / 100)
    print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números válidos.")
