# MiniEngine

MiniEngine is a simple physics engine for simulating and rendering 2D objects. It includes the `Window` class for creating a display window and the `Object` class for defining objects. The `Renderer` class is responsible for running the simulation and rendering the objects.

## Tela Class

The `Window` class represents the display window for the simulation. The constructor takes the following parameters:

### Parameters

* `width` (int): Width of the display window in pixels.
* `height` (int): Height of the display window in pixels.
* `title` (str): Title of the display window.

### Methods

* `add_object(object)`: Adds an instance of `Objeto` to the display window.
* `draw(object)`: Draws the object in its current position

## Objeto Class

The `Object` class represents a 2D object in the simulation. The constructor takes the following parameters:

### Parameters

* `width` (int): Width of the object in pixels.
* `height` (int): Height of the object in pixels.
* `position` (tuple): Current position of the object as an (x, y) tuple.
* `mass` (float): Mass of the object.
* `speed` (tuple): Initial velocity of the object as an (x, y) tuple.
* `direction` (float): Current direction of the object in degrees.
* `color` (tuple): Color of the object.
* `window` (Window): Instance of the Window class.
* `gravity`(Bool): Wether the object is affected by downwards gravity
 
### Methods

* `updatePosition(dt, gravity)`: Updates the object's position in dt time. 
* `checkColision(object)`: Checks if the object has colided with another object
* `border()`: Reverses object direction if it hits the screen border
* `accelerate(dV, angle)`: Accelerates the object. dV is the speed increment, angle is the direction it is accelerating
* `gravitate(object)` (tuple): Initial velocity of the object as an (x, y) tuple.

## Renderer Class

The `Renderer` class is responsible for running the simulation and rendering the objects. The constructor takes the following parameters:

### Parameters

* `tela` (Tela): Instance of the Tela class.
* `objetos` (list): List of Objeto instances to be rendered in the simulation.
* `dt` (float, optional): Time interval between updates in the simulation. Default is 1/60.
* `length` (int, optional): Length of time the simulation runs in seconds. Default is 2.
* `speed` (float, optional): Speed factor of the simulation. Default is 1.
* `gravity` (bool, optional): If True, gravitational forces between objects are considered. Default is False.

### Methods

* `render(simulation_name)`: Runs the simulation and saves each frame as an image with the given `simulation_name`. The images will be saved in a folder named "renders".
* `store_positions()`: Stores the positions of objects at each time step in a dictionary.
* `get_positions()`: Returns the stored positions of objects as a dictionary.

## Example

A small simulation of a tenis ball and a basketball 
```
import pygame
import Miniengine 

# creating our screen and the objects
screen = Miniengine.Window(800, 800, "Simulation")
basketball = Miniengine.Object(40, 40, (400, 600), 10, 80, -91, "orange", screen, gravity=True)
tennisball = Miniengine.Object(20, 20, (400, 400), 1, 0, 0, "yellow", screen, gravity=True)


# making the main game loop
playing = True
dt = 1/60*2  #interval between calculations
clock= pygame.time.Clock() # set fps
while playing:
    screen.window.fill((0,0,0))  # hide previous frame
    if basketball.checkColision(tennisball): # check if the balls colide
        Miniengine.Colide(basketball, tennisball) # handling the colision
    
    # make the balls stay in the screen
    basketball.border() 
    tennisball.border()
    #update the positions
    basketball.updatePosition(dt)
    tennisball.updatePosition(dt)
    #draw them on the screen
    screen.draw(tennisball)
    screen.draw(basketball)

    
    clock.tick(60)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing= False```



