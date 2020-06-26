
from A_star_search_Romania_Map import *
import time
import random
cities=["Craiova","Pitesti","Bucuresti","Oradea","Arad","Eforie","Drobeta","Fagaras","Giurgiu","Zerind","Timisoara",
        "Sibiu","Lugoj","Mehadia","Ramnicu Valcea","Urziceni","Hirsova","Vaslui","Iasi","Neamt"]

with open('graph.txt', 'r') as file:
    lines = file.readlines() #fill the graph and build
    graph = build_graph_weighted(lines[1:])

#random or keyboard input data
if(int(input("Enter 1 if you want random city or 2 if you want to introduce them\n"))==1):
    start=cities[random.randint(0,len(cities)-1)]
    dest=cities[random.randint(0,len(cities)-1)]
    print(" Start city of first friend: "+start +"\n"+" Start city of the second friend: "+ dest)
else:
    start = input("Enter the starting city of the first friend\n")
    dest = input("Enter the starting city of the second friend\n")
t1 = time.time()

#
try:
    path=a_star(graph, start, dest, True)#calculate path
    print("Path is",path, "\n\n")
except:
    print("ERROR !!CHECK THE NAME OF THE INTRODUCED CITIES")
friendMeetCity(path)
t2 = time.time()
print(t2 - t1)