5)Ant Colony Optimization for finding the shortest path in a graph
-------------------------------------------------------------------

Code:-
    
import random
import numpy as np

num_ants = 10
num_iterations = 100
alpha = 1
beta = 5
rho = 0.1
Q = 100
initial_pheromone = 1
pheromone_evaporation = 0.1

graph = np.array([
    [0, 2, 4, 0, 0, 0],
    [2, 0, 2, 4, 2, 0],
    [4, 2, 0, 0, 3, 0],
    [0, 4, 0, 0, 3, 2],
    [0, 2, 3, 3, 0, 2],
    [0, 0, 0, 2, 2, 0],
])

pheromones = np.ones_like(graph) * initial_pheromone

def fitness(path):
    return graph[path[:-1], path[1:]].sum()

class Ant:
    def __init__(self, start_node):
        self.path = [start_node]
        self.visited = set()
        self.visited.add(start_node)

    def choose_next_node(self):
        current_node = self.path[-1]
        unvisited_nodes = set(range(graph.shape[0])) - self.visited
        probabilities = [pheromones[current_node][node]**alpha * (1/graph[current_node][node])**beta for node in unvisited_nodes]
        probabilities /= sum(probabilities)
        next_node = np.random.choice(list(unvisited_nodes), p=probabilities)
        self.path.append(next_node)
        self.visited.add(next_node)

for iteration in range(num_iterations):
    ants = [Ant(random.randint(0, graph.shape[0]-1)) for _ in range(num_ants)]

    for ant in ants:
        while len(ant.visited) < graph.shape[0]:
            ant.choose_next_node()

        ant.path.append(ant.path[0])
        fitness_value = fitness(ant.path)
        for i in range(len(ant.path)-1):
            pheromones[ant.path[i]][ant.path[i+1]] = (1-rho) * pheromones[ant.path[i]][ant.path[i+1]] + rho * Q/fitness_value

    best_ant = min(ants, key=lambda ant: fitness(ant.path))
    for i in range(len(best_ant.path)-1):
        pheromones[best_ant.path[i]][best_ant.path[i+1]] = (1-pheromone_evaporation) * pheromones[best_ant.path[i]][best_ant.path[i+1]] + pheromone_evaporation * initial_pheromone

shortest_path = min(ants, key=lambda ant: fitness(ant.path)).path
print(shortest_path)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
