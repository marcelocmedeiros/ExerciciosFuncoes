# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
13.Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres 
‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que 
o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da 
faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma 
elegante
'''
# 1° def do valor mínimo ou em branco
def valor_por_omissao(valor):
    # caso deixe em branco mínimo == a 1 
    if valor=='':
        return int(1)
    else:
        return faixa_minima_maxima(int(valor))
# 2° def com o valor máximo é 20
def faixa_minima_maxima(valor):

    if valor<1:
        return 1
    # se digitar > 20 retorne == 20
    elif valor>20:
        return 20
    else:
        return valor
# 3° def cria a linha
def cria_linha(linha):
    l='+'
    for x in range(linha):
        l+='-'
    l+='+'
    print (l)
# 4° def cria a coluna
def cria_coluna(linha, coluna):
    for y in range(coluna):
        c='|'
        c+= ' '*linha
        c+='|'
        print (c)
# 4° def mostrar a moldura
def desenha_moldura(linha, coluna):
    cria_linha(linha)
    cria_coluna(linha, coluna)
    cria_linha(linha)


# programa principal
linha=input('Diga quantos +----+, entre 1 e 20: ')
coluna=input('Diga quantos |    |, entre 1 e 20: ')
desenha_moldura(valor_por_omissao(linha), valor_por_omissao(coluna))