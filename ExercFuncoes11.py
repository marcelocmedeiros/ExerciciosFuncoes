# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.

'''
11. Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA 
e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data 
e retorne NULL caso a data seja inválida.
'''
import re

# 1° def verificar dia e mes 
def validaData(dia, mes, ano):
    # Valida o dia 
    if (dia < 0) or (dia > 31):
        return False
    # verificar se o ano é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        bissexto = "sim"
    else:
        return False
    # verifica se o mês está dentro dos valores
    if mes < 1 or mes > 12:
        return False
    # analisa os meses de 30 e 31 dias
    if dia > 31 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30):
        return False
    # analisa o mês de fevereiro e se ele é bissexto
    if (mes == 2 and bissexto == "nao" and dia > 28) or (mes == 2 and bissexto == "sim" and dia > 29):
        return False
    # tudo ok retorna verdade e imprime o nome do mês
    return True
# 2° def para escrever o nome do mês por extenso
def dataPorExtenso(data):
    # Valida o formato da data por expressao regular
    reg = re.compile('^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$')
    if (not (reg.match(data))):
        print ('Data invalida')
        return None

    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    if (not validaData(dia, mes, ano)):
        return None

    mesExtenso = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho',
                  'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
                  'Dezembro')
    # como o mês está em uma tupla é mes-1 para ser igual ao indice da lista
    return '%d de %s de %d' % (dia, mesExtenso[mes - 1], ano)

# Fluxo Principal

data = input('Informe uma data no formato dd/mm/yyyy: ')
print(dataPorExtenso(data))