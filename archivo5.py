numeros = input("Ingrese una serie de números separados por espacios: ")  # Solicitar al usuario que ingrese una serie de números
numeros_lista = numeros.split()  # Dividir la cadena en una lista de números

suma = 0  # Variable para almacenar la suma de los números

# Recorrer cada número en la lista y sumarlo a la variable suma
for numero in numeros_lista:
    suma += int(numero)

print("La suma de los números es:", suma)  # Mostrar la suma de los números