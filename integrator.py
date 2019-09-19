import solver as solve
import random_graph_gen as gen
import networkx as nx
import numpy as np
import random

def get_ino(Graph):
    n = nx.number_of_nodes(Graph)
    filename = str(n) + ".in"

    f = open(filename, "w+")

    f.write(str(n) + "\n")

    nodes = ""
    for i in range(n):
        nodes += str(i) + " "
    f.write(nodes + " \n")
    f.write(str(random.choice(range(0, n))) + "\n")

    for i in range(n):
        matrixline = ""
        for j in range(n):
            if i == j:
                matrixline += str(random.choice(range(40, 70))) + " "
            elif Graph.has_edge(i, j):
                wt = Graph[i][j]['weight']
                matrixline += str(int(wt)) + " "
            else:
                matrixline += "x "
        f.write(matrixline + "\n")



    # matrix = nx.to_numpy_matrix(Graph)
    # print(np.shape(matrix))

    # row = 0
    # for i in matrix:
    #     print(np.shape(i))
    #     matrixline = ""
    #     col = 0
    #     for j in i:
    #         print(j)
    #         if col == row:
    #             matrixline += str(random.random()) + " "
    #             col += 1
    #             continue
    #         elif str(j) == '0':
    #             matrixline += 'x'
    #             col += 1
    #         else:
    #             matrixline += str(j) + " "
    #             col += 1
    #     row += 1
    #     print(matrixline)
    #     f.write(matrixline + "\n")



nodes = 200

g = gen.ret_good_er(nodes)
print(type(g))
get_ino(g)
