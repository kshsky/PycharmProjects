from graphviz import Digraph
grap_g = Digraph("G",format="pdf")

sub_g0 = Digraph(comment="process1",graph_attr={"style":'filled',"color":'green'},node_attr={"style":"filled","color":"red"})
sub_g0.node("a0","a0",shape='square')
sub_g0.node("a1","a1",shape='box')
sub_g0.node("a2","a2",fillcolor='yellow',shape='diamond')
sub_g0.node("a3","a3",shape='rect')

sub_g0.edge("a0","a1")
sub_g0.edge("a1","a2")
sub_g0.edge("a2","a3")
sub_g0.edge("a3", "a0")

sub_g1 = Digraph(comment="process1",node_attr={"style":'filled',"color":'green'})
sub_g1.node("B","b0")
sub_g1.node("C","b1",shape='box')
sub_g1.node(name="D",label="b2|b22|4",shape='record')
sub_g1.node("E","b3")
sub_g1.edges(["BC","CD","DE"])

grap_g.node("start", label="start",shape="Mdiamond")
grap_g.node("end", label="end", shape="Mdiamond")

#合并两个子图
grap_g.subgraph(sub_g0)
grap_g.subgraph(sub_g1)

grap_g.edge("start","a0")
grap_g.edge("start","B")

grap_g.edge("a1","E")
grap_g.edge("D","a3")

grap_g.edge("a3","end")
grap_g.edge("E","end")
print(grap_g.source)
grap_g.render('dataFile/transformOR', view=True)


