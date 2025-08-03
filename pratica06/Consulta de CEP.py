import requests

cep = input("Digite o CEP (somente números, sem traço): ")

# Validação simples de CEP
if not cep.isdigit() or len(cep) != 8:
    print("CEP inválido. Digite exatamente 8 números.")
else:
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" in dados:
                print("CEP não encontrado.")
            else:
                print(f"Logradouro: {dados.get('logradouro', '-')}")
                print(f"Bairro: {dados.get('bairro', '-')}")
                print(f"Cidade: {dados.get('localidade', '-')}")
                print(f"Estado: {dados.get('uf', '-')}")
                print(f"CEP: {dados.get('cep', '-')}")
        else:
            print("Erro ao acessar a API. Tente novamente mais tarde.")
    except requests.exceptions.RequestException:
        print("Erro de conexão. Verifique sua internet ou tente novamente.")
