from networkx.algorithms.smallworld import random_reference
import numpy as np
from networkx import Graph
import random

def data_generator(num_of_nodes = 5,num_of_edge = 3):
    nodes = []
    # генерируем названия узлов
    nodes = list(range(0,num_of_nodes))
    iter = 0
    graph = Graph()
    while iter < len(nodes):
        start = random.choice(nodes)
        end = random.choice(nodes)
        if (start,end) in graph:
            continue
        else:
            weight = random.choice(range(1,10))            
            graph.add_edge(start,end)
            graph[start][end]['weight'] = weight
        iter = iter + 1
    return graph

    

if __name__ == "__main__":
    print(data_generator())
