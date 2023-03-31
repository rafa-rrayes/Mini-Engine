from Miniengine import *
#setup a simulation
sim = Simulation(400, 800, "Simulation", True, 0.001, 60000, 2)

#add objects
ball = Object(20, 20, (200, 200), 2, 0, 0, "yellow", sim, hitBorder=True, circle=True, collisionLayer=0)
ball2 = Object(20, 20, (215, 185), 2, 0, 0, "red", sim, hitBorder=True, circle=True)
ball3 = Object(20, 20, (185, 185), 2, 0, 0, "green", sim, hitBorder=True, circle=True)
ball4 = Object(20, 20, (200, 170), 2, 0, 0, "blue", sim, hitBorder=True, circle=True)
ball5= Object(20, 20, (230, 170), 2, 0, 0, "black", sim, hitBorder=True, circle=True)
ball6 = Object(20, 20, (170, 170), 2, 0, 0, "orange", sim, hitBorder=True, circle=True)
ball7 = Object(20, 20, (200, 600), 3, 200, -90, "white", sim, hitBorder=True, circle=True, collisionLayer=0)


sim.add_object(ball)
sim.add_object(ball2)
sim.add_object(ball3)
sim.add_object(ball4)
sim.add_object(ball5)
sim.add_object(ball6)
sim.add_object(ball7)

#calculate with initial conditions
sim.calculate()
sim.run()
