"""
Adivinhe o número
Você deve chutar um número de 1 à 50 e será um número aleatório.
Caso você acerte, você ganha.
TDOO: após consertar a lógica do jogo transformar em um jogo de dados serão lançados 3 dados e você terá que apostar
qual número deve ser o resultado.
"""
import random

print('Vamos jogar um jogo de adivinhação!')
print('Você deve chutar um número de 1 à 50 e será um número aleatório.')
print('Caso você acerte, você ganha.')
print('Vamos começar!')

print('Se você quiser jogar digite Sim, caso contrário digite Não.')
aceitar_jogar = input('Digite sua escolha: ')

if aceitar_jogar == 'sim' or aceitar_jogar == 'Sim' or aceitar_jogar == 's' or aceitar_jogar == 'S':
    print('OK! Vamos começar!')
    print('Escolha um número de 1 à 50.')
    numero_chutado = int(input('Digite seu número: '))
    numero_aleatorio = random.randint(1, 2)

    if numero_chutado == numero_aleatorio:
        print('Parabéns! Você acertou!')

    else:
        print('Que pena! Você errou!')
        print('O número era {} e você digitou {}.'.format(numero_aleatorio, numero_chutado))

else:
    print('Tudo bem! Até a próxima!')
