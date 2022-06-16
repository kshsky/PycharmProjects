import os
import shutil
import path

input=r'F:\temp\Library-epub\input'
output=r'F:\temp\Library-epub\output'
topath=r'G:\zlibrary\1-zlibrary'
os.chdir(input)
files = os.listdir(os.getcwd())
for i in files:
    # print(i)
    pass
def movefile(input,output):
    for root,dirs,file in os.walk(input):
        if len(file)!=0:
            for i in file:
                if i.find('epub')!=-1:
                    shutil.move(root+'/'+i,output+'/'+i)
                if i.find('mobi')!=-1:
                    shutil.move(root+'/'+i,output+'/'+i)
                if i.find('pdf')!=-1:
                    shutil.move(root+'/'+i,output+'/'+i)
    print('\n\n move successfully ...')

def delAll(path):
    shutil.rmtree(path)

def emptyDir(path):
    os.chdir(path)
    files = os.listdir(os.getcwd())
    for i in files:
        print(i)
        if os.path.isdir(i):
            shutil.rmtree(i)
        if os.path.isfile(i):
            os.remove(i)
    print('>>> empty dir OK ... ')


# movefile(input,output)
# movefile(output,topath)
# emptyDir(input)
# emptyDir(output)


calibre=r'C:\Users\87754\AppData\Local\calibre-cache\ev2\f'
# emptyDir(calibre)



def changeFileName(path):
    os.chdir(path)
    file = os.listdir(path)
    for i in file:
        l=i.index('御赐')
        new = i[l:]
        os.rename(i,new)

def changeFileName2(path):
    os.chdir(path)
    file = os.listdir(path)
    for i in file:
        if i.find('2021-04-29-33') != -1:
            new = i.replace('2021-04-29-33','2021-05-03-33').replace('1615','1627')
            # new = new.replace('-25-','-22-')
            print('>>>>>',i,new)
            os.rename(i, new)
        # if i.find('16154') != -1:
        #     new = i.replace('16154','1616')
        #     print(i,new)
        #     os.rename(i, new)
        # if i.find('16132') != -1:
        #     new = i.replace('16132','1613')
        #     print(i,new)
        #     os.rename(i, new)
        if i.find('1453') != -1:
            new = i.replace('1453','1503')
            print(i,new)
            os.rename(i, new)
        if i.find('1454') != -1:
            new = i.replace('1454','1504')
            print(i,new)
            os.rename(i, new)
        else:
            continue
        # os.rename(i,new)

path = r'F:\PDF\newspaper\中国县域经济报\2022'
# changeFileName2(path)

def checkName(path):
    os.chdir(path)
    file = os.listdir(path)
    issue=0
    k=0
    issuelist=[]
    for i in file:
        if issue != i[:4]:
            k+=1
            issue =i[:4]
            yearissue=i[i.rindex('-')-2:i.rindex('-')]
            issuelist.append(str(issue))
            if int(yearissue)%10==0:
                print('-------------')
            print(k,yearissue,issue,i[i.index('-')+1:i.index('-')+11],i)
        else:
            continue
    print(issuelist)

path = r'F:\PDF\newspaper\中国县域经济报\2019'
checkName(path)