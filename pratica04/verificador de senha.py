while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == "sair":
        print("Programa encerrado.")
        break

    if len(senha) < 8:
        print("Senha fraca: deve conter pelo menos 8 caracteres.")
        continue

    if not any(char.isdigit() for char in senha):
        print("Senha fraca: deve conter pelo menos um número.")
        continue

    print("Senha forte!")
    break
