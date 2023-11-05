while True:
    if len((nome := input('Informe um nome: '))) <= 4:
        print('O nome é pequeno!')
    elif len(nome) >= 5 and len(nome) <= 6:
        print('O nome é normal.')
    elif len(nome) > 6:
        print('O nome é muito grande!')