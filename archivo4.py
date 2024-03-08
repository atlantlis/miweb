peso = float(input("Ingrese su peso en kilogramos: "))  # Solicitar al usuario que ingrese su peso en kilogramos
altura = float(input("Ingrese su altura en metros: "))  # Solicitar al usuario que ingrese su altura en metros

imc = peso / (altura ** 2)  # Calcular el índice de masa corporal (IMC)

print("Su índice de masa corporal (IMC) es:", imc)  # Mostrar el IMC