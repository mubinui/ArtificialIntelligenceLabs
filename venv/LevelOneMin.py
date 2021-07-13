# First Level
import  re
import Graph as g
f = open("LevelOne.txt","r")
txt = f.read()

blist = re.split("\s",txt)

vartics =int(blist[0])
max_con = int(blist[1])


graph = g.Graph(vartics)

for i in range(2,(max_con*2)+2,2):
    u = blist[i]
    v = blist[i+1]
    graph.addEdge(int(u),int(v))

level = graph.BFS(0,int(blist[len(blist)-1]))
print(level)












