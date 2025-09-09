import queue_class
import StackDS
class Graph:
    def __init__(self,nodes):
        self.nodes=nodes
        self.adjacency_list=[[]for i in range(nodes)]
        print (self.adjacency_list)

    def add_edge(self,node1,node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)
        print(self.adjacency_list)

    def BFS_distance (self,s):
        visited=[]
        distance=[-1 for i in range(self.nodes)]
        queue=queue_class.Queue(self.nodes)
        distance[s]=0
        visited.append(s)
        queue.enqueue(s)
        while not queue.isEmpty():
            node=queue.dequeue() 
            for i in self.adjacency_list[node]:
                if i not in visited:
                    distance[i]=distance[node]+1
                    queue.enqueue(i)
                    visited.append(i)
        print(visited)
        print(distance)


g=Graph(6)  
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,4)
g.add_edge(1,3)
g.add_edge(1,5) 
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,5)
g.BFS_distance(5)