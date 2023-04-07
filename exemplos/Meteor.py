import Miniengine

tela = Miniengine.Simulation(800, 800, "Simulação","black", True)

terra = Miniengine.Object(20, 20, (400, 600), 10, 150, -180, "blue", tela,  circle=True)
sol = Miniengine.Object(50, 50, (400, 400), 400, 0, 0, "yellow", tela,  circle=True)
asteroide = Miniengine.Object(10, 10, (-3500, 600), 1, 190, 0, "grey", tela, circle=True)

sol.addGravity(10)
terra.addGravity(10)
tela.calculate(80, 0.001)
tela.run(speed=3)
