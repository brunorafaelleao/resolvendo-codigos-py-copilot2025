print("Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")
if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif operacao == "-":     
    resultado = num1 - num2             
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2             
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2             
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
        

