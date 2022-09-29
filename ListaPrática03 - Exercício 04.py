list = []

while len(list) < 5:

    idade = int(input("Digite uma idade: "))
    list.append(idade)

    if len(list) == 5:
        print("A média das idades informadas é: ", sum(list) / 5)
        break