
#Horas trabajadas por un empleado 

"""Calcular el sueldo mensual de un trabajador conociendo la cantidad de horas trabajadas y el
pago por hora."""


"""Solucion : El problema requiere de una fórmula específica,
                   
                   𝑠𝑢𝑒𝑙𝑑𝑜 = ℎ𝑜𝑟𝑎𝑠 𝑡𝑟𝑎𝑏𝑎𝑗𝑎𝑑𝑎𝑠 ∗ 𝑐𝑜𝑠𝑡𝑜ℎ𝑜𝑟𝑎

Se ingresan valores como entrada y se obtienen valores enteros o reales de salida.
Valor de entrada 1 al programa = cantidad de horas trabajadas = CHT
Valor de entrada 2 al programa = pago por hora = PPH
Valor de salida del programa = sueldo = CHT * PPH
Proceso = fórmula identificada """


CHT =  input("Ingrese horas de trabajo: ")
print("Costo por hora:  ", end = " ")
PPH = input()
sueldo = int(PPH)*int(CHT)
print("Sueldo es: ", sueldo)























