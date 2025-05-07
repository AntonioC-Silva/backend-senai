def desc(valor):
    calcular = valor*0.10
    final = valor-calcular
    return final

valor = float(input("Escreva o valor do produto: "))
print(f"O valor final já com o desconto é {desc(valor)}")