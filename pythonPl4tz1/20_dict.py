print("******************************************************************")
print("******************************************************************")

print("Mostramos los valores cargados en el diccionario llamado person")
print("-----------------------------------------------------------------")

person = {
    'name' : 'nico',
    'last_name' : 'molina',
    'langs' : ['python' , 'javascript'],
    'age' : 99
}

print(person)

print("-----------------------------------------------------------------")
print("-----------------------------------------------------------------")
print("-----------------------------------------------------------------")
print("Ahora cambiamos el valor name a santi --- a la edad le restamos 50 , agregamos rust al final de la lista")
print("y mostramos el resultado")
print("-----------------------------------------------------------------")



person['name'] = 'santi'
person['age'] -= 50 # al valor actual le restamos 50
person['langs'].append('rust')  # Usamos el metodo .append para agregar un valor al final de la lista
print(person)

del person['last_name']  # eliminamos el atributo
person.pop('age')
print("-----------------------------------------------------------------")

print('name')
print(person)


