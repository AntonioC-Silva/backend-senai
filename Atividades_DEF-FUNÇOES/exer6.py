def faixetaria(idade):
    if idade <=0:
        return "Invalido"
    elif idade <18:
        return "Não pode assistir!"
    else:
        return "Pode assistir"

idade  = int(input("Digite sua idade: "))
print(faixetaria(idade))