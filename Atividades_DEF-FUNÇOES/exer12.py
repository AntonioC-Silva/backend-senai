def fat(num):
    if num<0:
        return "Inválido"
    else:
        resultado = 1
        for i in range(1, num + 1):
            resultado *= i
        return resultado

num = int(input("Escreva um numero: "))
print(f"O fatorial de {num} é {fat(num)}")