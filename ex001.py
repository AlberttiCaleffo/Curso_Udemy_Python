while True:
    try:
        if (n := int(input('Digite um numero: '))) % 2 == 0:
            print('O numero é par!')
        else:
            print('O numero é impar!')
    except:
        print('Não é um numero inteiro...')