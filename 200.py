import random
import numpy as np
import networkx as nx
import student_utils_sp18 as sputil

def er_graph(nodes):
    p = 0.04
    graph = nx.fast_gnp_random_graph(nodes, p)
    for u,v,d in graph.edges(data = True):
        d['weight'] = random.randint(40,70)
    return graph

def ret_good_er(nodes):
    i = 1
    flag = True
    while flag:
        gr = er_graph(nodes)

        print("Trial #: " + str(i))
        i += 1

        try:
            if nx.is_connected(gr):
                print("It's connected")
                if sputil.is_metric(gr):
                    print("Is Metric")
                    print("printing graph now")
                    flag = False
                    print(gr.nodes())
                    for u,v,d in gr.edges(data = True):
                        print(u,v, " -> weight = ", d['weight'])
                    return gr
            break
        except:
            print("HERE")
            continue
def try200():
	g = nx.Graph()
	g.add_nodes_from(['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12','x13','x14','x15','x16'])
	

# graph = ret_good_er()

# print(graph)
# print(type(graph))
