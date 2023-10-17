import pygame
import numpy as np
from scipy.integrate import odeint
class Simulation():
    def __init__(self, width, height, tittle, color, dt, collisions = False):
        self.dt = dt
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
    def calculate(self, lenght, dt, method = 'euler'):
        self.lenght = lenght
        self.dt = dt
        self.steps = round(lenght/dt)
        for q in range(self.steps):
            positions = []
            listaPos = np.array([i.position for i in self.gravity_objects])
            if len(self.gravity_objects) > 0:
                forces = acc(listaPos, np.array([i.mass for i in self.gravity_objects]), 0.1, 0.001)
            for object in self.gravity_objects:
                object.force += forces[self.gravity_objects.index(object)]
            if self.collisions: 
                for i in range(len(self.objects)):
                    object1 = self.objects[i]
                    for j in range(i + 1, len(self.objects)):
                        object2 = self.objects[j]
                        if object1.collisionLayer == object2.collisionLayer:
                            Collide(object1, object2, dt)
            for object in self.objects:
                if method == 'euler':
                    object.calculate(dt)
                elif method == 'verlet':
                    object.calculateVerlet(dt)
                positions.append([object, object.position])
            self.positions_history.append(positions)
class Object(pygame.Surface):
    def __init__(self, width, height, position, mass, speed , color, simulation,circle=False, COR = 1, collisionLayer=0):
        self.height = height
        self.width = width
        self.gravity = False
        self.position = np.array(position, dtype=np.float64).flatten()
        self.x , self.y = position
        self.circle = circle
        self.frictionCoeficient = 0
        self.mass = mass
        self.simulation = simulation
        self.speed = np.array([speed[0], -speed[1]], dtype=np.float64).flatten()
        self.oldPosition = np.array(position, dtype=np.float64).flatten() - self.speed*self.simulation.dt
        self.force = np.array([0,0], dtype=np.float64).flatten()
        if color == "black" or color == (0,0,0):
            color = (0,0,1)
        self.color = color
        self.collisionLayer = collisionLayer
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
        if any(self.speed != np.array([0, 0], dtype=np.float64).flatten()):
            Fat = self.mass*self.frictionCoeficient
            Fat = -(self.speed/np.linalg.norm(self.speed)) *Fat
            self.force += Fat
        acelleration = np.array(self.force/self.mass, dtype=np.float64).flatten()
        self.speed += acelleration*dt
        self.position = self.position + self.speed*dt
        self.force = np.array([0, 0], dtype=np.float64).flatten()
        return self.position
    def calculateVerlet(self, dt):
        if self.locked:
            return self.position
        
        if any(self.speed != np.array([0, 0], dtype=np.float64).flatten()):
            Fat = self.mass*self.frictionCoeficient
            Fat = -(self.speed/np.linalg.norm(self.speed)) *Fat
            self.force += Fat
        velocity = self.position - self.oldPosition
        self.speed = velocity/dt
        self.oldPosition = self.position
        acelleration = np.array(self.force/self.mass, dtype=np.float64).flatten()
        self.position = self.position + velocity + acelleration * dt *dt 
        self.force = np.array([0, 0], dtype=np.float64).flatten()
        return self.position     
global gravityCalculated 
gravityCalculated = []
import numpy as np

def Collide(object1, object2, dt):
    distance = np.linalg.norm(object2.position - object1.position)
    minimum_distance = object1.width/2 + object2.width/2
    if distance < minimum_distance and distance > 0:
        normal = object2.position - object1.position
        rv = object2.speed - object1.speed
        velAlongNormal = np.dot(rv, normal)
        if velAlongNormal > 0:
            return
        e = min(object1.COR, object2.COR)
        j = -(1 + e) * velAlongNormal
        j /= 1 / object1.mass + 1 / object2.mass
        impulse = j * normal
        object1.force -= (1 / object1.mass * impulse)*object1.mass
        object2.force += (1 / object2.mass * impulse)*object2.mass
def Collide3(object1, object2, dt):
    distance = np.linalg.norm(object2.position - object1.position)
    minimum_distance = object1.width/2 + object2.width/2
    if distance < minimum_distance and distance > 0:
        penetration = (minimum_distance - distance) / 2
        push = (object1.position - object2.position) / distance * penetration

        total_mass = object1.mass + object2.mass
        mass_ratio1 = object2.mass / total_mass
        mass_ratio2 = object1.mass / total_mass

        object1.position += push * mass_ratio1
        object2.position -= push * mass_ratio2

        restitution = min(object1.COR, object2.COR)
        object1.oldPosition += push * mass_ratio1 * restitution
        object2.oldPosition -= push * mass_ratio2 * restitution
        print(object1.oldPosition)
def Collide2(object1, object2, dt, bias=0.5):
    delta = object2.position - object1.position
    sum_radii = object2.width/2 + object1.width/2
    distance = np.linalg.norm(delta)
    collision_normal = delta / distance
    relative_speed = object2.speed - object1.speed
    constraint_speed = np.dot(collision_normal, relative_speed)
    constraint_value = distance - sum_radii
    
    if constraint_value < 0 and constraint_speed < 0:
        reduced_mass = 1 / (1 / object1.mass + 1 / object2.mass)
        impulse = collision_normal * (-constraint_speed - bias / dt * constraint_value) * reduced_mass
        #object1.force -= impulse
        #object2.force += impulse 
        overlap = sum_radii - distance
        object1.position -= collision_normal * overlap *object1.mass/(object1.mass+object2.mass)
        object2.position += collision_normal * overlap *object2.mass/(object1.mass+object2.mass)
from numba import float64, int64, f8, float32
from numba import guvectorize
@guvectorize(["float64[:, :],  float64[:] , float64 ,float64 ,float64[:, :]"], "(n, m), (n) ,(),()-> (n, m)", nopython=False, fastmath=True, forceobj=True)
def acc(x_ij, M_i, G=0.1, approx_error=0.001, out=None):
    '''
            calculation of accelaration given particles ( many to many )
            Parameters : 
            x_ij : ndarray
            cordinataes of particle
            M_i : ndarray
            masses of particles

            Return :
                    a_ij : ndarray
                    accelaration of every particle	 

    '''
    # number of particles
    n = x_ij.shape[0]

    for i in range(x_ij.shape[0]):
        acc = 0
        # separate particles : one to many
        X_i = x_ij[i]
        x_kj = np.delete(x_ij, i, axis=0)
        m = M_i[i]
        m_k = np.delete(M_i, i).reshape(-1, 1)

        # dr matrix contain all delta elemenets [[x_i0 - x_10, x_i1 - x_i1],[...,...],[x_i0 - x_k0, x_i1- x_k1]]
        dr_kj = x_kj - X_i

        # [(x_i0-x_k0)^2,(x_i1-x_k1)^2]
        mod_dr_kj = dr_kj**2
        #[sum_k (x_i0-x_k0)^2, sum_k (x_i1-x_k1)^2]
        mod_dr_k = np.sum(mod_dr_kj, axis=1)

        # when |dr| --> 0 then F--> infinity
        error_value = approx_error
        if (mod_dr_k < error_value).any():
            #message = '|dr|, |dr|-->0 , , there for the dr has been repalced by configured error value {}  '.format(error_value)
            mod_dr_k[mod_dr_k < error_value] = error_value
            # print(message)

        # if x_kj.shape[0] > 2 :
            # warnings.showwarning(
            # message, filename='gravity.py', lineno=135, category=RuntimeWarning)

        mod_dr_k = mod_dr_k.reshape(-1, 1)
        F = G*m*m_k*(dr_kj/mod_dr_k)
        out[i] = np.sum(F, axis=0)*1000
    return out
