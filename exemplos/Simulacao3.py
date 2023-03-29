import MiniEngine
import pygame
import random
clock = pygame.time.Clock()

Quantidade_de_bolas = 10
tamanho = 10
tela = MiniEngine.Tela(1000, 1000, "Simulação", tick=60, speed=1)
listaBolas = []
for i in range(10):
    bola = MiniEngine.Objeto(tamanho, tamanho, (200, 1000/Quantidade_de_bolas*i), 20, random.randint(20,60), random.randint(1,360), "cinza", tela)
    listaBolas.append(bola)

Jogando = True
clock = pygame.time.Clock()
tick =1000        # The tick defines how many time the the simulation is update 1 one second
dt = (1/tick)*6    #multiply the dt to increase the simulation speed
while Jogando:
    tela.tela.fill((0,0,0))
    for i in listaBolas:
        i.atualizarPos(dt)
        tela.desenhar(i)
        tela.desenhar(boli)
        for j in listaBolas:
            if i.ChecarColidir(j):
                MiniEngine.Colide(i, j, COR=1)
        i.Borda()
    clock.tick(tick)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Jogando = False
    pygame.display.update()