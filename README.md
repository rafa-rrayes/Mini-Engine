# PyPhysicsSim

Miniengine is a simple physics simulation library built on top of Pygame. It allows users to simulate the motion of objects, calculate collisions, and visualize the results. The library includes two main components: the `MiniEngine` module for handling physics calculations, and the `Renderer` class for rendering and displaying the simulations.

## Installation

To install PyPhysicsSim, simply clone this GitHub repository to your local machine.

## Dependencies

- Pygame

## Usage

### MiniEngine Module

The `MiniEngine` module provides the following classes and functions:

#### Window

`Window` class represents the simulation window. It has the following attributes:

- width: The width of the simulation window
- height: The height of the simulation window
- title: The title of the simulation window

#### Object

`Object` class represents a physical object in the simulation. It has the following attributes:

- height: The height of the object
- width: The width of the object
- position: The initial position of the object
- mass: The mass of the object
- speed: The initial speed of the object
- direction: The initial direction of the object in degrees
- color: The color of the object
- window: The simulation window the object belongs to

#### Colide

`Colide` function handles the collision between two objects.

### Renderer Class

`Renderer` class is used to visualize the simulation. It has the following attributes:

- window: The simulation window
- objects: The list of objects in the simulation
- dt: The time interval between each frame of the simulation
- length: The total duration of the simulation
- speed: The speed factor of the simulation
- gravity: If True, enables gravity in the simulation

The `Renderer` class provides the following methods:

- `bake`: Calculates the positions of objects at each frame
- `store_positions`: Stores the positions of objects at each frame

### Example

```python
from MiniEngine import Window, Object, Colide
from Renderer import Renderer, run

# Create window and objects
window = Window(800, 800, "Simulação")
object1 = Object(20, 20, (100, 100), 1, 50, 30, (255, 0, 0), window)
object2 = Object(20, 20, (300, 300), 1, 50, 200, (0, 255, 0), window)

# Create renderer
renderer = Renderer(window, [object1, object2], dt=1/60, length=10, speed=1, gravity=False)

# Calculate object positions
renderer.bake()

# Run the simulation
run(renderer)
