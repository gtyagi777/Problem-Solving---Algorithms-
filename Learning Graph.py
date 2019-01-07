<<<<<<< HEAD
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

g = Graph()
g.addEdge('a1','b1')
g.addEdge('a1','b3')
g.addEdge('a2','b2')
g.addEdge('a2','b4')
g.addEdge('a3','b1')
g.addEdge('a3','b3')
g.addEdge('a4','b2')
g.addEdge('a4','b4')

g.addEdge('b1','c1')
g.addEdge('b1','c2')
g.addEdge('b2','c1')
g.addEdge('b2','c2')
g.addEdge('b3','c3')
g.addEdge('b3','c4')
g.addEdge('b4','c3')
g.addEdge('b4','c4')
=======
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

g = Graph()
g.addEdge('a1','b1')
g.addEdge('a1','b3')
g.addEdge('a2','b2')
g.addEdge('a2','b4')
g.addEdge('a3','b1')
g.addEdge('a3','b3')
g.addEdge('a4','b2')
g.addEdge('a4','b4')

g.addEdge('b1','c1')
g.addEdge('b1','c2')
g.addEdge('b2','c1')
g.addEdge('b2','c2')
g.addEdge('b3','c3')
g.addEdge('b3','c4')
g.addEdge('b4','c3')
g.addEdge('b4','c4')
>>>>>>> 34dcdbaf7606329ea73cdb976296a4aeaa79cb79
