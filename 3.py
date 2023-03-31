3)Genetic Algorithm for sine function
-------------------------------------

Code:-
    
import random
import math

min_x = 0
max_x = 2*math.pi

population_size = 100
mutation_rate = 0.01
num_generations = 1000
tournament_size = 5

def fitness(x):
    return math.sin(x)

class Chromosome:
    def __init__(self, x):
        self.x = x
        self.fitness = fitness(x)

    def __lt__(self, other):
        return self.fitness < other.fitness


population = [Chromosome(random.uniform(min_x, max_x)) for _ in range(population_size)]

for generation in range(num_generations):
    parents = []
    for _ in range(2):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament)
        parents.append(winner)

    child_x = sum(p.x for p in parents) / 2
    child = Chromosome(child_x)

    if random.random() < mutation_rate:
        child.x += random.uniform(-0.1, 0.1)

    child.fitness = fitness(child.x)
    worst_chromosome = min(population)
    if child > worst_chromosome:
        population.remove(worst_chromosome)
        population.append(child)
best_chromosome = max(population)
print("Best solution: x =", best_chromosome.x, ", fitness =", best_chromosome.fitness)

----------------------------------------------
Output:-
    
Best solution: x = 1.5707963177777777 , fitness = 1.0
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
