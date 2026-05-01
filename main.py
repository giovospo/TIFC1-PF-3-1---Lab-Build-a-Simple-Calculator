# Programa que recibe dos números, los suma y muestra el resultado

num1 = float(input("ingrese el primer número: "))
num2 = float(input("ingrese el segundo número: "))

resultado = num1 + num2
print(resultado)

# Funcion extra Menú de operaciones con dos números

print("\nOperaciones adicionales disponibles:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Módulo")

opcion = input("Elige una opción (1-5): ")

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if opcion == "1":
    print("Resultado:", a + b)
elif opcion == "2":
    print("Resultado:", a - b)
elif opcion == "3":
    print("Resultado:", a * b)
elif opcion == "4":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Error: división por cero")
elif opcion == "5":
    print("Resultado:", a % b)
else:
    print("Opción no válida")

# Función extra: Sumar 3 números

n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))

print("Resultado:", n1 + n2 + n3)

# Función extra: Operaciones combinadas de 3 números o más

expresion = input("Ingresa una operación matemática (ej. 2 + 4 - 3): ")

try:
    print("Resultado:", eval(expresion))
except:
    print("Expresión inválida")