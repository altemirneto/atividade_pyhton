try:
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))

    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Desconsiderando anos bissextos

    print(f"Idade aproximada em dias: {idade_dias}")
except ValueError:
    print("Entrada inválida. Digite apenas números inteiros.")
