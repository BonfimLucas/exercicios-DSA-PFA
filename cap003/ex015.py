num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))


somar = lambda num1, num2: num1 + num2
print ("A soma dos números é: ", somar(num1,num2))