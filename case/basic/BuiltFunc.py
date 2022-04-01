# -*- coding:utf-8 -*-
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


print('=================')
d = {'第一集 Part2':1,'第二集 Part3':3,'第一集 Part2':1,'第一集 Part3':3,'第一集 Part1':10,'第四集 Part5':111,'第四集 Part2':13}
aa= sorted(d.keys())
print(d)

# a = [' 第四集 Part2 ', ' 第二集 Part6 ', ' 第三集 Part6 ', ' 第三集 Part4 ', ' 第三集 Part5 ', ' 第四集 Part1 ', ' 第三集 Part3 ', ' 第三集 Part1 ', ' 第三集 Part2 ', ' 第二集 Part5', ' 第一集 Part6 ', ' 第二集 Part1 ', ' 第二集 Part2 ', ' 第二集 Part3 ', ' 第十集 Part5 ', ' 第一集 Part5 ', ' 第二集 Part4 ', ' 第十集 Part4 ', ' 第九集 Part4 ', ' 第十集 Part2 ', ' 第九集 Part3 ', ' 第十集 Part3 ', ' 第九集 Part2 ', ' 第九集 Part1 ', ' 第十集 Part1 ', ' 第八集 Part6 ', ' 第八集 Part4 ', ' 第八集 Part5 ', ' 第七集 Part1 ', ' 第八集 Part3 ', ' 第六集 Part4 ', ' 第七集 Part4 ', ' 第八集 Part1 ', ' 第五集 Part4 ', ' 第八集 Part2 ', ' 第六集 Part2 ', ' 第六集 Part3 ', ' 第五集 Part3 ', ' 第五集 Part5 ', ' 第四集Part5 ', ' 第五集 Part1 ', ' 第七集 Part3 ', ' 第四集 Part4 ', ' 第五集 Part2 ', ' 第四集 Part6 ', ' 第一集 Part1 ', ' 第一集 Part3 ', ' 第一集 Part2 ', ' 第一集 Part4 ', ' 第六集 Part1 ', ' 第七集 Part2 ', ' 第四集 Part3 ']
b=['第一集 Part2', '第二集 Part2', '第一集 Part5', '第一集 Part4', '第一集 Part3', '第一集 Part6', '第一集 Part1', '第二集 Part3', '第二集 Part1', '第二集 Part4', '第二集 Part6', '第三集 Part2', '第三集 Part6', '第二集 Part5', '第三集 Part3', '第三集 Part1', '第三集 Part5', '第七集 Part4', '第六集 Part2', '第六集 Part4', '第七集 Part2', '第七集 Part1', '第十集 Part5', '第十集 Part4', '第九集 Part3', '第九集 Part4', '第十集 Part3', '第八集 Part6', '第十集 Part1', '第十集 Part2', '第八集 Part5', '第九集 Part1', '第九集 Part2', '第八集 Part4', '第七集 Part3', '第五集 Part5', '第六集 Part3', '第八集 Part2', '第八集 Part3', '第五集 Part1', '第五集 Part4', '第八集 Part1', '第五集 Part3', '第四集 Part3', '第四集 Part4', '第五集 Part2', '第四集 Part6', '第六集 Part1', '第三集 Part4', '第四集 Part2', '第四集 Part5', '第四集 Part1']

print(sorted(b))

