# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
1. Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
'''
# função lista 
def lista(n):
    
    return list(str(n) * n)

# programa principal 
n = int(input('Digite o número: '))
# laço for p impresão em interada (i = 1 e fim = n+1)
for i in range(1, n + 1):
    # metodo join para junta um espaço em branco ao "n" da lista(i)
    print(' '.join(lista(i)))