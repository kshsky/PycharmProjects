import json

#json 其实就是字典
dict_data = {
  'name': '张三',
  'age': 25,
  'sex': '男'
}
print(type(dict_data))
print(dict_data['name'])
print(dict_data)
print(str(dict_data).encode('utf-8'))#utf-8 每个中文字符占3位
print(str(dict_data).encode('gbk'))#gbk 每个中文字符占2位

print('==============================')
#dumps 将字典变成字符串
#json.dumps(dict_data) 生成字符串json格式,默认使用ascii码
json_str_ascii= json.dumps(dict_data)
json_str= json.dumps(dict_data, ensure_ascii=False)

print(json_str)
print(json_str_ascii)

print(type(json_str))
print(type(json_str_ascii))

print('==============================')
#eval 将字符串变成 字典
json_dict= eval(json_str)
json_dict_ascii= eval(json_str_ascii)
print(type(json_dict))
print(type(json_dict_ascii))
print(json_dict)
print(json_dict)
print(json_dict['name'])
print(json_dict_ascii['name'])
print('==============================')

#loads 把字符串变成字典
json_ = json.loads(json_str)
json_ascii = json.loads(json_str_ascii)
print(type(json_))
print(type(json_ascii))
print(json_)
print(json_ascii)
print(json_['sex'])
print(json_dict_ascii['name'])
print('==============================')


#json.dump(dict_data) 把字典转成json格式字符串并存储在文件中
with open('datafile\json.txt','w+',encoding='utf8') as f:
    json.dump(dict_data, f, ensure_ascii=False)

#json.load() 从文件中读取json数据并转化成字典,只支持读取模式,默认是读取模式
with open('datafile\json.txt','r',encoding='utf8') as f:
    json_file =json.load(f)
print(json_file)