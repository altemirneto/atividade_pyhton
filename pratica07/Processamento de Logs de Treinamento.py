import pandas as pd

arquivo = input("Digite o nome do arquivo CSV (ex: logs_treinamento.csv): ")

try:
    df = pd.read_csv(arquivo)

    if 'tempo_execucao' not in df.columns:
        print("Erro: A coluna 'tempo_execucao' não foi encontrada no arquivo.")
    else:
        media = df['tempo_execucao'].mean()
        desvio = df['tempo_execucao'].std()
        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Desvio padrão do tempo de execução: {desvio:.2f}")

except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except pd.errors.EmptyDataError:
    print("Erro: O arquivo está vazio ou possui formatação incorreta.")
except pd.errors.ParserError:
    print("Erro: Não foi possível ler o arquivo devido à formatação incorreta.")
except Exception as e:
    print(f"Erro inesperado: {e}")
