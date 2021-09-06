from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print (data_atual)
    data_atual_str = data_atual.strftime('%d/%m/%y %H:%M%S h')
    print(data_atual_str)
    print(data_atual.strftime('%c')) #%c mostra dia sem, mes ext, dia e hora, min, seg e Ano 4 dig
    print(data_atual.weekday())
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2020, 1, 18, 15, 30, 2)
    print(data_criada)
    print (data_criada.strftime ('%c'))
    data_string = '02/03/2020 12:40:03'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=3, minutes=10) #calculo com data, usar timedelta
    print(nova_data)

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A/%B/%Y') #%A=Dia semana, %B=Mes extenso, %Y= ano com 4 digitos
    data_atual_str = data_atual.strftime('%d/%m/%Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario_str))
    print(horario_str)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()

