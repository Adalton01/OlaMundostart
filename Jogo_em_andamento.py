from random import randint
import pygame

pygame.init()

# Janela
janela = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Criando jogo")

# Posições do carro do jogador
x = 300
y = 300

# Posições iniciais dos carros adversários
pos_x = 210
pos_y = 800
pos_y_a = 300
pos_y_s = 300
pos_y_v = 300
pos_y_p = 300

# Velocidade dos carros
velocidade = 5
velocidade_outros = 5

# Contador de tempo
time = 0
tempo_segundo = 0

# Carregamento de imagens
fundo = pygame.image.load("pista.png.png")
carro = pygame.image.load("carro.png")
policia = pygame.image.load("policia.png")
suv = pygame.image.load("suv.png")
vermelho = pygame.image.load("vermelho.png")
ambulancia = pygame.image.load("ambulancia.png")

# Fonte
font = pygame.font.SysFont("arial black", 30)

janela_aberta = True
while janela_aberta:
    pygame.time.delay(10)

    # Eventos (fechar janela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # Movimento do jogador
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and x <= 530:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 220:
        x -= velocidade

    # Colisão simples
    if (x + 50 > pos_x and x < pos_x + 50) and (y < pos_y + 180 and y + 180 > pos_y):
        print("Colisão!")
        y = 1200  # Joga o carro pra fora da tela (poderia ser fim de jogo)

    # Reset de carros adversários quando saem da tela
    if pos_y <= -80:
        pos_y = randint(700, 1000)
    if pos_y_p <= -80:
        pos_y_p = randint(900, 2000)
    if pos_y_v <= -80:
        pos_y_v = randint(1000, 3000)
    if pos_y_s <= -80:
        pos_y_s = randint(1200, 3200)
    if pos_y_a <= -80:
        pos_y_a = randint(1600, 3800)

    # Contagem de tempo
    if time < 20:
        time += 1
    else:
        tempo_segundo += 1
        time = 0

    # Movimento dos carros adversários
    pos_y -= velocidade_outros
    pos_y_s -= velocidade_outros + 5
    pos_y_v -= velocidade_outros + 3
    pos_y_p -= velocidade_outros - 1
    pos_y_a -= velocidade_outros + 6

    # Renderização de texto do tempo
    text = font.render("Tempo: " + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
    pos_text = text.get_rect(center=(100, 50))

    # Atualização da tela
    janela.fill("green")
    janela.blit(fundo, (200, -120))
    janela.blit(carro, (x, y))
    janela.blit(suv, (pos_x + 290, pos_y_s))
    janela.blit(vermelho, (pos_x + 210, pos_y_v))
    janela.blit(ambulancia, (pos_x + 10, pos_y_a))
    janela.blit(policia, (pos_x, pos_y + pos_y_p))
    janela.blit(text, pos_text)

    pygame.display.update()

pygame.quit()
