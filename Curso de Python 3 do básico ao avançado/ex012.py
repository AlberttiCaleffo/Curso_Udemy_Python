perguntas = [
    {
        'Pergunta': '1° Pergunta: Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': '2° Pergunta: Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': '3° Pergunta: Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

for contador in range(3):
    print(f'{perguntas[contador]["Pergunta"]}\n')
    for indice, opcao in enumerate(perguntas[contador]['Opções']):
        print(f'{indice}) {opcao}')
    resposta = input('Escolha uma opção: ')
    try:
        if resposta.isdigit():
            resposta = int(resposta)
            if perguntas[contador]['Opções'][resposta] == perguntas[contador]['Resposta']:
                print('Acertou!\n')
            else:
                print('ERROU!')
        else:
            print('ERROU!')
    except:
        print('ERROU!')