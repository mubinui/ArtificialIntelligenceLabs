import  re
import Graph as g
f = open("LevelTwoText.txt","r")
txt = f.read()

blist = re.split("\s",txt)

vartics =int(blist[0])
max_con = int(blist[1])


graph = g.Graph(vartics)

for i in range(2,(max_con*2)+2,2):
    u = blist[i]
    v = blist[i+1]
    graph.addEdge(int(u),int(v))

x_Lina_position = int(blist[len(blist)-3])
p_Nora_position = int(blist[len(blist)-2])
q_Lara_position = int(blist[len(blist)-1])

Nora_moves = graph.BFS(p_Nora_position,x_Lina_position)
Lara_moves = graph.BFS(q_Lara_position,x_Lina_position)
print(Nora_moves)
print(Lara_moves)

if Nora_moves < Lara_moves:
    print("Nora is the winner")
else:
    print("Lara is the winner")
