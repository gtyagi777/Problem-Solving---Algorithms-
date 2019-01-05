class Graph:
    
    node_list = []
    
    v = 0
    
    def add_edge(self,v,w):
        self.node_list[v[1]].append(w)
        self.node_list[w[1]].append(v)
        
    def adj(self,v):
        return self.node_list[v]
    
    def __init__(self,v):
        self.node_list = [[] for x in range(v+1)]
        self.v = v
 
    
 
# Write your code here
n,m,k = map(int,"3 3 2".split())
val = list(map(int,"7 9 8".split()))
 
g = Graph(n)
for i in range(m):
    v,w = map(int,input().split())
    g.add_edge((val[v-1],v),(val[w-1],w))

for i in g.node_list:
    print(i)
    
for i in range(n):
    l = len(g.adj(i+1)) 
    if l >= k:
        g.adj(i+1).sort()
        print(str(g.adj(i+1)[l-k][1])+'\n')
    else:
       print('-1')