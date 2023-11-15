def par_impar(numero):
    if numero % 2 == 0:
        return f'O numero {numero} é Par!'
    return f'O numero {numero} é Impar!'

numero = int(input('Informe um numero: '))

print(par_impar(numero))