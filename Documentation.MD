# MiniEngine

MiniEngine is a simple physics engine for simulating and rendering 2D objects. It includes the `Tela` class for creating a display window and the `Objeto` class for defining objects. The `Renderer` class is responsible for running the simulation and rendering the objects.

## Tela Class

The `Tela` class represents the display window for the simulation. The constructor takes the following parameters:

### Parameters

* `width` (int): Width of the display window in pixels.
* `height` (int): Height of the display window in pixels.
* `title` (str): Title of the display window.

### Methods

* `add_object(obj)`: Adds an instance of `Objeto` to the display window.

## Objeto Class

The `Objeto` class represents a 2D object in the simulation. The constructor takes the following parameters:

### Parameters

* `width` (int): Width of the object in pixels.
* `height` (int): Height of the object in pixels.
* `pos` (tuple): Initial position of the object as an (x, y) tuple.
* `mass` (float): Mass of the object.
* `vel` (tuple): Initial velocity of the object as an (x, y) tuple.
* `angle` (float): Initial angle of the object in degrees.
* `color` (str): Color of the object.
* `tela` (Tela): Instance of the Tela class.

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
