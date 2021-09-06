a = int(input('Entre com o valor:'))

for num in range(a+1):
    div = 0
    for x in range(1,num+1):
        resto = num % x
        #print(x, resto)
        if resto == 0:
            div += 1

    if div == 2:
        print('número {} é primo'.format(num))


# a = int(input('Entre com o numero:'))
#
# div = 0
# for x in range(1,a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('número {} é primo'.format(a))
# else:
#     print('número {} não é primo'.fomat(a))

