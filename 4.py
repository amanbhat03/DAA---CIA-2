4) Particle Swarm Optimization for sine function - both maxima and minima
--------------------------------------------------------------------------

Code:-
    
import random
import math

num_particles = 50
num_dimensions = 1
max_iterations = 100
c1 = 2
c2 = 2
w = 0.7
bounds = [(-math.pi, math.pi)]
max_velocity = (bounds[0][1] - bounds[0][0]) / 10

def fitness(x):
    return abs(math.sin(x[0]))

class Particle:
    def __init__(self):
        self.position = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(num_dimensions)]
        self.velocity = [random.uniform(-1, 1) for _ in range(num_dimensions)]
        self.best_position = self.position.copy()
        self.best_fitness = fitness(self.position)

    def update_position(self):
        for i in range(num_dimensions):
            self.position[i] += self.velocity[i]
            if self.position[i] < bounds[i][0]:
                self.position[i] = bounds[i][0]
                self.velocity[i] *= -1
            elif self.position[i] > bounds[i][1]:
                self.position[i] = bounds[i][1]
                self.velocity[i] *= -1

        current_fitness = fitness(self.position)
        if current_fitness > self.best_fitness:
            self.best_position = self.position.copy()
            self.best_fitness = current_fitness

    def update_velocity(self, global_best_position):
        for i in range(num_dimensions):
            r1 = random.random()
            r2 = random.random()
            cognitive_velocity = c1 * r1 * (self.best_position[i] - self.position[i])
            social_velocity = c2 * r2 * (global_best_position[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + cognitive_velocity + social_velocity
            if abs(self.velocity[i]) > max_velocity:
                self.velocity[i] = max_velocity if self.velocity[i] > 0 else -max_velocity

particles = [Particle() for _ in range(num_particles)]

global_best_fitness = -math.inf
global_best_position = None
for particle in particles:
    if particle.best_fitness > global_best_fitness:
        global_best_fitness = particle.best_fitness
        global_best_position = particle.best_position.copy()

for iteration in range(max_iterations):
    for particle in particles:
        particle.update_velocity(global_best_position)
        particle.update_position()
        if particle.best_fitness > global_best_fitness:
            global_best_fitness = particle.best_fitness
            global_best_position = particle.best_position.copy()

    max_particle_velocity = max([abs(particle.velocity[0]) for particle in particles])
    if max_particle_velocity < max_velocity/10:
        break

print(f"Global best position: {global_best_position}")
print(f"Global best fitness: {global_best_fitness}")

-------------------------------------------------
Output:-
    
Global best position: [-1.5707963125947286]
Global best fitness: 0.9999999999999999
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
