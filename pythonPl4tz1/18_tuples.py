numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico' )

print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# CRUD
# numbers.append(10)
print(numbers)
# numbers[1] = 'change'

print(strings)
print(strings.index('zule'))   # Me indica en que posicion esta el string 'zule'
print(strings.count('nico'))   # Me indica cuantas veces se repite el string 'nico'

my_list = list(strings)  # Convierte el string en list
print(type(my_list))

# Ahora siendo una lista puedo cambiar los valores de la lista

my_list[1] = 'juli'  # Agregamos julia  la lista
print(my_list)

my_tuple = tuple(my_list)   # Convertimos nuevamente a tupla
print(my_tuple)














