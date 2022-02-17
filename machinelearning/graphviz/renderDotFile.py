#渲染dot文件
from graphviz import Source
# path = 'datafile/breastCancerTree.dot'
path = "dataFile/dotFile/family1.dot"
s = Source.from_file(path,format='png')
#默认format='pdf'
# s = Source.from_file(path,format='pdf')
s.view()