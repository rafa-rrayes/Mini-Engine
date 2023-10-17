from PosModsim import *
import time

sim = Simulation(600, 600, "Titulo", "dark green",0.001, True)

for i in range(20):
    ball = Object(20, 20, [np.random.randint(0, 600), np.random.randint(0, 600)], 2,[0,0], "yellow", sim, circle=True)
    ball.addGravity()
start = time.time()
sim.calculate(15, 0.001, method='verlet')
print(time.time()-start)
sim.run(3)