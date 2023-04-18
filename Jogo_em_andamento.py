from random import randint
import random

import pygame

pygame.init()

janela = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Criando jogo")

x = 300      # 540 max
y = 300
pos_x = 210
pos_y = 800
pos_y_a = 300
pos_y_s = 300
pos_y_v = 300
pos_y_p = 300
time = 0
tempo_segundo = 0

velocidade = 5
velocidade_outros = 5

fundo = pygame.image.load("pista.png.png")
carro = pygame.image.load("carro.png")
policia = pygame.image.load("policia.png")
suv = pygame.image.load("suv.png")
vermelho = pygame.image.load("vermelho.png")
ambulancia = pygame.image.load("ambulancia.png")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x <= 530:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 220:
        x -= velocidade

    if (x + 80 > pos_x and y + 180 > pos_y):
        y = 1200

    if (x - 80 > pos_x and y + 180 > pos_y):
        y = 1200

        y = 400

    if (pos_y <= -80):
        pos_y = randint(700, 1000)

    if (pos_y_p <= -80):
        pos_y_p = randint(900, 2000)

    if (pos_y_v <= -80):
        pos_y_v = randint(1000, 3000)

    if (pos_y_s <= -80):
        pos_y_s = randint(1200, 3200)

    if (pos_y_a <= -80):
        pos_y_a = randint(1600, 3800)

    if (time < 20):
        time += 1

    else:
        tempo_segundo += 1
        text = font.render("Tempo : " + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        time = 0

    pos_y -= velocidade_outros
    pos_y_s -= velocidade_outros + 5
    pos_y_v -= velocidade_outros + 3
    pos_y_p -= velocidade_outros - 1
    pos_y_a -= velocidade_outros + 6

    font = pygame.font.SysFont("arial black", 30)
    text = font.render("  Tempo: " + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
    pos_text = text.get_rect()
    pos_text.center = (65, 50)

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
