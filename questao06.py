print("palavra é um palíndromo?")

palavra = input("Digite uma palavra: ")

inverso = palavra[::-1]
if palavra == inverso:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")



"""
Pedi ao chatgpt ajuda sobre como criar um código que verifique se uma palavra é um palíndromo. Abaixo está o código que ele me forneceu com a orientação
detalhada de como funciona a parte do código que inverte a string usando a sintaxe [::-1].
🧩 Passo a passo:

palavra → é uma string previamente definida, por exemplo:

palavra = "python"


[::-1] → é uma sintaxe de fatiamento (slice) em Python.
O formato geral do slice é:

[início:fim:passo]


início → índice inicial (opcional)

fim → índice final (opcional)

passo → de quantos em quantos índices o Python deve andar

Quando você usa [::-1]:

deixa início e fim em branco (ou seja, pega a string toda),

e define o passo como -1, o que significa “andar de trás pra frente”.


"""