# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.
  
  
'''
9. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721.
'''

def reverso(n):
    return str(n[::-1])


#programa principal
# n = str p na def "n" ser invertido dentro lista [::-1] e strip p retirar os espaços
n = str(input('Digite um número: ')).strip()
print(f'Reverso: {reverso(n)}')