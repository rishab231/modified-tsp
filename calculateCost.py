
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
import networkx as nx
import numpy as np
#from utils_sp18 import *
from utils import *
from student_utils_sp18 import *
# import planarity

RANGE_OF_INPUT_SIZES = range(201)
MAX_NAME_LENGTH = 20

input_file = "100.in"
output_file = "100.out"

input_data = utils.read_file(input_file)
output_data = utils.read_file(output_file)
number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
node_weights = [adjacency_matrix[i][i] for i in range(len(adjacency_matrix))]


kingdom_tour = output_data[0]
conquered_kingdoms = output_data[1]
list_of_edges_in_tour = tour_to_list_of_edges(kingdom_tour)
kingdom_name_to_index = lambda name : list_of_kingdom_names.index(name)
edges_in_tour_by_index = map(lambda edge : (kingdom_name_to_index(edge[0]), kingdom_name_to_index(edge[1])), list_of_edges_in_tour)

G = adjacency_matrix_to_graph(adjacency_matrix)
prev = kingdom_name_to_index(kingdom_tour[0])
costConquer = 0
costTour = 0

for i in range(1,len(kingdom_tour)):
	t = kingdom_tour[i]
	next = kingdom_name_to_index(t)
	dist = G.get_edge_data(prev, next)['weight']
	costTour += dist
	prev = next

for k in conquered_kingdoms:
	ind = kingdom_name_to_index(k)
	costConquer += node_weights[ind]

print("Tour cost = ", costTour)
print("Conquering cost = ", costConquer)
print("Total cost = ", costTour + costConquer)
