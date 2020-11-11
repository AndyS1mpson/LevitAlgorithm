from networkx.algorithms.smallworld import random_reference
import numpy as np
from networkx import DiGraph
import random
from queue import Queue

def graph_generator(num_of_nodes = 5,num_of_edge = 6):
    if num_of_edge < num_of_nodes:
        return Exception("Graph is not connected")
    else:
        nodes = []
        # генерируем названия узлов
        nodes = list(range(0,num_of_nodes))
        iter = 0
        # создаем пустой граф
        graph = DiGraph()
        while iter < num_of_edge:
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

def Levit(graph,s = 0):
    # инициализируем нужные нам множества и очереди
    M = set()
    M1_main = Queue()
    M1_urgent = Queue()
    M1 = set([M1_main,M1_urgent])
    M2 = set()
    # помещаем заданную вершину в срочную очередь
    M1_urgent.put(s)
    M1.add(s)
    # помещаем все остальные вершины в множество M2
    for node in graph.nodes:
        if node != s:
            M2.add(node)
    # создаем список кратчайших путей от заданной вершины до остальных
    d = [None] * len(graph.nodes) - 1
    d[s] = 0
    list_of_edges = list(graph.edges)
    while not M1_main and M1_urgent:
        if not M1_urgent:
            u = M1_urgent.get()
        else: 
            u = M1_main.get()
        # Получаем вершины, соединенные с текущим ребром
        le = filter(lambda x: x[0] == u,list_of_edges)
        for i in len(le):
            for v in le[i][1]:
                if v in M2:
                    M1_main.put(v)
                    d[v] = d[u] + graph[u][v]
                elif v in M1:
                    d[v] = min(d[v],d[u] + graph[u][v])
                elif v in M:
                    if d[v] > d[u] + graph[u][v]:
                        d[v] = d[u] + graph[u][v]
                        M1.add(v)
    return d

    

if __name__ == "__main__":
    g = graph_generator()
    l = list(g.edges)[0]
    print(l)
    print(l[0])
