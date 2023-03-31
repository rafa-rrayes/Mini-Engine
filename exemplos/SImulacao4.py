from Miniengine import *

screen = Simulation(1000, 1000, "Simulation", collisions=True, dt=0.001, steps=60000, speed=1)
sun = Object(50, 50, (500, 500), 40, 0, 0, "yellow", screen, circle=True)

earth = Object(20, 20, (500, 800), 10, 160, 180, "blue", screen, hitBorder=False, circle=True)
mars = Object(20, 20, (500, 200), 10, 160, 0, "red", screen, hitBorder=False, circle=True)

sun.addGravity(9.8, lock=True)
sun.lockPos()
mars.addGravity(9.8)

screen.add_object(mars)
earth.addGravity(9.8)
screen.add_object(sun)
screen.add_object(earth)
screen.calculate()
screen.run()
