
# Programa que simula el ingreso de n notas.

""" Escriba un programa que permita el ingreso de n notas de una asignatura, calcule el promedio y
lo presenta en pantalla, adicionalmente para detener el ingreso deberá usar el número -99.



Solución: (Análisis)
Para este programa, el uso del contador no está explícito, dependerá de la cantidad de notas
que el usuario desee ingresar n, siendo el número -99 un valor de ingreso como una nota, pero
sin ser tomado en cuenta. A este valor se lo conoce como valor centinela. Un valor señuelo que
indica al programa la finalización de ingresos a través de la variable nota. Adicionalmente una
variable está implícita, el acumulador de notas (que no acumula el último valor) para luego
obtener el promedio. Para este problema, similar al anterior, utiliza nombres similares en sus
variables, es la forma de utilizar la estructura repetitiva lo que va a cambiar, observe la condición
de este programa.

"""


print("LIBRETA ESCOLAR")
print("Asignatura Programación")

acum,i = (0, 0.0)
nota, promedio = (0, 0.0)

print("Ingrese notas a continuación, -99 para finalizar")
print("Nota [",(i+1),"]", end=" ")

nota = float(input("Ingrese: "))
while(nota!=-99):
    acum = acum + nota
    i = i + 1
    print("Nota [",(i+1),"]",end=" ")
    nota = float(input("Ingrese: "))
if(i>0):
    promedio = acum/i
    print("Promedio: ",promedio)
else:
    print("Finalizó el programa")



    





    































