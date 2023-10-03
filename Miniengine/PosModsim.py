import pygame
import numpy as np
from scipy.integrate import odeint
class Simulation():
    def __init__(self, width, height, tittle, color, collisions = False):
        self.width = width
        self.height = height
        self.tittle = tittle
        self.color = color
        self.objects = []
        self.positions_history = []
        self.collisions = collisions
        self.gravity_objects = []
    def add_object(self, object):
        self.objects.append(object)
        if object.gravity:
            self.gravity_objects.append(object)
    def run(self, speed=1, fps=60, frames='all'):
        if frames == 'all': frames = len(self.positions_history)
        listaIndex = np.linspace(0, len(self.positions_history)-1, round(self.lenght*fps/speed), dtype=int)
        display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.tittle)
        clock = pygame.time.Clock()
        x = 0
        positions = [self.positions_history[i] for i in listaIndex]
        for objects in positions:
            display.fill(self.color)
            for object in objects:
                display.blit(object[0].body, object[1] - np.array([object[0].width/2, object[0].height/2]))
            pygame.display.update()
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    def calculate(self, lenght, dt, method='euler'):
        self.lenght = lenght
        self.dt = dt
        self.steps = round(lenght/dt)
        if method == 'euler':
            for q in range(self.steps):
                positions = []
                if self.collisions: 
                    for i in range(len(self.objects)):
                        object1 = self.objects[i]
                        for j in range(i + 1, len(self.objects)):
                            object2 = self.objects[j]
                            if object1.collisionLayer == object2.collisionLayer:
                                if checkCollision(object1, object2):
                                    Collide(object1, object2, dt)
                calculate_gravity(self.gravity_objects, dt)
                for object in self.objects:
                    object.calculate(dt)
                    positions.append([object, object.position])
                self.positions_history.append(positions)
        elif method == 'odeint':
            initial_states = [obj.position.tolist() + obj.speed.tolist() for obj in self.objects]
            initial_states = np.array(initial_states).flatten()
            t = np.linspace(0, lenght, self.steps)
            result = odeint(self.system_derivative, initial_states, t)
            self.extract_positions_from_result(result)
    
    def system_derivative(self, y, t):
        n = len(self.objects)
        derivatives = []
        
        # Reset forces
        for obj in self.objects:
            obj.force = np.array([0, 0], dtype=np.float64).flatten()        
        # Calculate gravity forces
        calculate_gravity(self.gravity_objects, self.dt)

        
        for i in range(n):
            pos = y[4*i : 4*i+2]
            speed = y[4*i+2 : 4*i+4]
            obj = self.objects[i]
            
            acc = obj.force / obj.mass
            
            derivatives += [speed[0], speed[1], acc[0], acc[1]]
        
        return derivatives
    
    def extract_positions_from_result(self, result):
        for state in result:
            positions = []
            for i, obj in enumerate(self.objects):
                pos = state[4*i : 4*i+2]
                obj.position = pos
                positions.append([obj, obj.position])
            self.positions_history.append(positions)
class Object(pygame.Surface):
    def __init__(self, width, height, position, mass, speed, color, simulation,circle=False, COR = 1, collisionLayer=0):
        self.height = height
        self.width = width
        self.gravity = False
        self.position = np.array([position], dtype=np.float64).flatten()
        self.x , self.y = position
        self.circle = circle
        self.mass = mass
        self.speed = np.array(speed, dtype=np.float64).flatten()
        self.force = np.array([0,0], dtype=np.float64).flatten()
        if color == "black" or color == (0,0,0):
            color = (0,0,1)
        self.color = color
        self.collisionLayer = collisionLayer
        self.simulation = simulation
        self.COR = COR
        self.body = pygame.Surface((self.width, self.height))
        if circle:
            self.body.set_colorkey((0, 0, 0))  
            pygame.draw.circle(self.body, (color), (self.width/2, self.height/2), self.width/2)
        else:
            self.body.fill(color)
        simulation.add_object(self)
        self.locked = False
    def lockPos(self):
        self.locked = True
    def addGravity(self, g=0):
        self.gravity = True
        self.g = g
        self.simulation.gravity_objects.append(self)
    def addForce(self, force):
        self.force += force
    def onScreen(self):
        if self.position[0] > self.simulation.width+self.width or self.position[0] < 0-self.width or self.position[1] > self.simulation.height+self.height or self.position[1] < 0-self.height:
            return False
        return True
    def calculate(self, dt):
        if self.locked:
            return self.position
        resultante = self.force
        acelleration = resultante/self.mass
        self.speed += acelleration*dt
        self.position = self.position + self.speed*dt
        self.force = np.array([0, 0], dtype=np.float64).flatten()
        return self.position
def checkCollision(object1, object2):
    if object1.circle and object2.circle:
        if np.linalg.norm(object2.position - object1.position) <= object1.width/2 + object2.width/2:
                return True
        return False
    elif object1.circle == object2.circle:
        if (object1.position[0] < object2.position[0] + object2.width and
        object1.position[0] + object1.width > object2.position[0]):
        
        # Check if the rectangles are overlapping along the y-axis
            if (object1.position[1] < object2.position[1] + object2.height and object1.position[1] + object1.height > object2.position[1]):
            
            # The rectangles are overlapping
                return True
    # The rectangles are not overlapping
        return False
global gravityCalculated 
gravityCalculated = []
def calculate_gravity(objects, dt):
    global gravityCalculated
    for i, object1 in enumerate(objects):        
        for j, object2 in enumerate(objects):
            if i == j:
                continue
            if [i,j] in gravityCalculated or [j,i] in gravityCalculated:
                continue
            gravityCalculated.append([i,j])
            r = object2.position - object1.position
            dist = np.linalg.norm(r)
            force = object1.mass * object2.mass / dist ** 2
            direction = r/dist
            vectorForce = force * direction *500
            object1.addForce(vectorForce)
            object2.addForce(-vectorForce)
    gravityCalculated = []
            
def Collide(object1, object2, dt):

    COR = object1.COR*object2.COR
    normal = object2.position - object1.position
    distance = np.linalg.norm(normal)
    radius_sum = (object1.width / 2) + (object2.width / 2)
    if distance < radius_sum:
        # Calculate the overlap distance, plus one unit of distance
        overlap = (radius_sum - distance)+0.1

        # Calculate the unit vector in the direction from circle1 to circle2
        unit_vector = normal / distance
        object1.position -= (unit_vector * (overlap / 2))
        object2.position += (unit_vector * (overlap / 2))
        # Move the circles apart by half the overlap distance each, in opposite directions
    # Calculate the relative velocity along the normal vector
    if distance == 0:  # Prevent division by zero
        return
    normal /= distance  # Normalize the vector
    
    # Calculate relative velocity
    relative_velocity = object1.speed - object2.speed

    # Calculate velocity along the normal (dot product)
    velocity_along_normal = np.dot(relative_velocity, normal)
    # Objects are moving away from each other, so no response needed
    if velocity_along_normal > 0:
        return
    
    # Compute the impulse scalar
    impulse_scalar = -(1 + COR) * velocity_along_normal
    impulse_scalar /= (1 / object1.mass + 1 / object2.mass)
    
    # Compute the actual impulse
    impulse = impulse_scalar * normal
    object1.force +=  impulse/dt
    object2.force +=  -impulse/dt 