my_dict = {}    # los diccionarios se escriben entre corchetes
print(type(my_dict))      #

my_dict = {
    'avion'     : 'bla bla bla bla ' ,
    'name'      : "Nicolas"          ,
    'last_name' : 'Molina Monroy'    ,
    'age'       : "87"                ,

}

print(my_dict)
print(len(my_dict))

#puedo hacer consultas al diccionario usando
print("------------")
print(my_dict["age"])
print(my_dict['last_name'])
print(my_dict.get('unvalor')) # previene un error sino existe

# Como ver si existe un valor en el diccionario

print('avion' in my_dict)
print('otroqueno' in my_dict)










