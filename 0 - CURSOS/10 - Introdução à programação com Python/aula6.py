conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)
conjunto_diferenca = conjunto.difference(conjunto2)
print(conjunto_diferenca)
#dif simetrica = tudo que tem num conjunto mas no outro nao tem
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('diferença simetrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5,6,7}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é um subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

conjunto_c = {10,20,30,40,50}
conjunto_c.discard(40)
print(conjunto_c)

# conjunto = {1, 5, 7,7, 9}
# print(type(conjunto))
# conjunto.add(6)
# conjunto.discard(7) #retira o elemento do conjunto
# print(conjunto)
