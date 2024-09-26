#Desarrollar un programa que lee un valor y determine su factorial.

print (" ")
print ("Torres Olvera Gael")
print (" ")

#establece la orden al sistema para poder proporcionar la factorial
def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Leer un valor que el usuario proporciona y proporcionarle la factorial
try:
    number = int(input("Introduce un número entero para calcular su factorial: "))
    print(f"El factorial de {number} es: {factorial(number)}")
except ValueError:
    print("Por favor, introduce un número entero válido.")
