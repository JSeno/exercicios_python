"""
Questão
- Crie um programa que peça ao usuário para digitar seu nome e sua idade. Imprima uma mensagem endereçada a 
eles informando o ano em que completarão 100 anos. 

- Observação: para este exercício, a expectativa é que você escreva explicitamente o ano.

"""

from datetime import datetime


nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

ano = datetime.now().year

print(f"Olá {nome}, você completará 100 anos em {ano + 100 - idade}")
