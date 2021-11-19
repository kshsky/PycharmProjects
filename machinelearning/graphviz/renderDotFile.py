#渲染dot文件
from graphviz import Source
path = 'dataFile/breastCancerTree.dot'
s = Source.from_file(path,format='png')
#默认format='pdf'
# s = Source.from_file(path,format='pdf')
s.view()