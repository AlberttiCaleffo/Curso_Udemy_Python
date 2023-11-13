from random import randint
import sys

gerar_aleatorio = False
insercao_cpf = input('Digite seu cpf para verificar ou digite [1] para gerar um aleatorio valido: ').strip()

if insercao_cpf == '1':
    gerar_aleatorio = True
    insercao_cpf = str(randint(10000000000, 99999999999))

while True:
    if '.' in insercao_cpf:
        insercao_cpf = insercao_cpf.replace('.', '')
    if '-' in insercao_cpf:
        insercao_cpf = insercao_cpf.replace('-', '')
    if len(insercao_cpf) * insercao_cpf[0] == insercao_cpf:
        print('Valor repetido...')
        insercao_cpf = input('Insira um cpf valido: ')
    elif insercao_cpf.isdigit() and len(insercao_cpf) == 11:
        break
    else:
        print('Valor invalido...')
        insercao_cpf = input('Digite novamente seu cpf: ')
primeiros_9 = insercao_cpf[:9]
    
# for i, numero in enumerate(primeiros_9[::-1], 2):
#     resultados.append(int(numero) * i)
resultados = [int(numero) * i for i, numero in enumerate(primeiros_9[::-1], 2)]

resultado = sum(resultados) * 10 % 11
primeiros_10 = primeiros_9 + str(resultado)

# for i, numero in enumerate(primeiros_10[::-1], 2):
#     resultados_2.append(int(numero) * i)
resultados_2 = [int(numero) * i for i, numero in enumerate(primeiros_10[::-1], 2)]
resultado_2 = sum(resultados_2) * 10 % 11

if resultado > 9:
    resultado = 0
if resultado_2 > 9:
    resultado_2 = 0
 
if gerar_aleatorio:
    insercao_cpf = insercao_cpf[:9] + str(resultado) + str(resultado_2)
    print(f'O CPF gerado foi {insercao_cpf}')
    sys.exit()
    
print(f'O CPF informado foi {insercao_cpf}')
print(f'O resultado do primeiro digito é: {resultado}\n'
      f'O resultado do segundo digito é: {resultado_2}')

if str(resultado) in insercao_cpf[9] and str(resultado_2) in insercao_cpf[10]:
    print('CPF Valido!')
else:
    print('CPF Invalido!')