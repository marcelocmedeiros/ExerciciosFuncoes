# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

  
'''
3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma 
desses três argumentos.
'''

def soma3(a, b, c):
    """soma três números

    Arguments:
        a 1° parametro
        b 2° parametro
        c 3° parametro

    Returns:
        soma -- a + b + c
    """
    s = a + b + c
    return s


#programa principal 
print('SOMA DE TRÊS NÚMEROS')
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

print('Soma = ', soma3(a, b, c))