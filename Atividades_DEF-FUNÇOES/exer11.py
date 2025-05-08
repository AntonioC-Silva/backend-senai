
def palindromos(palavras):
    palavrass = palavras.replace(" ", "")
    if palavrass.lower() == palavrass.lower()[::-1]:
        return "É palindromo!"
    else:
        return "Não é um palindromo!"


palavras = str(input("Digite uma palavra: "))
print(palindromos(palavras))