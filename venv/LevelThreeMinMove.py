import  re
import Graph as g
f = open("LevelThree.txt","r")
txt = f.read()

blist = re.split("\s",txt)

vartics =int(blist[0])
max_con = int(blist[1])


graph = g.Graph(vartics)

for i in range(2,(max_con*2)+2,2):
    u = blist[i]
    v = blist[i+1]
    graph.addEdgeOD(int(u),int(v))

x_Lina_position = int(blist[len(blist)-7])
k = int(blist[len(blist)-6])


x = graph.BFSLevelThree(0,9)
print(x,"k1")
x1 = graph.BFSLevelThree(1,9)
print(x1,"k2")
x2 = graph.BFSLevelThree(3,9)
print(x2,"k3")
x3 = graph.BFSLevelThree(5,9)
print(x3,"k4")
x4 = graph.BFSLevelThree(7,9)
print(x4,"k5")




    
    