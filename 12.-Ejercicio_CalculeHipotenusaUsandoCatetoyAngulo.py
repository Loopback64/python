# Escriba un programa que calcule la hipotenusa de un triángulo rectángulo, dados un cateto y un ángulo.

"""Solución: (Análisis)
El problema nos pide el uso de las funciones trigonométricas.

El ángulo 𝜃 y uno de los catetos son dados para el problema, se debe recordar las identidades trigonométricas 𝜃
           
           𝐶𝑜𝑠 𝜃 =  𝑎𝑑𝑦𝑎𝑐𝑒𝑛𝑡𝑒
                    ℎ𝑖𝑝𝑜𝑡𝑒𝑛𝑢𝑠𝑎

Para nuestro problema debemos utilizar el arcoseno o coseno inverso para obtener:
                  
                ℎ𝑖𝑝𝑜𝑡𝑒𝑛𝑢𝑠𝑎 = 𝑎𝑑𝑦𝑎𝑐𝑒𝑛𝑡𝑒
                              cos' 𝜃                                              """

import math 
a = 3
b = 4
c = 5

angulo = 53.1301023541

h = a / math.cos(angulo*math.pi/180)

print("Hipotenusa:  ",h )
identidad = 3/5
te = math.acos(identidad)
print("Angulo",te*180/math.pi)

