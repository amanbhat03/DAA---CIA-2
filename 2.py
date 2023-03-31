2) Cultural Algorithm for TSP
-----------------------------

Code:-
    
import random
import math

num_cities = 20
distance_matrix = [[0 for j in range(num_cities)] for i in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i == j:
            continue
        distance_matrix[i][j] = math.sqrt((i-j)**2 + (i-j)**2)

population_size = 100
num_generations = 100
elite_size = 10
mutation_rate = 0.01
knowledge_pool_size = 10
knowledge_sharing_rate = 0.5

def fitness(tour):
    distance = 0
    for i in range(num_cities - 1):
        distance += distance_matrix[tour[i]][tour[i+1]]
    distance += distance_matrix[tour[num_cities-1]][tour[0]]
    return 1/distance

class Tour:
    def __init__(self, cities):
        self.cities = cities
        self.fitness = fitness(self.cities)

    def __lt__(self, other):
        return self.fitness < other.fitness

    def mutate(self):
        i, j = random.sample(range(num_cities), 2)
        self.cities[i], self.cities[j] = self.cities[j], self.cities[i]
        self.fitness = fitness(self.cities)

population = [Tour(random.sample(range(num_cities), num_cities)) for _ in range(population_size)]

knowledge_pool = []

for generation in range(num_generations):
    population.sort(reverse=True)

    for tour in population[:elite_size]:
        if tour not in knowledge_pool:
            knowledge_pool.append(tour)
        if len(knowledge_pool) > knowledge_pool_size:
            knowledge_pool.pop(0)

    new_population = []

    for i in range(population_size):
        parents = random.sample(population, 2)

        child_cities = parents[0].cities.copy()
        for j in range(num_cities):
            if child_cities[j] != parents[1].cities[j] and random.random() < knowledge_sharing_rate:
                for k in range(len(knowledge_pool)):
                    if child_cities[j] in knowledge_pool[k].cities:
                        idx = knowledge_pool[k].cities.index(child_cities[j])
                        child_cities[j], child_cities[idx] = child_cities[idx], child_cities[j]
                        break

        child = Tour(child_cities)
        if random.random() < mutation_rate:
            child.mutate()

        new_population.append(child)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------  
