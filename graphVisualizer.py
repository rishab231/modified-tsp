import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
# from utils_sp18 import *
from student_utils_sp18 import *
# import planarity

RANGE_OF_INPUT_SIZES = range(201)
MAX_NAME_LENGTH = 20

def test():
	input_file = "50.in"
	input_data = utils.read_file(input_file)
	number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
	G = adjacency_matrix_to_graph(adjacency_matrix)
	return G

G = test()

#plt.show()
pos=nx.spring_layout(G)
nx.draw(G, with_labels = True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()


print(type(G))