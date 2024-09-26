#Ingresar un número entero para saber si es divisible por 7 y es mayor a 40.

print (" ")
print ("Torres Olvera")
print (" ")

A = int(input("Introduce un valor: ")) #Solcita un valor al usuario

print (" ") #Salto de linea

div = A/7 #Ordena al sistema realizar una operacion


#Abrimos cadena 'If'
if div > 40:
    print (div, "Es superior a 40")
else:
    print (div, "No es superior a 40")