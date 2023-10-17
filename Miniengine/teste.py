from PosModsim import *


sim = Simulation(400, 800, "Titulo", "dark green",0.001, True)


ball = Object(20, 20, [200, 200], 2,[0, 0], "yellow", sim, circle=True)
# ball2 = Object(20, 20, [215, 185], 2,[0, 0], "red", sim, circle=True)
# ball3 = Object(20, 20, [185, 185], 2,[0, 0], "green", sim, circle=True) 
# ball4 = Object(20, 20, [200, 170], 2,[0, 0], "blue", sim, circle=True)
# ball5= Object(20, 20, [230, 170], 2,[0, 0], "black", sim, circle=True)
# ball6 = Object(20, 20, [170, 170], 2,[0, 0], "orange", sim, circle=True)
ball7 = Object(20, 20, [200, 600], 2,[0, 200], "white", sim, circle=True, COR=0.5)
ball.frictionCoeficient = 0.2
# ball2.frictionCoeficient = 0.2
# ball3.frictionCoeficient = 0.2
# ball4.frictionCoeficient = 0.2
# ball5.frictionCoeficient = 0.2
# ball6.frictionCoeficient = 0.2
ball7.frictionCoeficient = 0.2
sim.calculate(10, 0.001, method='verlet')
sim.run(speed=2)
