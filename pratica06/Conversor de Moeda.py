import requests
from datetime import datetime

moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").upper()

url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

try:
    resposta = requests.get(url, timeout=5)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave in dados:
            info = dados[chave]
            cotacao = float(info['bid'])
            maximo = float(info['high'])
            minimo = float(info['low'])
            data_hora = datetime.fromtimestamp(int(info['timestamp']))
            
            print(f"\nCotação {moeda}/BRL")
            print(f"Cotação atual: R$ {cotacao:.4f}")
            print(f"Valor máximo: R$ {maximo:.4f}")
            print(f"Valor mínimo: R$ {minimo:.4f}")
            print(f"Última atualização: {data_hora.strftime('%d/%m/%Y %H:%M:%S')}")
        else:
            print("Código da moeda não encontrado ou inválido.")
    else:
        print("Erro ao acessar a API. Tente novamente mais tarde.")
except requests.exceptions.RequestException:
    print("Erro de conexão. Verifique sua internet ou tente novamente.")
