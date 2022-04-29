"""
Adivinhe o número
Você deve chutar um número de 1 à 50 e será um número aleatório.
Caso você acerte, você ganha.
TDOO: após consertar a lógica do jogo transformar em um jogo de dados serão lançados 3 dados e você terá que apostar
qual número deve ser o resultado.
"""
import random


def aceitar_jogar():
    if aceitar_jogar == 's' or aceitar_jogar == 'S':
        return True
    elif aceitar_jogar == 'n' or aceitar_jogar == 'N' or aceitar_jogar == 'p' or aceitar_jogar == 'P':
        return False
    else:
        print('\nVocê digitou um valor inválido.\n')
        return aceitar_jogar()


def jogar():
    print('\nVocê deve chutar um número de 1 à 10 e será um número aleatório.\n')
    print('Caso você acerte, você ganha.\n')
    print('Para sair, digite "N".\n')

    print('\nDigite um número de 1 à 10')
    numero_chutado_usuario = input()
    numero_chutado = random.randint(1, 10)
    if numero_chutado_usuario == numero_chutado:
        print('\nParabéns, você acertou!')
    elif numero_chutado_usuario != numero_chutado:
        print('\nVocê errou!')
        print(f'O número era {numero_chutado} e você chutou {numero_chutado_usuario}.')
jogar()



        
