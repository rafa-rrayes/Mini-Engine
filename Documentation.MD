# MiniEngine 1.0.1

MiniEngine is a simple physics engine for simulating and rendering 2D objects.

## Tela Class

The `Simulation` class represents the display window for the simulation. The constructor takes the following parameters:

### Parameters

* `width` (int): Width of the display window in pixels.
* `height` (int): Height of the display window in pixels.
* `title` (str): Title of the display window.
* `color` (str or tupple): color of the background


### Methods

* `calculate(lenght, dt)`: calculates the entire simulation based on the initial coditions of the objects
* `run(speed)`: Plays the simulation. You need to calculate the simulation first.

## Object Class

The `Object` class represents a 2D object in the simulation. The constructor takes the following parameters:

### Parameters

* `width` (int): Width of the object in pixels.
* `height` (int): Height of the object in pixels.
* `position` (tuple): Current position of the object as an (x, y) tuple.
* `mass` (float): Mass of the object.
* `speed` (tuple): Initial velocity of the object as an (x, y) tuple.
* `direction` (float): Current direction of the object in degrees.
* `color` (tuple): Color of the object.
* `simulation` (Simulation): Which simulation the object belongs to.
* `circle`(Bool): Wether the object is a circle or not. If not defined, it's a square.
* `COR`(float): Coeficient of restituition of the object. If not defined, it's 1
* `colisionLayer`(int): Objects in the same colision layer will colide. if not defined, it's 0
* `hitBorder`(Bool): wheter the object colides with the border or not. If not defined, it's False
 
### Methods

* `updatePosition(dt)`: Updates the object's position in dt time. 
* `addGravity(g)`: Adds gravity to the object.
* `addAcceleration(dV, angle)`: Adds acceleration to the object.
* `lockPos()`: Locks the object in place.
* `onScreen()`: Returns True if at least a part of the object is on screen
* `accelerate(dt)`: increments the speed of the object using its dV in dt time.


### Other Functions

* `Collide(object1, object2)`: Handles the collision between the two objects
* `distance(object1, object2)`: returns the distance between the two objects
* `calculate_gravity(objects, dt)`: Takes a list of objects and handles the effect of gravity on each object and updates its speed and direction.
* `Collide(object1, object2)`: Handles the collision between the two object
* `border(object)`: Checks if object is hitting the border, and if so handles the colision.
* `checkCollision(object1, object2)`: Checks if the two objects are colliding

## Example

A small simulation of a snooker game
```
from Miniengine import *


sim = Simulation(400, 800, "Title", "dark green", True)


ball = Object(20, 20, (200, 200), 1, 0, 0, "yellow", sim, hitBorder=True, circle=True, COR = 0.9)
ball2 = Object(20, 20, (215, 185), 2, 0, 0, "red", sim, hitBorder=True, circle=True, COR = 0.9)
ball3 = Object(20, 20, (185, 185), 2, 0, 0, "green", sim, hitBorder=True, circle=True, COR = 0.9) 
ball4 = Object(20, 20, (200, 170), 2, 0, 0, "blue", sim, hitBorder=True, circle=True, COR = 0.9)
ball5= Object(20, 20, (230, 170), 2, 0, 0, "black", sim, hitBorder=True, circle=True, COR = 0.9)
ball6 = Object(20, 20, (170, 170), 2, 0, 0, "orange", sim, hitBorder=True, circle=True, COR = 0.9)
ball7 = Object(20, 20, (200, 600), 4, 200,  270, "white", sim, hitBorder=True, circle=True, COR = 0.9)

sim.calculate(20, 0.001)
sim.run(speed=2)
