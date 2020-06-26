from queue import PriorityQueue
import colorama
from colorama import Fore, Back, Style


#store the minimum path
def visualize(frontier):
    colorama.init()
    for i in range(len(frontier.queue)):
        text = str(frontier.queue[i])
        if i == 0:
            print(Back.RED + Fore.WHITE + text + Style.RESET_ALL)
        else:
            print(text)
    print()

def build_graph_weighted(file):
    #Builds a weighted, undirected graph
    graph = {}
    for line in file:
        v1, v2, w = line.split(',')
        v1, v2 = v1.strip(), v2.strip()
        w = int(w.strip())
        if v1 not in graph:
            graph[v1] = []
        if v2 not in graph:
            graph[v2] = []
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))
    return graph

# Helper methods for A*
def build_heuristic_dict():
    h = {}
    with open("to_Craiova.txt", 'r') as file: # heuristic straight line distance dictionary
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h

def heuristic(node, values):
    return values[node]
# A* search
temp=[]
def a_star(graph, start, dest, visualization=False):
    """Performs A* search on graph 'graph' with
        'start' as the beginning node and 'dest' as the goal.
        Returns shortest path from 'start' to 'dest'.
        If 'visualization' is set to True, then progress of
        algorithm is shown."""

    frontier = PriorityQueue()#to keep best cost paths first

    # uses helper function for heuristics
    h = build_heuristic_dict()

    # path is a list of tuples of the form ('node', 'cost')
    frontier.put((0,[(start, 0)]))
    explored = set()

    while not frontier.empty():

        # show progress of algorithm
        if visualization:
            visualize(frontier)
       
        # shortest available path
        path = frontier.get()[1]
        
        # frontier contains paths with final node unexplored
        node = path[-1][0]
        g_cost = path[-1][1]
        explored.add(node)

        # goal test:
        if node == dest:
            # return only path without cost
            for it in path:
                temp.append(it[1])
            return [x for x, y in path]

        for neighbor, distance in graph[node]:
            cumulative_cost = g_cost + distance
            f_cost = cumulative_cost + heuristic(neighbor, h)
            new_path = path + [(neighbor, cumulative_cost)]

            # add new_path to frontier
            if neighbor not in explored:
                frontier.put((f_cost,new_path))

            # update cost of path in frontier
            elif neighbor in frontier.queue:
                frontier.put((f_cost,new_path))
                
    return false

def friendMeetCity(path):
    print("Distances: ")
    print(temp)
    size=len(path)
    for index in range(0, int(size/2)-1):
        print("First friend arrives from ", path[index], " in ", path[index+1])
        print("Second friend leaves from ", path[size - index - 1], " and arrives  in ", path[size - index - 2])
        print("\n")
    print("Friends meet in: "+path[int(size/2)])

    

    
