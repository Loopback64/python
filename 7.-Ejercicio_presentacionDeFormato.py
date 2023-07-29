#Ejemplo 7. Presentación de formato de tipos de datos
#Muestre en pantalla un conjunto de tipos de datos con el uso de la función format.

"""Solución :El problema requiere mostrar un conjunto de datos almacenados en variables, se utilizará
format( ) un método que referencia a lugares dentro de una cadena de caracteres, este método
utiliza las llaves para la ubicación dentro de la cadena."""

t = "variablestring"   #variable string
n = 23           #entero

print("puedo poner el texto que quiera luego sigue la variable cargada t y es = ",t,"ahora sigue la variable numero n que es", n)

m = "Otra manera de poner el valor de la avariable texto t que es  {} ahora un numero que es n '{}' ".format(t,n)

print(m)                 #uso de funcion de formato a referencia
print(3*t+t )            #triplicar string y concatenar



























