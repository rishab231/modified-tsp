import networkx as nx
import sys
from utils import *
#import utils
from student_utils_sp18 import *
from weighted_set_cover import *
import random
import numpy as np
import time
from christofides import *
from graph import *

'''
Code for approximating TSP for a metric graph taken from here: https://pypi.org/project/python-christofides/
The code is saved in christofides.py and graph.py
'''

#networkx.relabel.convert_node_labels_to_integers
def graphSetCover(input_file, params=[], choice = 0):
	input_data = read_file(input_file)
	number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)

	#This is the weights list that we can into our weighted_set_cover
	#TODO: Change this into a smarter heuristic

	set_weights = [adjacency_matrix[i][i] for i in range(len(adjacency_matrix))]

	#This takes the average edge weight of a graph
	if choice == 1:
		for i in range(0,number_of_kingdoms):
			summation = 0
			num_neighbors = 0
			for j in range(number_of_kingdoms):
				if (adjacency_matrix[i][j]!="x"):
					num_neighbors = num_neighbors + 1
					summation = summation + adjacency_matrix[i][j]
			average = summation/num_neighbors
			set_weights[i] = set_weights[i] + average


	# Taking the maximum edge weight
	elif choice == 2:
		for i in range(0,number_of_kingdoms):
			maxima = -1
			for j in range(number_of_kingdoms):
				if (adjacency_matrix[i][j]!="x"):
					if (adjacency_matrix[i][j]>maxima):
						maxima = adjacency_matrix[i][j]
			set_weights[i] = set_weights[i] + maxima

	# Taking the minimum edge weight
	elif choice == 3:
		for i in range(0,number_of_kingdoms):
			minima = float("inf")
			for j in range(number_of_kingdoms):
				if (adjacency_matrix[i][j]!="x"):
					if (adjacency_matrix[i][j]<minima):
						minima = adjacency_matrix[i][j]
			set_weights[i] = set_weights[i] + minima

	#The set S representing the neighbors of each vertex
	S_neighbors = []
	for i in range(0,number_of_kingdoms):
		neighbors = [i+1]
		for j in range(number_of_kingdoms):
			if (adjacency_matrix[i][j]!="x"):
				neighbors.append(j+1)
		S_neighbors.append(neighbors)

	intermediate_vertices, cost = weightedsetcover(S_neighbors,set_weights)

	costConquer = 0
	for i in intermediate_vertices:
		costConquer += adjacency_matrix[i][i]

	'''
	#Now, because ordering starts from 0 from what is returned
	special_vertices = ["x"+str(i+1) for i in intermediate_vertices]
	final_set = set()
	for index in intermediate_vertices:
		for item in S_neighbors[index]:
			final_set.add(item)
	'''

	print("Cost of conquering (set cover) = ", costConquer)
	#return special_vertices
	return intermediate_vertices, costConquer

#print(graphSetCover("50.in"))

def tour(S, G, current):
	# Set of kingdoms that we have already conquered
	conquered = set()

	# The tour we have taken that covers all special vertices
	tourTaken = [current]
	minTarget = None
	start = current
	if current in S:
		conquered.add(current)

	costOfTravel = 0

	while len(conquered) != len(S):
		lengths, paths = nx.single_source_dijkstra(G, current)
		#print("reaching here for node ", current)
		min = float('inf')
		#minTarget = None
		for s in S:
			if lengths[s] <= min and s not in conquered and s != current:
				min = lengths[s]
				minTarget = s

		costOfTravel = costOfTravel + lengths[minTarget]
		for i in range(1,len(paths[minTarget])):
			p = paths[minTarget][i]
			tourTaken.append(p)

		# Adding the closest special vertex to conquered and conquering it
		conquered.add(minTarget)

		# Then proceeding from that vertex
		current = minTarget


	if minTarget is not None:
		print("here")
		length, path = nx.single_source_dijkstra(G, minTarget, start)
		costOfTravel += length

		for i in range(1,len(path)):
			p = path[i]
			tourTaken.append(p)

	#print("Cost of travel = ", costOfTravel)
	return tourTaken, costOfTravel


def solve(input_file):
	i_data = read_file(input_file)
	number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(i_data)
	G = adjacency_matrix_to_graph(adjacency_matrix)
	kingdom_name_to_index = lambda name : list_of_kingdom_names.index(name)
	start = kingdom_name_to_index(starting_kingdom)
	print(start)
	minSol = float('inf')
	minCover = None
	minCoverCost = 0
	minTourCost = 0
	minTour = None
	for i in range(4):
		cover, costConquer = graphSetCover(input_file, choice = i)
		print("printing cover", cover)
		tree = steiner(G, cover)
		new_nodes = dict()
		tnodes = list(tree.nodes())
		for i in range(len(tnodes)):
			new_nodes[i] = tnodes[i]
		#distance_matrix = tree_to_dist_matrix(tree)

		if len(tree.nodes()) == 0:
			t, costOfTravel = tour(cover, G, start)
			if costConquer + costOfTravel < minSol:
				minSol = costConquer + costOfTravel
				minCover = cover
				minTour = t
				minTourCost = costOfTravel
				minCoverCost = costConquer
			continue


		if len(cover) <= 30:
			distance_matrix = complete_matrix(tree, G)
			TSP = compute(distance_matrix)

			if TSP is not None:

				#TSP = compute(distance_matrix)
				nodes_extract = []

				for i in TSP['Christofides_Solution']:
					nodes_extract.append(new_nodes[i])
				print("*******")
				print(TSP['Christofides_Solution'])
				print(nodes_extract)
				pathTSP, costOfTSP = calculateCost(G, nodes_extract, start)
				if costConquer + costOfTSP < minSol:
					print("updating minSol with TSP Approx")
					print(costOfTSP)
					print(pathTSP)
					minSol = costConquer + costOfTSP
					minCover = cover
					minTour = pathTSP
					minTourCost = costOfTSP
					minCoverCost = costConquer

		t, costOfTravel = tour(cover, G, start)

		if costConquer + costOfTravel < minSol:
			minSol = costConquer + costOfTravel
			minCover = cover
			minTour = t
			minTourCost = costOfTravel
			minCoverCost = costConquer

	return minTour, minCover
	print("Set cover : ", minCover)
	print("Tour : ", minTour)
	print("Cost of travel  = ", minTourCost)
	print("Cost of conquering = ", minCoverCost)
	print("Total cost = ", minTourCost + minCoverCost)

def steiner(G, special):
	'''Input:
	G is the graph that we input
	Special is the list of special vertices (or terminal nodes) for Steiner Tree needs to be created

	Output:
	A Steiner Tree in NetworkX Graph format
	'''
	t = nx.algorithms.approximation.steinertree.steiner_tree(G,special, weight = 'weight')
	print("steiner tree: ", t.nodes())
	return t

def tree_to_dist_matrix(G):
	nodes = list(G.nodes())
	print("printing nodes now", nodes)
	num = len(nodes)
	matrix = []
	max_edge = 0
	for u,v,d in G.edges(data = True):
		w = d['weight']
		if w > max_edge:
			max_edge = w

	for i in range(num):
		adj_list = [0]
		for x in range(i):
			adj_list.append(0)
		node = nodes[i]
		for j in range(i + 1, num):
			node2 = nodes[j]
			if G.has_edge(node, node2):
				adj_list.append(G.get_edge_data(node, node2)['weight'])
			else:
				#adj_list.append(max_edge**10)
				adj_list.append(0)
				#adj_list.append(sys.float_info.max/1000)
		matrix.append(adj_list)

	return matrix

def complete_matrix(tree, G):
	nodes = list(tree.nodes())
	print("printing nodes now", nodes)
	num = len(nodes)
	matrix = []
	max_edge = 0
	for i in range(num):
		adj_list = [0]
		for x in range(i):
			adj_list.append(0)
		node = nodes[i]
		for j in range(i + 1, num):
			node2 = nodes[j]
			if G.has_edge(node, node2):
				adj_list.append(G.get_edge_data(node, node2)['weight'])
			else:
				length, path = nx.single_source_dijkstra(tree, node, node2)
				adj_list.append(length)
		matrix.append(adj_list)
	return matrix

def dfs(graph, start, special):
    visited, stack = set(), [start]
    tour = []
    conquered = set()
    while stack:
        vertex = stack.pop()
        tour.append(vertex)
        if vertex == start and len(special) == len(conquered):
        	return tour
        visited.add(vertex)
        if vertex in special:
        	conquered.add(vertex)
        #nodes = graph.neighbors(vertex)
        nodes = [n for n in graph.neighbors(vertex)]
        #print(nodes)
        choice = random.choice(nodes)
        nodes.remove(choice)
        stack.extend(nodes)
        stack.append(choice)
    return visited

def calculateCost(graph, tour, start):
	cost = 0
	prev = start
	pathTSP = [start]
	print("printing tour", tour)
	for x in range(1, len(tour)):
		current = tour[x]
		length, path = nx.single_source_dijkstra(graph, prev, current)
		cost += length
		prev = current
		pathTSP.extend(path[1:])
	if path[len(path) - 1] != start:
		length, path = nx.single_source_dijkstra(graph, path[len(path)-1], start)
		pathTSP.extend(path[1:])
		cost += length
	return pathTSP, cost



#solve("200.in")
for i in range(400,726):
	prefix = r"inputs/"
	input_file = prefix + str(i) + ".in"

	try:
		testing = read_file(input_file)
	except:
		print("File ", i, " is missing. Continuing the loop")
		continue

	prefix2 = r"outputs/"
	filename = prefix2 + str(i) + ".out"
	f = open(filename, "w+")

	minTour, minCover = solve(input_file)

	input_data = read_file(input_file)

	number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
	res = ""
	res2 = ""
	for k in minTour:
   		res += list_of_kingdom_names[k] + " "

	for k in minCover:
   		res2 += list_of_kingdom_names[k] + " "

	res = res[0:len(res)- 1]
	res2 = res2[0:len(res2)- 1]
	f.write(res + "\n")
	f.write(res2)
	print("File number ", i, " done")
