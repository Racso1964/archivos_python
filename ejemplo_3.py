# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def calcular_promedio(objetivo):
    #print("¡Ejemplo integrador!")
    # Esta función recibe el género del cual
    # se debe calcular la altura promedio
    # puede ser --> femenino o masculino

    # Utilizar el archivo CSV "alturas",
    # el cual posee dos columnas:
    # - genero
    # - altura

    # Profe:
    # - Leer el archivo CSV
    # - Recorrer todas las filas del archivo CSV
    # - En cada iteración obtenga la altura del genero objetivo
    # - Acumule el valor y la cantidad para realizar
    #   el promedio al terminar el bucle

    # --- Comience aquí a desarrollar su código ---


    with  open('alturas.csv', mode='r') as csvfile:
        data = list(csv.DictReader(csvfile))

    #condicionar la entrada de la variable genero

    with  open('alturas.csv', mode='r') as csvfile:
        data = list(csv.DictReader(csvfile))

    #condicionar la entrada de la variable genero

   

    valor = 0
    contador = 0
    for fila in data:
        if fila.get("genero").lower() == objetivo:
            valor += float(fila.get("altura", 0.0))
            contador += 1
    return valor/contador  


if __name__ == '__main__':
   
   genero = str(input("Ingrese el nombre del genero:\n").lower())
   promedio = calcular_promedio(genero)
   print(f"El promedio de la altura es:{promedio}")