def dificul(classificacao):
    if classificacao <=5:
        return "Pequeno"
    elif classificacao<=10:
        return "Médio"
    else:
        return "Grande"


classificacao = int(input("Escreva o nivel de dificuldade do desafio: "))
print(f"O nivel de dificuldade é {dificul(classificacao)}")