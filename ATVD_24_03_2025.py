'''
#ATVD1
num =int(input("Escreva um numero: "))
if num%2 == 0:
    print("O numero é par.")
else:
    print("O numero é impar.")
'''

'''
#ATVD2
num =float(input("Escreva um numero: "))
if num >10:
    print("Maior que 10")
else:
    print("Não é maior que 10")
'''

'''
#ATVD3
idade =int(input("Escreva sua idade: "))
if idade >=18:
    print("Maior de idade")
else:
    print("Menor de idade")
'''

'''
#ATVD4
idade = int(input("Escreva sua idade: "))
if idade <16:
    print("Não eleitor")
elif idade >=16 and idade <18:
    print("Voto opcional")
elif idade>=70:
    print("Voto opcional")
else:
    print("Obrigatorio")
'''

'''
#ATVD5
num =float(input("Escreva um numero: "))
if num == 0:
    print("O numero é 0")
elif num<0:
    print("Numero negativo")
else:
    print("Numero positivo")
'''

'''
#ATVD6
nota = float(input("Digite a Nota: "))
if nota <0:
    print("Nota inválida")
elif  nota <3:
    print("Nota E")
elif  nota <5:
    print("Nota D")
elif  nota < 7:
    print("Nota C")
elif  nota < 9:
    print("Nota B")
elif  nota <= 10:
    print("Nota A")
else: print("Nota inválida")
'''

'''
#ATVD7
idade = int(input("Digite sua idade: "))
if idade<13:
    print("Paga meia")
elif idade<60:
    print("Paga valor total")
else:
    print("Paga meia")
'''

'''
#ATVD8
lado1 = float(input("Escreva um lado: "))
lado2 = float(input("Escreva outro lado: "))
base = float(input("Escreva o valor da base: "))
tria = lado1+lado2
cal = tria>base
if tria>base:
    print("É um triângulo")
    if lado1 == lado2 and lado2==base:
        print("Equilatero")
    elif lado1==lado2 and lado2!=base:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não pode ser um triângulo")
'''

'''
#ATVD9
valor = float(input("Escreva o valor da compra: "))
if valor < 100:
    desc = (valor*5)/100
    print("O valor a pagar é", valor-desc)
elif valor < 501:
    desc = (valor*10)/100
    print("O valor a pagar é", valor-desc)
else:
    desc = (valor*15)/100
    print("O valor a pagar é", valor-desc)
'''

'''
#ATVD10
ano = int(input("Escreva um ano: "))
if (ano%4== 0 and ano%100 !=0) or (ano%400 == 0):
    print("O ano é bissexto")
else:
    print("Ano não Bissexto")
'''

'''
#ATVD11
peso = float(input("Escreva seu peso: "))
altura = float(input("Escreva sua altura:"))
imc = peso/(altura*altura)
print(imc)
if imc < 18.5:
    print("Baixo peso")
elif imc <25:
    print("Peso normal")
elif imc <30:
    print("Sobrepeso")
else:
    print("Obesidade")
'''

'''
#ATVD12
num1 = float(input("Escreva um numero: "))
num2 = float(input("Escreva outro numero: "))
num3 = float(input("Escreva outro numero: "))
if num1>num2 and num2>num3:
    print("Ordem descrescente")
elif num3>num2 and num2>num1:
    print("Ordem crescente")
elif num1==num2 and num2==num3:
    print("Os numeros são iguais")
else:
    print("Não estão em uma ordem")
'''

'''
#ATVD13
temp = float(input("Escreva quantidade de Graus Celsius: "))
if temp<10:
    print("Frio")
elif temp<26:
    print("Aconchegante")
elif temp<41:
    print("Quente")
else:
    print("Muito Quente")
'''

'''
#ATVD14
data = input("Digite a data no formato dd/mm/aaaa: ")
dia = data[0:2]
mes = data[3:5]
ano = data[6:10]
dat = (f"{ano}/{mes}/{dia}")
print(f"A data convertida é: {dat}")
'''

'''
#ATVD15
import re

senha = input("Digite a senha: ")
requisitos= True
if len(senha) < 8:
    print("a senha deve ter pelo menos 8 caracteres.")
    requisitos= False
if not re.search(r"[A-Z]", senha):
    print("a senha deve ter pelo menos uma letra maiúscula.")
    requisitos= False
if not re.search(r"[a-z]", senha):
    print("a senha deve ter pelo menos uma letra minúscula.")
    requisitos= False
if not re.search(r"[0-9]", senha):
    print("a senha deve ter pelo menos um número.")
    requisitos= False
if not re.search(r"[@#$%&]", senha):
    print("a senha deve ter pelo menos um caractere especial (@, #, $, %, &).")
    requisitos= False
if requisitos:
    print("Senha válida")
'''

'''
#ATVD16
num = float(input("Escreva um numero: "))
if num<0:
    print("Não é possível calcular a raiz quadrada de um número negativo.")
elif num>100:
    print("Número muito grande, reduza para um valor abaixo de 100.")
else:
    num = num**0.5
    print(f"A raiz quadrada é {num:,.2f}")
'''

'''
#ATVD17
data = input("Escreva a data no seguinte formato (dd/mm/aaaa): ")
partes = data.split("/")
dia = int(partes[0])
mes = int(partes[1])
ano = int(partes[2])

if mes < 1 or mes > 12:
    print("Mês inválido. O mês deve estar entre 1 e 12.")
else:
    if mes == 2:
        if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
            limite = 29
        else:
            limite = 28
    elif mes in [4, 6, 9, 11]:
        limite = 30
    else:
        limite = 31

    if dia < 1 or dia > limite:
        print(f"Dia inválido. O mês {mes} no ano {ano} tem no máximo {limite} dias.")
    else:
        print(f"{ano:04d}-{mes:02d}-{dia:02d}")
'''


'''
#ATVD18
expressao = input("Digite a expressão matemática: ")
resultado = eval(expressao)
print(f"Resultado: {resultado}")
'''

##############################DESAFIO###############################

#ATVD19
cpf = input("Digite o número do CPF (formato XXX.XXX.XXX-XX): ")
cpf = ''.join(filter(str.isdigit, cpf))

if len(cpf) != 11:
    print("CPF Inválido")
else:
    pesos1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum(int(cpf[i]) * pesos1[i] for i in range(9))
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1

    pesos2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = sum(int(cpf[i]) * pesos2[i] for i in range(9)) + digito1 * pesos2[9]
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    if cpf[-2:] == f"{digito1}{digito2}":
        print("CPF Válido")
    else:
        print("CPF Inválido")
