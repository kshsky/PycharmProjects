from graphviz import Digraph
grap_g = Digraph("G",format="pdf")

sub_a = Digraph(comment="output",
                graph_attr={"style":'filled',"color":'green'},
                node_attr={"style":"filled","color":"red"},
                rankdir = "LR")
sub_a.node("a_0","a_0",shape='square')
sub_a.node("a_1","a_1",shape='box')
sub_a.node("a_1","a_1",shape='box')
sub_a.node("a_cdot1","a_cdot1",fillcolor='yellow',shape='diamond')
sub_a.node("a_i","a_i",shape='rect')
sub_a.node("a_cdot2","a_cdot2",shape='rect')
sub_a.node("a_m","a_m",shape='rect')

sub_b = Digraph(comment="input",
                node_attr={"style":'filled',"color":'green'})
sub_b.node("b_0","b_0")
sub_b.node("b_1","b_1")
sub_b.node("b_2","b_2")
sub_b.node("b_cdot1","b_cdot1")
sub_b.node("b_j","b_j")
sub_b.node("b_cdot2","b_cdot2")
sub_b.node("b_n","b_n")

# grap_g.node("start", label="start",shape="Mdiamond")
# grap_g.node("end", label="end", shape="Mdiamond")

#合并两个子图
grap_g.subgraph(sub_a)
grap_g.subgraph(sub_b)

grap_g.edge("a_i","b_0")
grap_g.edge("a_i","b_1")
grap_g.edge("a_i","b_2")
grap_g.edge("a_i","b_cdot1")
grap_g.edge("a_i","b_j")
grap_g.edge("a_i","b_cdot2")
grap_g.edge("a_i","b_n")

print(grap_g.source)
grap_g.render('dataFile/transformOR', view=True)


