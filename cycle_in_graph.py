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

    def is_cycle_utility(self,node,visited,parent):
        visited[node]=True
        for i in self.adjacency_list[node]:
            if not visited[i]:
                if self.is_cycle_utility(i,visited,node):
                    return True
            elif i != parent: 
                return True
        return False 

    def is_cycle(self):
        visited=[False for i in range(self.nodes)]
        for i in range(self.nodes):
            if not visited[i]:
                if self.is_cycle_utility(i,visited,-1):
                    return True
        return False
    


g=Graph(6)  
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)
#g.add_edge(1,2)
print(g.is_cycle())