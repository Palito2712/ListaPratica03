numeroUmAdez = int(input("Digite um valor inteiro de 1 a 10 para saber a sua tabuada: "))

if numeroUmAdez <= 10 and numeroUmAdez > 0:

    for numero in range(1, 11):
        print(numero * numeroUmAdez)