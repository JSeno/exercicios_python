"""
Questão
Peça ao usuário um número. Dependendo se o número é par ou ímpar, imprima uma mensagem apropriada para o usuário.

"""

num = int(input("Digite um número: "))
if num % 2 ==0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")

