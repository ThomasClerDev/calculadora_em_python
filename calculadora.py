import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Impossível dividir por zero!")
        return
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        print("Impossível calcular raiz quadrada de números negativos!")
        return
    return math.sqrt(x)

def logarithm(x):
    if x <= 0:
        print("Impossível calcular logaritmo de números negativos ou iguais a zero!")
        return
    return math.log10(x)

print("Selecione a operação.")
print("1.Adição")
print("2.Subtração")
print("3.Multiplicação")
print("4.Divisão")
print("5.Potência")
print("6.Raiz Quadrada")
print("7.Logaritmo")

choice = input("Enter choice(1/2/3/4/5/6/7): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
    print(num1,"^",num2,"=", power(num1,num2))

elif choice == '6':
    print("√",num1,"=", square_root(num1))

elif choice == '7':
    print("log(",num1,")=", logarithm(num1))
else:
    print("Opção inválida.")
