import os 

palavra_secreta = 'tomate'
palavra_secreta = list(palavra_secreta)
palavra_oculta = '*' * len(palavra_secreta)
letra_usuario = input('Digite uma letra: ').strip().lower()
i = tentativas = 0

while True:  
    if len(letra_usuario) != 1 or letra_usuario.isdigit():
        letra_usuario = input('Digite apenas uma letra: ')
        continue 

    if letra_usuario in palavra_secreta:
        palavra_oculta = list(palavra_oculta)
        for a in palavra_secreta:
            if letra_usuario == a:
                palavra_oculta[i] = letra_usuario
            i += 1
        i = 0
        palavra_oculta = ''.join(palavra_oculta)
    print(palavra_oculta)
    tentativas += 1
    if '*' not in palavra_oculta:
        break
    letra_usuario = input('Digite uma letra: ').strip().lower()
os.system('cls')
print('Você acertou a palavra secreta!')
print(f'Você tentou {tentativas} vezes.')