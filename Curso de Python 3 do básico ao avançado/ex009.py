def multi(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

numeros = []

while True:
    try:
        numero = int(input('Digite um numero: '))
    except:
        break
    if numero == 0:
        break
    numeros.append(numero)

resultado = multi(*numeros)
print(resultado)