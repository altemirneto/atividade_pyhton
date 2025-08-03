import csv

# Dados fictícios de pessoas (sem acentuação nos nomes)
dados = [
    ["Maria", 25, "Sao Paulo"],
    ["Joao", 32, "Rio de Janeiro"],
    ["Ana", 28, "Belo Horizonte"],
    ["Carlos", 41, "Curitiba"],
    ["Fernanda", 22, "Salvador"],
    ["Pedro", 35, "Fortaleza"],
    ["Lucas", 29, "Brasilia"],
    ["Julia", 27, "Recife"]
]

nome_arquivo = input("Digite o nome do arquivo CSV para salvar os dados (ex: pessoas.csv): ")

try:
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        # Cabeçalhos
        escritor.writerow(["nome", "idade", "cidade"])
        # Dados das pessoas
        escritor.writerows(dados)
    print(f"Dados gravados com sucesso em '{nome_arquivo}'!")
except Exception as e:
    print(f"Erro ao gravar o arquivo: {e}")
