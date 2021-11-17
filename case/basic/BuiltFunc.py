series_str='春夏秋冬'
series_tuple=('春','夏','秋','冬')
series_list=['春','夏','秋','冬']

series_dict={1:'春',2:'夏',3:'秋',4:'冬'}
series_set={'春','夏','秋','冬'}


print(series_str)
print(series_list)
print(series_tuple)
print(series_dict)
print(series_set)

print('===list()===')
print(list(series_str))
print(list(series_list))
print(list(series_tuple))
print(list(series_dict))
print(list(series_set))

print('===str()===')
print(str(series_str))
print(str(series_list))
print(str(series_tuple))
print(str(series_dict))
print(str(series_set))

print('===sum()===')
# print(sum(series_str))
# print(sum(series_list))
# print(sum(series_tuple))
print(sum(series_dict))
# print(sum(series_set))

print('===sorted()===')
print(sorted(series_str))
print(sorted(series_list))
print(sorted(series_tuple))
print(sorted(series_dict))
print(sorted(series_set))

print('===reversed()===')
series_str_reversed=reversed(series_str)
series_list_reversed=reversed(series_list)
series_tuple_reversed=reversed(series_tuple)

print(series_str)
print(series_list)
print(series_tuple)

print(list(series_str_reversed))
print(list(series_list_reversed))
print(list(series_tuple_reversed))

print('扩展切片',series_str[::-1])
print('扩展切片',series_tuple[::-1])
print('扩展切片',series_list[::-1])
# print('扩展切片',series_dict[::-1])
# print('扩展切片',series_set[::-1])

for index,item in enumerate(series_str):
	print(index+1,item)
for index,item in enumerate(series_list):
	print(index+1,item)
for index,item in enumerate(series_tuple):
	print(index+1,item)
for index,item in enumerate(series_dict):
	print(index+1,item,series_dict[item])
for index,item in enumerate(series_set):
	print(index+1,item)
