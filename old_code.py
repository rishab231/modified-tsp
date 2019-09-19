'''
def tourRandom(S, G, current):
	# Set of kingdoms that we have already conquered
	conquered = set()

	# The tour we have taken that covers all special vertices
	tourTaken = [current]
	minTarget = None
	start = current
	if current in S:
		conquered.add(current)

	costOfTravel = 0

	while trials in range(1000):
		order = random.shuffle()

	while len(conquered) != len(S):
		lengths, paths = nx.single_source_dijkstra(G, current)
		sorted_lengths = sorted(lengths.items(), key = lambda (k,v): v)

		for x in range(5):
			dest, length = sorted_lengths[x]



		min = float('inf')
		minTarget = None
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

	length, path = nx.single_source_dijkstra(G, minTarget, start)
	costOfTravel += length



	for i in range(1,len(path)):
			p = path[i]
			tourTaken.append(p)

	#print("Cost of travel = ", costOfTravel)
	return tourTaken, costOfTravel


solve("50.in")

shortestTourTillNow = []
costOfShortestTour = float('inf')

def recurse(G, current, tour, special, conquered, cost, start):
	if len(conquered) == len(special):
		length, path = nx.single_source_dijkstra(G, current, start)
		tour.append(path[1:])
		cost = cost + length
		if cost < costOfShortestTour:
			shortestTourTillNow = tour
			minCost= cost
			tour = tour[0: len(tour) - len(path)]
			cost = cost - length

		return


	lengths, paths = nx.single_source_dijkstra(G, current)
	sorted_lengths = sorted(lengths.items(), key = lambda (k,v): v)
	i = 0
	while num <= 5 or i == len(sorted_lengths) - 1:
		dest, length = sorted_lengths[x]
		if dest not in special or if dest in conquered:
			continue
		path = paths[dest]
		cost += length 
		tour.extend(path[1:])
		conquered.add(dest)
		recurse(G, dest, tour, special, conquered, cost + length, start)
		num += 1




def get_ino(minTour, minCover):
    filename = str(n) + ".out"
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

'''


def randomize(special, G, current):
	S = [x for x in iter(special)]
	minCost = float('inf')
	minTour = None
	start = current
	conquered = set()
	if start in special:
		conquered.add(start)
		S.remove(start)
	order = S

	print("New trial")
	print("Order = ", order)
	if start in special:
		print("printing start-special : ", S)

	for trials in range(2000):
		tempTour = [start]
		#print("before shuffle : ", order)
		random.shuffle(order)
		#print("printing order: ", order)
		prev = start
		cost = 0
		for i in range(len(order)):
			current = order[i]

			length, path = nx.single_source_dijkstra(G, prev, current)
			prev = current
			tempTour.extend(path[1:])
			cost += length

		length, path = nx.single_source_dijkstra(G, prev, start)
		cost += length
		tempTour.extend(path[1:])

		if cost < minCost:
			minTour = tempTour
			minCost = cost


	print("Min Cost Tour:", minTour)
	print("Min cost = ", minCost)
	return minTour, minCost
