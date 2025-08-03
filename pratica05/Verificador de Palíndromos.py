def remover_acentos(texto):
    acentos = {
        'á':'a', 'à':'a', 'ã':'a', 'â':'a',
        'é':'e', 'ê':'e',
        'í':'i',
        'ó':'o', 'ô':'o', 'õ':'o',
        'ú':'u',
        'ç':'c'
    }
    texto_sem_acentos = ""
    for c in texto.lower():
        if c in acentos:
            texto_sem_acentos += acentos[c]
        else:
            texto_sem_acentos += c
    return texto_sem_acentos

def limpar_texto(texto):
    texto = remover_acentos(texto)
    texto_limpo = ""
    for c in texto:
        if c.isalnum():
            texto_limpo += c
    return texto_limpo

frase = input("Digite uma palavra ou frase: ")
texto_limpo = limpar_texto(frase)

if texto_limpo == texto_limpo[::-1]:
    print("Sim, a palavra é um palíndromo")
else:
    print("Não, a palavra não é um palindromo")
