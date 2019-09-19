import priorityqueue
import networkx

MAXPRIORITY = 99999999999

def travelling_salesman(G, S):
    '''Input:
    S: A special subset of vertices V
    G: A graph created by networkx
    YOU CAN ALSO RUN DIJKSTRA'S AND GREEDILY GO TO THE CLOSEST VERTICE IN THE SPECIAL SET
    '''
    return

def weightedsetcover(S, w):
    '''Weighted set cover greedy algorithm:
    pick the set which is the most cost-effective: min(w[s]/|s-C|),
    where C is the current covered elements set.
    The complexity of the algorithm: O(|U| * log|S|) .
    Finding the most cost-effective set is done by a priority queue.
    The operation has time complexity of O(log|S|).
    Input:
    udict - universe U, which contains the <elem, setlist>. (dict)
    S - a collection of sets. (list)
    w - corresponding weight to each set in S. (list)
    Output:
    selected: the selected set ids in order. (list)
    cost: the total cost of the selected sets.
    '''

    udict = {}
    selected = list()
    scopy = [] # During the process, S will be modified. Make a copy for S.
    for index, item in enumerate(S):
        scopy.append(set(item))
        for j in item:
            if j not in udict:
                udict[j] = set()
            udict[j].add(index)

    pq = priorityqueue.PriorityQueue()
    cost = 0
    coverednum = 0
    for index, item in enumerate(scopy): # add all sets to the priorityqueue
        if len(item) == 0:
            pq.addtask(index, MAXPRIORITY)
        else:
            pq.addtask(index, float(w[index]) / len(item))
    print(len(udict))
    while coverednum < len(udict):
        a = pq.poptask() # get the most cost-effective set
        #print("a ", a)
        selected.append(a) # a: set id
        cost += w[a]
        #print("scopy[a] = ", len(scopy[a]))
        coverednum += len(scopy[a])
        # Update the sets that contains the new covered elements
        for m in scopy[a]: # m: element
            for n in udict[m]:  # n: set id
                if n != a:
                    scopy[n].discard(m)
                    if len(scopy[n]) == 0:
                        pq.addtask(n, MAXPRIORITY)
                    else:
                        pq.addtask(n, float(w[n]) / len(scopy[n]))
        #print("here set cover, length = ", coverednum)
        scopy[a].clear()
        pq.addtask(a, MAXPRIORITY)
                        
    return selected, cost

if __name__ == "__main__":
    '''S = [[1,2,3],
         [3,6,7,10],
         [8],
         [9,5],
         [4,5,6,7,8],
         [4,5,9,10],]
    w = [1, 2, 3, 4, 3, 5]
    selected, cost = weightedsetcover(S, w)'''
    Sp = [[1,2,3],
         [3,6,7,10],
         [8],
         [9,5],
         [4,5,6,7,8],
         [4,5,9,10],]
    w = [1, 2, 3, 4, 3, 5]
    S = []
    for lst in Sp:
        newSet = []
        for int_element in lst:
            converted_to_String="x"+str(int_element)
            newSet.append(converted_to_String)
        S.append(newSet)
    selected, cost = weightedsetcover(S, w)
    print("The sets that we have are: ", S)
    print("The weight array is as follows: ", w)
    print("selected: ", selected)
    print("cost: ", cost)