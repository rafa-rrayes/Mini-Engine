import pygame
import MiniEngine



tela = MiniEngine.Tela(800, 800, "Simulação", tick=60, speed=1)
terra = MiniEngine.Objeto(20, 20, (400, 400), 3, 0, 0, "verde", tela)
sol = MiniEngine.Objeto(50, 50, (400, 500), 20, 20, -90, "amarelo", tela)
Jogando = True
clock = pygame.time.Clock()
tick = 60
dt = 1/tick
while Jogando:
    tela.tela.fill((0,0,0))
    sol.atualizarPos(dt)
    terra.atualizarPos(dt, gravidade=True)
    tela.desenhar(sol)
    tela.desenhar(terra)
    clock.tick(tick)
    if terra.ChecarColidir(sol):
        MiniEngine.Colide(sol, terra, COR=1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Jogando = False
    pygame.display.update()