while True:
    try:
        if (hora := int(input('Que horas são (em numero inteiro)? '))) >= 0 and hora <= 11:
            print('Bom dia!')
        elif hora >= 12 and hora <= 17:
            print('Boa tarde!')
        elif hora >= 18 and hora <= 23:
            print('Boa noite!')
        else:
            print('Passou do padrão normal da hora!')
    except:
        print('Valor invalido!')