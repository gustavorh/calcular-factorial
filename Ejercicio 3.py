# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:04:06 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""


# Esta función calculará el valor factorial de un número ingresado por el usuario
def calcularFactorial(numero):
    fact = 1  # Se inicializa con valor 1 la variable 'fact' (factorial)
    # Ciclo el cual multiplicará el valor anterior por el numero siguiente hasta n (numero)
    for num in range(2, numero+1):
        # Se multiplica el valor en memoria por el valor en el que va el ciclo (num)
        fact *= num
    return fact  # Se devuelve el resultado final como fact


numero = int(input("Ingrese un número para calcular el factorial: "))
# Se le entrega a la función calcularFactorial el parámetro número
factorial = calcularFactorial(numero)

sumatoria = 0
exponente = 0
sumatoria_antigua = -1

diferencia = (sumatoria - sumatoria_antigua)
elevado = (1 / 100000)  # 10 ^ -5

while (diferencia > elevado):
    sumatoria_antigua = sumatoria
    # Serie de Taylor guardado en una suma acumulada
    sumatoria += (numero ** exponente) / calcularFactorial(exponente)

    exponente = exponente + 1  # Se incrementa el exponente para el siguiente ciclo
    # Actualizamos la variable diferencia dentro del ciclo
    diferencia = sumatoria - sumatoria_antigua


print(f'El factorial del número {numero} es: {factorial}')  # Resultado final
print(f"Según la Serie de Taylor, el valor de {numero} es: {sumatoria}")
