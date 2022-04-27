"""
Adivinhe o número
Você deve chutar um número de 1 à 10 e será um número aleatório.
Caso você acerte, você ganha.
"""
import random


print('Vamos Jogar Advinhe o Número?')
print('Se sim digite S e se não digite N')
aceitar_jogar = input()
if aceitar_jogar == 'N' or aceitar_jogar == 'n':
    print('Obrigado por jogar')
elif aceitar_jogar == 'S' or aceitar_jogar == 's':
    flag = True
    while flag:
        print('Vamos jogar então!')
        num2 = random.randint(1, 10)
        num1 = int(input("Digite um número de 1 a 10: "))
        while num1 != num2:
            if num1 == 'P':
                break
            print(f'Você digitou {num1} e o número era {num2} /(T_T)/ ')
            num1 = int(input("Digite um número de 1 a 10,\nPara desistir digite P: "))
            print(end="\n")
            num2 = random.randint(1, 10)
        if num1 == num2:
            print('+--------------------------------------------+')
            print('\(^_^)/ Parabéns você acertou o número \(^_^)/')
            print('+--------------------------------------------+')
            cont = input('Deseja jogar novamente? S/N ')

            if cont == 'N' or cont == 'n':
                flag = False
        else:
            print('Game Over')
            flag = False
else:
    print('Você digitou um valor inválido, tente novamente')





        
