# Undirected unweighted unidirected graph implementation using adjacentList method



class Graph:
    def __init__(self) -> None:
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertix(self,node):
        if node in self.adjacentList:
            print("Dubplicate vertex not allowed")
            return
        self.adjacentList[node] = []
        self.numberOfNodes+=1
    def addEdge(self,node1,node2):
        if node1 not in self.adjacentList or node2 in self.adjacentList.get(node1):
            
            print("Node1 either not in adjacentList or Dublicates edge found")
            return
   
        self.adjacentList.get(node1).append(node2)
        self.adjacentList.get(node2).append(node1)

    def showConnections(self):
        allNodes = self.adjacentList.keys()
        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = ""
            for vertex in nodeConnections:
                connections+=vertex+" "
            print(node+"--->"+connections)    

g = Graph()

g.addVertix('0')
g.addVertix('1')
g.addVertix('2')
g.addVertix('3')
g.addVertix('4')
g.addVertix('5')
g.addVertix('6')


g.addEdge('3','1')
g.addEdge('3','4')
g.addEdge('4','2')
g.addEdge('4','5')
g.addEdge('1','2')
g.addEdge('1','0')
g.addEdge('0','2')
g.addEdge('6','5')


g.showConnections()