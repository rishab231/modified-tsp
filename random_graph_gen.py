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


# graph = ret_good_er()

# print(graph)
# print(type(graph))
