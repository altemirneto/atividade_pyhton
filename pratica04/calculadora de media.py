notas = []
while True:
    entrada = input("Digite uma nota entre 0 e 10 ou 'fim' para encerrar: ")
    if entrada.lower() == "fim":
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Erro: Nota fora do intervalo permitido (0 a 10).")
    except ValueError:
        print("Erro: Entrada inválida. Digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
    print(f"Total de notas válidas: {len(notas)}")
else:
    print("Nenhuma nota válida foi registrada.")
