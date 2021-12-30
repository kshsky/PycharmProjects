
def replaceSpecialCharForFile(ss):
    #
    # windows下文件名中不能含有：\ /: * ? " < > | 英文的这些字符

    # : * ? | ->-
    # \ / -> .
    # " < >  -> '
    char_list =['\\','/','|','<','>',':','：','*','?','？','\'','"']
    newstr = ''
    for i in char_list:
        if ss.find(i) !=-1:
            print(ss)
            newstr=ss.replace(i,'-')
            print(ss)
    return ss

import re
def validateTitle(title):

    #替换英文字符
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线

    #替换中文字符
    rstr2=r"[：？'‘“”]"
    result = re.sub(rstr2, "-", new_title)  # 替换为下划线

    return result
print(replaceSpecialCharForFile('卫哲：谈谈新消费视野和打法'))
print(validateTitle('卫哲：谈谈新消费视野和打法'))


print('你是"好人"是的"'.replace('"','\\"'))


import matplotlib.pyplot as plt
y1=[]
y2=[]
x=[]
for i in range(1,800):
    x.append(i)
    y1.append(240-0.5*i)
    y2.append(300-i)

plt.plot(x,y1,c='cornflowerblue')
plt.plot(x,y2,c='peru')
plt.axvline(200,c='limegreen')
plt.xlim(0,500)
plt.ylim(0,300)
plt.text(121,181,'(120,180)')
plt.text(201,140,'(200,140)')
plt.text(201,100,'(200,100)')
plt.show()