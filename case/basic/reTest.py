
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

pagename = '2006-02-13-第26版：产经\u3000汽车.pdf'
print(re.sub('\s','',pagename))
#2006-02-13-第26版：产经汽车.pdf
pagename = '2006-02-13-第33版：商业\r\n\u3000\u3000新知新管理.pdf'
print(re.sub('\s','',pagename))
#2006-02-13-第33版：商业新知新管理.pdf