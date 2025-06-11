from random import randint

# Imprime uma linha decorativa para iniciar o sorteio
print('==' * 12)
print(f"        {'Sorteio'}")
print('==' * 12)

# Gera um número aleatório entre 1 e 10 (número da sorte)
numero = randint(1, 10)

# Inicializa a variável resposta com um valor que não corresponde ao número sorteado
resposta = 11  

# Inicializa o contador de tentativas
tentativas = 0

# Loop continua enquanto o número digitado pelo usuário for diferente do número sorteado
while numero != resposta:
    # Solicita que o usuário digite seu palpite para o número da sorte
    resposta = int(input("Digite seu Número da Sorte (entre 1 e 10): "))
    
    # Incrementa o número de tentativas (corrigido para somar +1)
    tentativas += 1  

# Quando o usuário acertar, imprime a quantidade de tentativas e o número sorteado
print(f"Tentativas: {tentativas} \nNúmero Sorte
