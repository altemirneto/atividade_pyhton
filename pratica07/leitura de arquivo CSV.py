import csv

nome_arquivo = input("Digite o nome do arquivo CSV a ser lido (ex: pessoas.csv): ")

try:
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            print(linha)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
