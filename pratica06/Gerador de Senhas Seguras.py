import random
import string

try:
    tamanho = int(input("Digite o numero de caracteres da senha desejada: "))

    if tamanho < 4:
        print("Para sua segurança, a senha deve ter pelo menos 4 caracteres para conter todos os tipos exigidos.")
    else:
        letras_maiusculas = string.ascii_uppercase
        letras_minusculas = string.ascii_lowercase
        numeros = string.digits
        simbolos = "!@#$%&*"

        #Garante pelo menos um de cada tipo
        senha = [
            random.choice(letras_maiusculas),
            random.choice(letras_minusculas),
            random.choice(numeros),
            random.choice(simbolos)
        ]

        #Completa o restante da senha
        todos = letras_maiusculas + letras_minusculas + numeros + simbolos
        senha += [random.choice(todos) for _ in range(tamanho - 4)]

        #Embaralha os caracteres da senha
        random.shuffle(senha)
        senha_gerada = ''.join(senha)
        print(f"Senha gerada: {senha_gerada}")
except ValueError:
    print("Entrada inválida. Digite um número inteiro para o tamanho da senha.")
