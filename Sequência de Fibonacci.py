# Imprime uma linha de separação com 30 sinais de igual
print("=" * 30)

# Solicita ao usuário a quantidade de termos da sequência de Fibonacci
n = int(input("-- Sequência de Fibonacci --\n"))

# Inicializa os dois primeiros termos da sequência
t1 = 0
t2 = 1

# Imprime outra linha de separação
print("=" * 30)

# Imprime os dois primeiros termos da sequência no formato "0-1"
print(f"{t1}-{t2}", end='')

# Inicializa o contador a partir do terceiro termo
cont = 3

# Loop para calcular e imprimir os termos seguintes até o número informado
while cont <= n:
    t3 = t1 + t2  # Calcula o próximo termo da sequência
    print(f"-{t3}", end='')  # Imprime o próximo termo precedido de "-"
    t1 = t2  # Atualiza o primeiro termo para o próximo cálculo
    t2 = t3  # Atualiza o segundo termo para o próximo cálculo
    cont += 1  # Incrementa o contador

# Imprime a palavra "Fim" indicando o término da sequência
print("- Fim")

# Imprime uma linha de separação com 30 asteriscos
print("*" * 30)
