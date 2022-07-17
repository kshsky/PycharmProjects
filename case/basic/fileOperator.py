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
#移动文件
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

def changeFileName(path):
    os.chdir(path)
    file = os.listdir(path)
    for i in file:

        l=i.index('(')
        r=i.rindex('.')
        # new = i.replace('一','1').replace('一','1').replace('二','2').replace('三','3').replace('四','4').replace('五','5').replace('六','6').replace('七','7').replace('八','8')
        new = i[:l]+i[r:]
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

        else:
            continue
        # os.rename(i,new)

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

def deleteParticularFile(path):
    import os
    os.chdir(path)
    for root,dir,file in os.walk(path):

        for i in file:
            if i.find('mobi')!=-1 :
                absi=os.path.join(root,i)
                print(absi)
                os.remove(absi)
        #
        # if len(dir)>0:
        #     for i in dir:
        #         absi=os.path.join(root,i)
        #         if len(os.listdir(absi))==0:
        #             print(i)
        #             os.rmdir(absi)






path=r'H:\zlibrary\5000+epub+mobi+pdf'
# path=r'F:\temp\book-zlibrary'
# deleteParticularFile(path)

# movefile(input,output)
# movefile(output,topath)
# emptyDir(input)
# emptyDir(output)


calibre=r'C:\Users\87754\AppData\Local\calibre-cache\ev2\f'
emptyDir(calibre)
#

# path = r'F:\BOOK_word\01-刑部\大型电视专题片《永远在路上》'
path = r'D:\Program Files\jj-Download\《项目管理概论》2022春 全67p'
# changeFileName(path)


path = r'F:\PDF\newspaper\中国县域经济报\2019'
# checkName(path)