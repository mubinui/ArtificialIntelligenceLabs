from collections import defaultdict
class Graph:
    def __init__(self,vertics):
        self.V = vertics
        self.graph = defaultdict(list)



    def addEdge(self,src,dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)
        
    def addEdgeOD(self,src,dest):
        self.graph[src].append(dest)

    #bfs edited
    def BFS (self,start, end ):
        visited = [False] * self.V
        dist = [None]*self.V
        
        counter = 0

        queue = []

        queue.append(start)
        visited[start] = True
        dist[start] = 0
        
        while queue : 
            start = queue.pop(0) 
            # From queue we alwast dequeue the first 
            print(start,end="->")
            child_counter = 0
        
            for i in self.graph[start] :
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    dist[i]=dist[start]+1
            
            
        print()
        return dist[end]


    

    def DFSUtil(self,ver,end, explored,counter):
        explored.add(ver)
        counter = counter+1
        print(ver,end='->')

        for nb in self.graph[ver]:
            if nb not in explored:
                self.DFSUtil(nb, end, explored, counter)
            if end in explored:
                break



    def DFS(self,start,end):
        counter = 0
        explored = set()
        self.DFSUtil(start,end,explored,counter)



    def printGraph(self):
        for i in range(self.V):
            print("[",i,"]",end='=>')
            for j in self.graph[i]:
                print('{',j,'}', end="->")
            print()

        


    def BFSLevelThree(self,start,end):
        visited = [False] * self.V
        dist = [None] * self.V

        counter = 0

        queue = []

        queue.append(start)
        visited[start] = True
        dist[start] = 0

        while queue:
            start = queue.pop(0)
            # From queue we alwast dequeue the first
            print(start, end="->")
            child_counter = 0

            for i in self.graph[start]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    dist[i] = dist[start] + 1

        print()
        return dist[end]