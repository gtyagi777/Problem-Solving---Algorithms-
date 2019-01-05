# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:34:42 2018

@author: tyagi
"""

from PureGraph import Graph


def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = []
  vertQueue.insert(0,start)
  while len(vertQueue) > 0:
    currentVert = vertQueue.pop()
    print(currentVert.getId(), end = ",")
    for nbr in currentVert.getConnections():
        if (nbr.getColor() == 'white'):
            nbr.setColor('gray')
            nbr.setDistance(currentVert.getDistance() + 1)
            nbr.setPred(currentVert)
            vertQueue.insert(0,nbr)
    currentVert.setColor('black')
        
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 


print ("Following is Breadth First Traversal"
				" (starting from vertex 2)") 
bfs(g,g.getVertex(2))               
                
                
    
