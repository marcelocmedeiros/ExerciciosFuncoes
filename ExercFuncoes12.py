# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
12. Embaralha palavra. Construa uma função que receba uma string como parâmetro e 
devolva outra string com os carateres embaralhados. Por exemplo: se função receber 
a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, 
de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos 
em caixa alta ou caixa baixa, independentemente de como foram digitados.
'''


def embaralha(nome):
    #importe shuffle embaralhar as letras reorganizando-as
    from random import shuffle
    # a =  lista da variével nome 
    a = list(nome)
    # metodo shuffle em (a) p reorganizar
    shuffle(a)
    # e join(a) juntar
    a = ''.join(a)
    # imprimir tudo em maiúscula
    print(a.lower())


# programa principal
nome = input('Digite algo: ')
embaralha(nome)