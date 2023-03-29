This program is a 2D physics simulation, that provides functionalities to create, visualize, and manipulate objects on a screen using the Pygame library. The simulation is capable of handling gravity, object collisions, and various other properties related to the motion of the objects. It is important to note that this is still the first version of the program. As such, the precision and accuracy of the simulations might not be at very precise, especially in small scales.

Creating a simulation window: The Tela class creates a simulation window with specified dimensions and title. The window is displayed using Pygame.
```
import pygame
import MiniEngine

tela = MiniEngine.Tela(800, 800, "Simulação")
```

Creating and displaying objects: The Objeto class creates and display objects with specified dimensions, position, mass, velocity, direction and color.

```
terra = MiniEngine.Objeto(20, 20, (400, 600), 30, 40, -180, "verde", tela)
sol = MiniEngine.Objeto(50, 50, (400, 400), 20, 0, 0, "amarelo", tela)
asteroide = MiniEngine.Objeto(10, 10, (-770, -770), 20, 40, 45, "cinza", tela)
``` 
gravitar(): This function calculates gravitational force between two objects and updates their velocities accordingly. It takes three arguments: the other object, the time interval dt, and the gravitational constant g.
```
terra.gravitar(sol, dt, g=10)
```

atualizarPos(): This function updates the position of an object based on its current velocity and the time interval dt. If gravidade is set to True, it updates the position considering the force of gravity.
Example 1 (without gravity):

```
terra.atualizarPos(dt, gravidade=True)
```
gravidade = True means it will take the downwards aceleration due to gravity when calculating the positions

desenhar(): This function draws the object on the simulation window.
```
tela.desenhar(sol)
```

ChecarColidir(): This function checks if two objects have collided. It takes the other object as an argument and returns True if the objects have collided, False otherwise.

```
if terra.ChecarColidir(asteroide):
```
Colide(): This function handles the collision between two objects. It takes two objects and an optional COR argument, which represents the coefficient of restitution. By default, it is set to 1 (perfectly elastic collision).
Example:

```
if terra.ChecarColidir(asteroide):
  MiniEngine.Colide(asteroide, terra, COR=1)
```
