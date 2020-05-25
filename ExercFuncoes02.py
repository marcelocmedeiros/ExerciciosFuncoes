# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
2. Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
'''


n = int(input('Digite o número: '))

def lista(n):
    # laço for vai percorrer (i = 1 e fim = n+1)
    for i in range(1, n + 1):
        # criei uma lista para impresão ser no modelo acima
        l = []

        for j in range(i):
            # a lista será add +1 p ficar com números distintos
            l.append(str(j+1))
        print(' '.join(l))
lista(n)