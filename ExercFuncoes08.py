# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.
  
  
'''
8. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
'''

def inteiros(n):
    return len((str(n)))


#programa principal
# n = str p na def "n" ser contado pela função len() q conta caracter e strip p tirar os espaços
n = str(input('Digite um número inteiro : ')).strip()
print(f'Esse número tem {inteiros(n)} dígitos')