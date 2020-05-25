# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.
  
'''
5. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é 
custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto 
sobre vendas
'''

def somaImposto(taxaImposto, custo):
    """Valor fim do produto mais imposto

    Arguments:
        taxaImposto valor do imposto
        Custo valor do produto

    Returns:
        valor com o imposto
    """
    return custo + ((custo * taxaImposto) / 100)


#programa principal
print('SOMA DOS IMPOSTOS')    
t = float(input('Digite a taxa de imposto: '))
c = float(input('Digite o custo: '))
print('Valor com imposto:', somaImposto(t,c))