class Error(Exception):
    pass

class InputError(Error):
    def __Init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10') #raise força uma excessão
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas numeros!')
    except InputError as ex: #trata a excessão para pedir nova entrada do numero de 1 a 10
        print(ex)


