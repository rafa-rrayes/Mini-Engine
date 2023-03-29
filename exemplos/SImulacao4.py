import pygame
import MiniEngine

tela = MiniEngine.Tela(800, 800, "Simulação")

terra = MiniEngine.Objeto(20, 20, (400, 600), 30, 40, -180, "verde", tela)
sol = MiniEngine.Objeto(50, 50, (400, 400), 20, 0, 0, "amarelo", tela)
asteroide = MiniEngine.Objeto(10, 10, (-770, -770), 20, 40, 45, "cinza", tela)


clock = pygame.time.Clock()
tick = 60    # The tick defines how many time the the simulation is update 1 one second
dt = (1/tick)*4    #multiply the dt to increase the simulation speed
Jogando = True
while Jogando:
    tela.tela.fill((0,0,0))
    terra.atualizarPos(dt)
    tela.desenhar(sol)
    tela.desenhar(terra)
    asteroide.atualizarPos(dt)
    tela.desenhar(asteroide)
    clock.tick(tick)
    if terra.ChecarColidir(asteroide):
        MiniEngine.Colide(asteroide, terra, COR=1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Jogando = False
    pygame.display.update()
