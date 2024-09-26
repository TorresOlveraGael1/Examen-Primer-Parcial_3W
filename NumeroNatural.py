#Solicitar al usuario un número natural

print (" ")
print ("Torres Olvera Gael")
print (" ")

A = int(input("Introduce un valor: ")) #Solcita un valor al ususario

print (" ") #Salto de linea

#Abrimos cadena 'If'
if A <= 12:
    print ("El numero es:", A, "Y esta dentro del rango de la primera docena de numeros")
else:
    print ("El numero es:", A, "Y NO esta dentro del rango de la primera docena de numeros")

print (" ") #Salto de linea

#Abrimos segunda cadena 'If'
if A % 2 == 0 :
    print ("El numero es par")
else:
    print ("El numero es impar")