def par(face):
    if face%2 ==0:
        return "Jogador avança"
    else:
        return "Jogador recua"


face = int(input("Digite a face que caiu: "))
print(par(face))