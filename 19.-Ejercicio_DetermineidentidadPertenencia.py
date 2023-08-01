# Determine la identidad y pertenencia

"""  En Python encontraremos operadores que determinan la identidad de un objeto en una
referencia, así como la pertenencia de un valor en una variable. En la siguiente figura, podemos
utilizar los operadores de pertenencia e identidad disponibles: """


num1 = 3 
num2 = 3.0
letra = "3"
num3 = 5
num4 = 3
conjunto = [ 1,2,3,4]
palabra = "universidad"
lista1 = ["cristina", "Sebastian" ]
tupla1 =  ("cristina", "Sebastian")
#identidad

print("Identidad")
print("1: " ,num1 is num2)
print("2: " ,num1 is letra) 
print("3: " ,num1 is num3)
print("4: " ,num1 is num4)
print("5: " ,num1 is palabra) 
print("6: " ,lista1 is tupla1)
#pertenencia

print("Pertenencia")
print("7: ","univer" in palabra)
print("8: ",num1 in conjunto)



