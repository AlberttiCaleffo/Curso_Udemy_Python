# def multi(numero):
#     def duplicar():
#         return numero * 2
#     def triplicar():
#         return numero * 3
#     def quadruplicar():
#         return numero * 4
#     return duplicar(), triplicar(), quadruplicar()
    
# n = multi(4)

# print(*n)
# print(*n)

def criar_multi(*multiplicador):
    resultado = []
    def multi(numero):
        resultado.clear()
        for n in multiplicador:
            resultado.append(numero * n)
        return resultado

    return multi

n = criar_multi(2, 3, 4)

print(*n(10))
print(*n(23))
print(*n(2))
