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

def jogar():
    print('Escolha um número de 1 à 50.')
    numero_chutado = int(input('Digite seu número: '))
    numero_aleatorio = random.randint(1, 2)
    if  numero_chutado == numero_aleatorio:
        print('+----------------------------------+')
        print('|\(*.*)/   Você acertou!    \(*.*)/|')
        print('+----------------------------------+')

    elif numero_chutado != numero_aleatorio:
        print('+---------------------------------------------------------------+')
        print(f'Que pena! Você errou o número era {numero_aleatorio} e você chutou {numero_chutado}')
        print('+---------------------------------------------------------------+')
        print('\nGostaria de tentar novamente? Digite Sim ou Não.')
        aceitar_jogar = input('Digite sua escolha: ')
        if aceitar_jogar == 'Sim' or aceitar_jogar == 'sim' or aceitar_jogar == 'S' or aceitar_jogar == 's':
            jogar()
        elif aceitar_jogar == 'Não' or aceitar_jogar == 'não' or aceitar_jogar == 'N' or aceitar_jogar == 'n':
            print('Obrigado por jogar!')
        else:
            print('Opção inválida!')


while aceitar_jogar == 'Sim' or aceitar_jogar == 'sim' or aceitar_jogar == 'S' or aceitar_jogar == 's':
    if aceitar_jogar == 'sim' or aceitar_jogar == 'Sim' or aceitar_jogar == 's' or aceitar_jogar == 'S':
        print('OK! Vamos começar!')
        jogar()
        print('Você quer jogar novamente? Digite. S/N')
        aceitar_jogar = input('Digite sua escolha: ')
        if aceitar_jogar == 'sim' or aceitar_jogar == 'Sim' or aceitar_jogar == 's' or aceitar_jogar == 'S':
            jogar()
        else:
            print('Tchau!')

    elif aceitar_jogar == 'não' or aceitar_jogar == 'Não' or aceitar_jogar == 'n' or aceitar_jogar == 'N':
        print('Tudo bem, até mais!')
        break
    else:
        print('Opção inválida!')
        break

