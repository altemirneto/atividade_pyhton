try:
    preco_original = float(input("Digite o preço original do produto: ").replace(',', '.'))
    percentual_desconto = float(input("Digite o percentual de desconto: "))

    preco_final = preco_original * (1 - percentual_desconto / 100)
    print(f"Preço final do produto com desconto: R$ {preco_final:.2f}")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números válidos.")
