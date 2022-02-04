import graphviz
# file = "dataFile/dotFile/eg1.dot"
# file = "dataFile/dotFile/expressway.dot"
# file = "dataFile/dotFile/tcpip0.dot"
# file = "dataFile/dotFile/tcpip.dot"
# file = "dataFile/dotFile/datastruct.dot"
# file = "dataFile/dotFile/datastruct1.dot"
file = "dataFile/dotFile/transport.dot"
# file = "dataFile/dotFile/qiantao.dot"
# file = "dataFile/dotFile/cell2.dot"
# file = "dataFile/dotFile/family1.dot"
# file = "dataFile/dotFile/family2.dot"
# file = "dataFile/dotFile/dataFlow.dot"

with open(file,'r',encoding='utf-8') as f:
    dot_graph = f.read()

dot=graphviz.Source(dot_graph)
dot.view()
