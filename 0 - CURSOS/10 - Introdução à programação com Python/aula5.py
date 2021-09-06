lista = [12,10, 7, 5]
lista_animal = ['cachoro', 'gato', 'elefante', 'lobo', 'arara']

#tuplas nao consegue alterar valores usa ()
tupla = (1, 5, 9, 17)
print(tupla)
print(len(tupla))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0]=100
print(lista_numerica)

# listas consegue alterar o valores usa []

# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

# if 'lobo' in lista_animal:
#     print('existe lobo na lista')
# else:
#     print('não existe lobo na lista. será incluído')
#     lista_animal.append('lobo')
#     print(lista_animal)
#
#     #lista_animal.pop(3) #retira da lista (3) posição
#     lista_animal.remove('elefante') #remove da lista pelo nome
#     print(lista_animal)
