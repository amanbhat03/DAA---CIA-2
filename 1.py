1) Genetic Algorithm for Travelling Salesman Problem (TSP)
------------------------------------------------------------

Code:-
    
    
import numpy as np
import random

distance_matrix = np.array([
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9]
])

population_size = 20
num_generations = 100

mutation_rate = 0.01

def calculate_fitness(individual):
    total_distance = 0
    for i in range(len(individual) - 1):
        total_distance += distance_matrix[individual[i], individual[i+1]]
    total_distance += distance_matrix[individual[-1], individual[0]]
    fitness = 1 / total_distance
    return fitness

population = []
for i in range(population_size):
    individual = list(range(distance_matrix.shape[0]))
    random.shuffle(individual)
    population.append(individual)


for generation in range(num_generations):
    fitness_scores = []
    for individual in population:
        fitness_scores.append(calculate_fitness(individual))

    parents = []
    for i in range(2):
        parent_index = np.random.choice(range(population_size), size=5, replace=False, p=fitness_scores / np.sum(fitness_scores))
        parent_fitness = [fitness_scores[i] for i in parent_index]
        parent = population[parent_fitness.index(max(parent_fitness))]
        parents.append(parent)

    offspring = []
    for i in range(population_size - 2):
        child = []
        for j in range(distance_matrix.shape[0]):
            if random.uniform(0, 1) < mutation_rate:
                child.append(random.randint(0, distance_matrix.shape[0]-1))
            else:
                gene = parents[random.randint(0, 1)][j]
                while gene in child:
                    gene = parents[random.randint(0, 1)][j]
                child.append(gene)
        offspring.append(child)

    population = parents + offspring

best_individual = max(population, key=calculate_fitness)
print('Best solution:', best_individual)


-------------------------------------------------
Output:-
    
Enter No. of Cities: 5
Enter Cost Matrix
Enter Elements of Row:- : 1
1 2 3 4 5
Enter Elements of Row:- : 2
2 3 4 5 6
Enter Elements of Row:- : 3
3 4 5 6 7
Enter Elements of Row:- : 4
4 5 6 7 8
Enter Elements of Row:- : 5
5 6 7 8 9

The cost list is:

1       2       3       4       5
2       3       4       5       6
3       4       5       6       7
4       5       6       7       8
5       6       7       8       9
  
The Path is:
1 -->5 -->4 -->3 -->2 -->1
 
Minimum cost:25
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

