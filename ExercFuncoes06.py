# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.
  
  
'''
6. Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre 
a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar 
as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que 
permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
'''

def formatar(h, m):
    horas = ''
    # foi usado o str p concatenar os valores e ficar na forma pedida
    if h > 12: #pm
        horas = str(h - 12) + ':' + str(m) +' P.M'
    else: #am
        horas = str(h) + ':' + str(m) + ' A.M'
    # retornou a hora conforme requerido
    return horas


#programa principal
# loop que permita que o usuário repita o cálculo 
while True:
    # um print p informar condição de parada do calculo -1
    print('Digite -1 para sair')
    horas = int(input('Digite as horas: '))
    if horas < 0:
        break
    minutos = int(input('Digite os minutos: '))

    print(formatar(horas, minutos))