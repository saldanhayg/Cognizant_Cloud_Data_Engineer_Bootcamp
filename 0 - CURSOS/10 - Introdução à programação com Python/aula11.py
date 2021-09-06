'''
Tratamento de erros e excessões, sempre codificar do filho para o pai
https://docs.python.org/3/library/exceptions.html #documentação das excessões
'''
lista =[1, 10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex: #BaseException é o pai das excessões dentro da árvore
    print('Erro desconhecido! {}'.format(ex))
else:
    print('Executa quando Não houve nenhuma excessão')
finally:
    print('sempre executa')
    print('fechando arquivo')
    arquivo.close()
