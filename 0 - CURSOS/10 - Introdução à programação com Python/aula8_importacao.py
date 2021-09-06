from aula7televisao import Televisao      #importa a classe dentro do módulo
from aula7calculadora1 import Calculadora #importa a classe dentro do módulo
from aula8_contador_letras import contador_letras #importa o método dentro do módulo

if __name__ == '__main__':
    televisao = Televisao() #instancia a classe
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(10,5) #instancia a classe e envia os valores para o calculo
    print(calculadora.soma())
    lista = ['cachorro', 'jacaré', 'urso'] #popula a lista
    total_letras = contador_letras(lista)  #chama o método
    print('Total de Letras por palavra: {}'.format(total_letras)) #printa o resultado

