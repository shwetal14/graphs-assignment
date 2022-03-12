#!/usr/bin/env python
# coding: utf-8

# In[ ]:







   # 1. Breadth First Traversal for a Graph



graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] 
queue = []     

def bfs(visited, graph, node): 
    visited.append(node)
    queue.append(node)

    while queue:          
        m = queue.pop(0) 
        print (m, end = " ") 

    for neighbour in graph[m]:
        if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, '5')   




   # 2. Depth First Traversal for a Graph



graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() 

def dfs(visited, graph, node): 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, '5')




   # 3. Count the number of nodes at given level in a tree using BFS
    
    
      
class Graph: 
  
    def __init__(self, V): 
        self.V = V  
        self.adj = [[] for i in range(V)] 
      
    def addEdge(self, u, v): 
        
        self.adj[u].append(v) 
      
    def countPaths(self, s, d): 
          
        visited = [False] * self.V 
      
        pathCount = [0]  
        self.countPathsUtil(s, d, visited, pathCount)  
        return pathCount[0] 
       
    def countPathsUtil(self, u, d,  
                       visited, pathCount): 
        visited[u] = True
      
        if (u == d): 
            pathCount[0] += 1
       
        else: 
              
            i = 0
            while i < len(self.adj[u]): 
                if (not visited[self.adj[u][i]]):  
                    self.countPathsUtil(self.adj[u][i], d,  
                                        visited, pathCount) 
                i += 1
      
        visited[u] = False
  
 if __name__ == '__main__': 
    
    g = Graph(4)  
    g.addEdge(0, 1)  
    g.addEdge(0, 2)  
    g.addEdge(0, 3)  
    g.addEdge(2, 0)  
    g.addEdge(2, 1)  
    g.addEdge(1, 3)  
  
    s = 2
    d = 3
    print(g.countPaths(s, d)) 
  
    

    
  # 4. Count number of trees in a forest




def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
 
 def DFSUtil(u, adj, visited):
    visited[u] = True
    for i in range(len(adj[u])):
        if (visited[adj[u][i]] == False):
            DFSUtil(adj[u][i], adj, visited)
 
 def countTrees(adj, V):
    visited = [False] * V
    res = 0
    for u in range(V):
        if (visited[u] == False):
            DFSUtil(u, adj, visited)
            res += 1
    return res
 
if __name__ == '__main__':
 
    V = 5
    adj = [[] for i in range(V)]
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 3, 4)
    print(countTrees(adj, V))




  # 5. Detect Cycle in a Directed Graph


from collections import defaultdict

class Graph():
   
   def __init__(self, vertices):
         self.graph = defaultdict(list)
            self.V = vertices
            
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def isCyclicUtil(self, v, visited, recStack):
           visited[v] = True
            recStack[v] = True
      
      for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
            return True
      
      recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        
             for node in range(self.V):
                if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
            return False
g = Graph(4)
    


    
    
    #  Implement n-Queen’s Problem



def isSafe(mat, r, c):
 
    
    for i in range(r):
        if mat[i][c] == 'Q':
            return False
 
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1
 
    (i, j) = (r, c)
    while i >= 0 and j < len(mat):
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1
 
    return True
 
 
 def printSolution(mat):
    for r in mat:
        print(str(r).replace(',', '').replace('\'', ''))
    print()
 
 
def nQueen(mat, r):
 
    # if `N` queens are placed successfully, print the solution
    if r == len(mat):
        printSolution(mat)
        return
 
    for i in range(len(mat)):
 
        if isSafe(mat, r, i):
            mat[r][i] = 'Q'
 
            nQueen(mat, r + 1)
 
            mat[r][i] = '–'
 
 
if __name__ == '__main__':
 
    # `N × N` chessboard
    N = 8
    mat = [['–' for x in range(N)] for y in range(N)]
    nQueen(mat, 0)
 

