import os
from time import sleep

lista_compras = []
produto = ''

while True:
    opcao = input('Selecione uma opção\n'
                '[i]nserir [a]pagar [l]istar: ')
    try:
        if opcao[0] == 'i':
            os.system('cls')
            produto = input('Qual produto gostaria de inserir? ')
            lista_compras.append(produto)
            print('Produto inserido com sucesso!')
            sleep(2)
            os.system('cls')
        elif opcao[0] == 'a':
            os.system('cls')
            posicao = int(input('Qual indice você gostaria de deletar? '))
            try:
                item_excluido = lista_compras.pop(posicao)
                print(f'Produto {item_excluido} excluido com sucesso!')
                sleep(2)
            except:
                print('Indice invalido...\n')
                sleep(1)
                os.system('cls')
        elif opcao[0] == 'l':
            if bool(lista_compras) is False:
                os.system('cls')
                print('Não a nada na lista ainda para listar...')
                sleep(1)
                os.system('cls')
                continue
            else:
                os.system('cls')
                print('-=' * 20)
                for indice, compras in enumerate(lista_compras):
                    print(f'{indice} - {compras}')
                print('-=' * 20)
        else:
            print('Valor invalido...')
    except:
        print('Insira algum valor.')