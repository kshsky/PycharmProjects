import graphviz
from graphviz import Digraph

#digraph digraphName {}
dot = Digraph(name='digraphName',comment='graphviz000', format="pdf")
# dot = Digraph(format="pdf")

# 添加圆点A,A的标签是Dot A
# dot.node('A', 'Dot A')
dot.node(name='A', label='Dot A',color='red')

# 添加圆点 B, B的标签是Dot B
dot.node('B', 'Dot B')
# dot.view()

# 添加圆点 C, C的标签是Dot C
dot.node('C', 'Dot C')

# D
dot.node(name='D', label = 'diamond D',color='orange')

#
dot.edges(['AB', 'AC', 'AB'])


# 从B指向C,
dot.edge('B', 'C', 'B-C')
dot.edge('A','D',label='diamond',color='orange')

# 获取DOT source源码的字符串形式
print(dot.source)
# // The Test Table
# digraph {
# 	A [label="Dot A" color=red]
# 	B [label="Dot B"]
# 	C [label="Dot C"]
# 	D [label="diamond D" color=orange]
# 	A -> B
# 	A -> C
# 	A -> B
# 	B -> C [label="B-c"]
# 	A -> D [label=diamond color=orange]
# }

# 保存source到文件，并提供Graphviz引擎
#render(filename=None, directory=None, view=False, cleanup=False)
# 参数分别为文件名、文件保存路径、是否用默认程序打开渲染效果、是否在渲染后删除源文件
# 有时需要用绝对地址
dot.render('dataFile/g0', view=True)