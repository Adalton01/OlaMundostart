from random import *

print('==' * 12)
print(f"        {'Sorteio'}")
print('==' * 12)

numero = randint(1, 10)
resposta = 11
tentativas = 0
while numero != resposta:
    resposta = int(input("Digite seu Numero da Sorte "))
    tentativas = tentativas + +1
print(f"Tentativas {tentativas} \nNumero Sorteado {numero}"), print("**" * 10)
