import graphviz
# file = "datafile/dotFile/eg1.dot"
# file = "datafile/dotFile/expressway.dot"
# file = "datafile/dotFile/tcpip0.dot"
# file = "datafile/dotFile/tcpip.dot"
# file = "datafile/dotFile/datastruct.dot"
# file = "datafile/dotFile/datastruct1.dot"
file = "dataFile/dotFile/transport.dot"
# file = "datafile/dotFile/qiantao.dot"
# file = "datafile/dotFile/cell2.dot"
# file = "datafile/dotFile/family1.dot"
# file = "datafile/dotFile/family2.dot"
# file = "datafile/dotFile/dataFlow.dot"

with open(file,'r',encoding='utf-8') as f:
    dot_graph = f.read()

dot=graphviz.Source(dot_graph)
dot.view()
