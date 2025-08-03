import json

# Dicionário com dados de uma pessoa (sem acentuação)
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "Curitiba"
}

nome_arquivo = input("Digite o nome do arquivo JSON (ex: pessoa.json): ")

# Escrita do arquivo JSON
try:
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo_json:
        json.dump(pessoa, arquivo_json, ensure_ascii=False, indent=4)
    print(f"Dados salvos com sucesso em '{nome_arquivo}'.")
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")

# Leitura do arquivo JSON
try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo_json:
        dados_carregados = json.load(arquivo_json)
    print("Conteudo lido do arquivo JSON:")
    print(dados_carregados)
except FileNotFoundError:
    print("Erro: Arquivo JSON não encontrado.")
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
