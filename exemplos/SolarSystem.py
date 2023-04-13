from Miniengine import *

screen = Simulation(1000, 1000, "Simulation", "black", collisions=True)
sun = Object(50, 50, (500, 500), 40, 0, 0, "yellow", screen, circle=True)
venus = Object(20, 20, (500, 200), 10, 200, 0, "orange", screen, hitBorder=False, circle=True)
earth = Object(20, 20, (500, 900), 10, 160, 180, "green", screen, hitBorder=False, circle=True)
mercury = Object(10, 10, (500, 600), 10, -250, 0, "red", screen, hitBorder=False, circle=True)

sun.addGravity(98)
sun.lockPos()
venus.addGravity(98)
mercury.addGravity(98)
earth.addGravity(98)
screen.calculate(20, 0.001)
screen.run()
