# Exercicios Listas https://wiki.python.org.br/ExerciciosListas
# Marcelo Campos de Medeiros
# Aluno UNIFIP ADS 2020
# Patos-PB, maio de 2020.
  
  
'''
10. Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par 
de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um 
"natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e 
você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". 
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, 
no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''

# importa as sleep e ra
from random import randint
from time import sleep
# 1° def lança os dados 
def lancamento_dados():
    resultado_lancamento = randint(2, 13)
    return resultado_lancamento
# 2° def verifica os resultados do 1° lanamento
def verificar_resultado(lancamento):
    # condição p ganhar de primeira [7, 11]
    if lancamento in [7, 11]:
        print('=-'*10)
        print("Você tirou: ", lancamento, "\nVocê é um natural e ganhou!")
    # condição p perder de primeira [2, 3, 12]
    elif lancamento in [2, 3, 12]:
        print('=-'*10)
        print("Você tirou: ", lancamento, "\n[Craps] VOCÊ PERDEU!")
    # se não ganha um ponto com os demais resultados
    else:
        print('=-'*10)
        print("Você tirou: ", lancamento, "\nVocê ganhou um Ponto")

        numero_tirado = lancamento
        
        lancamento2 = True
        # loop para os demais resultados
        while numero_tirado != lancamento2:
            # sorteio randint(2, 13)
            lancamento2 = randint(2, 13)
            # se tirar 7 perde a partir do 2° lançamento
            if lancamento2 == 7:
                print('=-'*10)
                print("Você tirou: ", lancamento2, "\nVocê perdeu!")
                break
            # Ganha se tirar o mesmo n° a partir do 2° lançamento
            elif lancamento2 == numero_tirado:
                print('=-'*10)
                print("Você tirou: ", lancamento2, "\nVocê tirou o mesmo número novamente. você GANHOU")
            # se não joga novamente
            else:
                print('=-'*10)
                print("Você tirou:", lancamento2, "\nJogando novamente em 2 segundos...")
                print('=-'*17)
                sleep(2)

                
lancamento = lancamento_dados()
verificar_resultado(lancamento)