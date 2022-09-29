list = []

while len(list) < 5:

    numeros = int(input("Digite um número: "))
    list.append(numeros)

for numero in list:

    if numero % 2 == 0:
        print("Esse número é par: ", numero)

    else:
        print("Esse número é ímpar: ", numero)