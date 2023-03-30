import pygame
import MiniEngine

tela = MiniEngine.Window(800, 800, "Simulação")
terra = MiniEngine.Object(20, 20, (400, 600), 30, 40, -180, (0,0,255), tela)
sol = MiniEngine.Object(50, 50, (400, 400), 20, 0, 0, (255, 255, 0), tela)
asteroide = MiniEngine.Object(10, 10, (-770, -770), 20, 40, 45, "grey", tela)

Jogando = True
clock = pygame.time.Clock()
tick = 60
dt = dt = (1/tick)*4
while Jogando:
    tela.window.fill((0,0,0))
    terra.gravitate(sol,True, dt, g=10)
    terra.updatePosition(dt)
    sol.updatePosition(dt)
    tela.draw(sol)
    tela.draw(terra)
    asteroide.updatePosition(dt)
    tela.draw(asteroide)
    clock.tick(tick)
    if terra.checkColision(asteroide):
        MiniEngine.Colide(asteroide, terra, COR=1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Jogando = False
    pygame.display.update()
