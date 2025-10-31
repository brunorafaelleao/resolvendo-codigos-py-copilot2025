questao = "Vamos receber dois dados diferentes do usuário e concatena-los em uma única string"
print(questao)
# Recebendo dois dados do usuário
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")
# Concatenando os dados em uma única string
# Exibindo o resultado
'''
print("A concatenação dos dados é: ${dado1} ${dado2}")

aqui eu tinha errado a forma de concatenar as strings, agora está correta segundo o chatGPT:
Maneiras corretas de fazer:
1. Usando f-string (recomendado):
print(f"A concatenação dos dados é: {dado1} {dado2}")
'''

print(f"A concatenação dos dados é: {dado1} {dado2}")

"""
Saída esperada:
Vamos receber dois dados diferentes do usuário e concatena-los em uma única string
Digite o primeiro dado: informática
Digite o segundo dado: básica
A concatenação dos dados é: informática básica
"""