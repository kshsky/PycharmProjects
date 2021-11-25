seasons={'spring':'春','summer':'夏','autumn':'秋','winter':'冬'}
print(seasons)

# 使用enumerate，获取索引和key
for i,j in enumerate(seasons):
	print(i+1,j,seasons[j])

#使用 dictionary[key]
for i in seasons:
	print(i,seasons[i])

#使用dictionary.get(i)
for i in seasons:
	print(i,seasons.get(i))

#dictionary.items()获取键值对
for item in seasons.items():
	print('items()->',item)

#dictionary.keys()获取所有keys
for i in seasons.keys():
	print(i,seasons[i])

#dictionary.values()获取所有values
for i in seasons.values():
	print(i)

seasons.update({3:'spring'})

for i in seasons.keys():
    print(i,seasons.get(i))