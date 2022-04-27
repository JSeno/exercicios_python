# TODO: Criar função para receber respota de continuar ou não jogando e colocar o jogo em loop.

"""
Adivinhe o número
Você deve chutar um número de 1 à 10 e será um número aleatório.
Caso você acerte, você ganha.
"""
import random


print('Vamos Jogar Advinhe o Número?')
print('Se sim digite S e se não digite N')
aceitar_jogar = input()
if aceitar_jogar == 'N' or 'n':
    print('Obrigado por jogar')
elif aceitar_jogar == 'S' or 's':
    print('Vamos jogar então!')
    num1 = int(input("Digite um número de 1 a 10: "))
    num2 = random.randint(1, 10)
    if num1 == num2:
        print('Parabéns você acertou o número')
    else:
        print(f'Você errou o número era {num2} e você digitou {num1}, tente novamente')
else:
    print('Você digitou um valor inválido, tente novamente')





        
