def covert(celsius):
    f = (celsius * 1.8) + 32
    return f



celsius = float(input("Escreva os graus celsius: "))
print(f"A temperatura em Fahrenheit é {covert(celsius)}")