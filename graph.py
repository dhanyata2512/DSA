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

    def BFS (self,s):
        visited=[]
        queue=queue_class.Queue(self.nodes)
        visited.append(s)
        queue.enqueue(s)
        while not queue.isEmpty():
            node=queue.dequeue() 
            for i in self.adjacency_list[node]:
                if i not in visited:
                    queue.enqueue(i)
                    visited.append(i)
        print(visited)

    def DFS (self,start):
        visted=[]  
        stack=StackDS.Stack(self.nodes)
        stack.push(start)
        while not stack.is_empty() :
            item=stack.pop()
            visted.append(item)
            for i in self.adjacency_list[item]:
                if i not in visted and not stack.is_in(i):
                    stack.push(i)
        print(visted)            

            


g=Graph(6)  
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,4)
#g.add_edge(1,3)
g.add_edge(1,5) 
g.add_edge(2,3)
#g.add_edge(2,4)
#g.add_edge(3,5)
g.BFS(0)
g.DFS(1)
