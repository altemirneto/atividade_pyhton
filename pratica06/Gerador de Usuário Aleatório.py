import requests

try:
    resposta = requests.get("https://randomuser.me/api/", timeout=5)
    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    else:
        print("Erro: Não foi possível obter dados da API. Código de status:", resposta.status_code)
except requests.exceptions.RequestException:
    print("Erro de conexão ou falha ao acessar a API.")
