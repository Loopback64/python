# CRUD Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5]
print(numbers)
print('imprime el orden de elemento inicia en 0,1,2,3,4')
print(numbers[1])
numbers[-1] = 10
print('Se cambio el ultimo elemento por 10')
print(numbers)

print('-------------')

numbers.append(700) #agrega a la ultima posicion el entero 700
print('Agrega al ultimo elemento el valor de 700')
print(numbers)
print('-------------')

print('Agrega el valor de "hola" al inicio de la tabla')
numbers.insert(0,'hola')
print(numbers)
print('-------------')
print('agrega al lugar 3 el elemento "change" ')

numbers.insert(3,'change')
print(numbers)
print('-------------')

tasks = ['todo 1', 'todo 2', 'todo 3']
print(numbers)
print(tasks)
print('-------------')
print('-------------')
print('-------------')

print('Unimos los valores de los elementos de las tablas numbers y tasks')

new_list = numbers + tasks
print(new_list)
print('-------------')


# preguntamos en qe posicion esta un elemento
index = new_list.index('todo 2')

print(index)
print('camia el valor de "todo 2" por el valor "todo changed"')
new_list[index] = 'todo changed'

print(new_list)

print('-------------')
print('-------------')


print("removemos parte de la lista usando el metodo remove,  todo 1")
new_list.remove('todo 1')
print(new_list)

# metodo que elimina automaticamente el ultimo elemento de una lista .pop


print('-------------')
print('-------------')

print('metodo que elimina automaticamente el ultimo elemento de una lista .pop')

new_list.pop()
print(new_list)

#Tambien puede eleminiar un elemento que ocupa un lugar en la lista, por ejemplo el elemento de de orden 0

print('Elimina un elemento de la lista usando el metodo .pop, con usando el lugar que ocupa en este ejemplo el lugar 0 , es decir el elemento hola ')
new_list.pop(0)
print(new_list)

#Usando el metodo reverse
print('-------------')
print('-------------')

print('Usamos el metodo .reverse para poder revertir o invertir el orden de la lista')


new_list.reverse()
print(new_list)


#Usamos un metodo para ordenar una lista de menor a mayor

print('-------------')
print('-------------')

print('Usamos el metodo .sort para ordenar una lista de numeros de menor a mayor ')

numbers_a = [  1, 4, 6 ,3 ]
print(numbers_a)
numbers_a.sort()

print(numbers_a)



print('-------------')
print('-------------')

#Ahora ordenamos strings en la lista re , ab , ed   usando el metodo sort

strings = [ 're' , 'ab' , 'ed'  ]

print(strings)

strings.sort()

print(strings)

#El metodo sort no funciona cuando tenemos datos mezclados como numero y letras 
print('El metodo .sort no funciona cuando tenemos numeros con letras mezclados')
print('-------------')
print('-------------')

print('Usando lista de numeros y letras para probar metodo .sort')
#sale un error
#   print(new_list)
#   new_list.sort()






print('-------------')
print('-------------')


print('-------------')
print('-------------')



print('-------------')
print('-------------')



print('-------------')
print('-------------')
