print("Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.")
texto = input("Por favor, insira uma string: ")
repeticoes = int(input("Por favor, insira um número inteiro: "))
resultado = texto * repeticoes
print(f"O resultado é: {resultado}")
"""
Saída esperada:
Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.
Por favor, insira uma string: bola
Por favor, insira um número inteiro: 3
O resultado é: bolabolabola

perguntei ao chatgpt para gerar esse código para mim com espaço entre as strings repetidas. Sugestão dele:
Para colocar um espaço entre elas, você pode usar o método .join() em conjunto com uma lista de repetições, assim:

texto = input("Por favor, insira uma string: ")
repeticoes = int(input("Por favor, insira um número inteiro: "))
resultado = ' '.join([texto] * repeticoes)
print(f"O resultado é: {resultado}")
"""

## usando a sugestão do chatgpt para repetir com espaço entre as strings
resultado2 = ' '.join([texto] * repeticoes)
print(f"O resultado é: {resultado2}")