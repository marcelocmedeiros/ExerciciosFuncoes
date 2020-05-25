# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.
'''
14. Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas,
com um número em cada posição e no qual a soma das linhas, colunas e diagonais
é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
    8  3  4 
    1  5  9
    6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
'''

import random
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
boolean = False
def quadrado_magico():
    global boolean
    # condição quadrado mágico é a soma das linhas, colunas e diagonais é a mesma.
    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz[1][1] + matriz[2][2] == matriz[0][2] + matriz[1][1] + matriz[2][0]:
        boolean = True
    else:
        boolean = False
    return boolean

while boolean == False:
    # lista de [1,9] para forma o quadrado mágico
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # um for dentro de outro for para formar a matriz(3x3)
    for i in range(3):
        for j in range(3):
            #choice retorna um item aleatório de uma lista
            choice = random.choice(vetor)
            matriz[i][j] = choice
            # index retorne o menor i, de modo que i seja o índice da 1° ocorrência de x na matriz.
            indice = vetor.index(choice)
            vetor = vetor[:indice] + vetor[indice + 1:]
    # chama a def(quadrado_magic) 
    quadrado_magico()
    #print da matriz pula uma linha [0], pula uma linha [1] e pula uma linha[2]
    print("\n", matriz[0], "\n", matriz[1], "\n", matriz[2])