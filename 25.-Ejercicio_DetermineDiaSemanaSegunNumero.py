# Determine el día de la semana dependiendo de un número ingresado
""" Escriba un programa que permita el ingreso de un número que represente un día de la semana.
Su programa debe mostrar el nombre del día.

Solución: (Análisis)
Utilizaremos una estructura llamada diccionario de almacenamiento para alojar los posibles
nombres de los días a utilizar. """

diccionario = {    
        1: "lunes",
        2: "martes",
        3: "miercoles",
        4: "jueves",
        5: "viernes",
        6: "sabado",
        7: "domingo"
}

dia = int(input("Ingrese el número del dia: "))
print("Dia:",diccionario[dia])
                               







