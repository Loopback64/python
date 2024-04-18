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



