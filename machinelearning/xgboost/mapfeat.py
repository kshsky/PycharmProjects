'''
1）帽形（cap-shape）：钟形=b，圆锥形=c，凸形=x，平面=f，把手形=k，凹陷=S
2）帽面（cap-surface）：纤维状=f，凹槽状=g，鳞片状=y，光滑=s。
3）帽颜色（cap-color）：棕色=n，浅黄色=b，肉桂色=c，灰色=g，绿色=r，粉红色=p，紫色=u，红色=e，白色=w，黄色=y。
4）创伤（bruises）：创伤=t，no=f。
5）气味（odor）：杏仁=a，茴香=l，石灰=c，腥味=y，臭味=f，霉味=m，无=n，刺鼻=p，辣=s。
6）菌褶附属物（gill-attachment:）：附着=a，下降=d，自由=f，缺口=n。
7）菌褶间距（gill-spacing）：紧密=c，拥挤=w，远隔=d。
8）菌褶大小（gill-size）：宽=b，窄=n。
9）菌褶颜色（gill-color）：黑色=k，棕色=n，浅黄色=b，巧克力色=h，灰色=g，绿色=r，橙色=o，粉红色=p，紫色=u，红色=e，白色=w，黄色=y。
10）茎形（stalk-shape）：扩大=e，锥形=t。
11）茎根（stalk-root）：球根=b，棒状=c，杯状=u，均等的=e，根状菌索=z，扎根=r，缺省=？。
12）环上茎面（stalk-surface-above-ring）：纤维状=f，鳞片状=y，丝状=k，光滑=s。
13）环下茎面（stalk-surface-below-ring）：纤维状=f，鳞片状=y，丝状=k，光滑=s。
14）环上茎颜色（stalk-color-above-ring）：棕色=n，浅黄色=b，黄棕色=c，灰色=g，橙色=o，粉红色=p，红色=e，白色=w，黄色=y。
15）环下茎颜色（stalk-color-below-ring）：棕色=n，浅黄色=b，黄棕色=c，灰色=g，橙色=o，粉红色=p，红色=e，白色=w，黄色=y。
16）菌幕类型（veil-type）：部分=p，普遍=u。
17）菌幕颜色（veil-color）：棕色=n，橙色=o，白色=w，黄色=y。
18）环数量（ring-number）：没有=n，一个=o，两个=t。
19）环类型（ring-type）：蛛网状=c，消散状=e，喇叭形=f，大规模的=l，无=n，悬垂的=p，覆盖=s，环带=z。
20）孢子显现颜色（spore-print-color）：黑色=k，棕色=n，蓝色=b，巧克力色=h，绿色=r，橙色=o，紫色=u，白色=w，黄色=y。
21）种群（population）：丰富=a，聚集=c，众多=n，分散=s，个别=v，单独=y。
22）栖息地（habitat）：草地=g，树叶=l，草甸=m，路上=p，城市=u，荒地=w，树林=d。
23）class：label字段，有可食用（edible）和有毒性（poisonous）两个取值。



agaricus-lepiota.data——蘑菇数据文件；
agaricus-lepiota.fmap——字段名称映射文件；
agaricus-lepiota.names——蘑菇数据集描述文件；
mapfeat.py——数据集特征值预处理；
mknfold.py——划分数据集；
mushroom.conf——模型配置文件；
runexp.sh——运行脚本。
'''
#数据预处理，处理成LibSVM格式的文件，直接运行即可
#产生两个文件：datafile/featmap.txt，datafile/agaricus.txt
def loadfmap( fname ):
   fmap = {}
   nmap = {}
   for l in open( fname ):
        # 以空字符（空格、换行、制表符等）为分割符分割一行
        arr = l.split()
        # 解析每行中的特征名称、取值等
        # idx为初始特征索引，ftype为初始特征名称，content为该特征取值说明
        if arr[0].find('.') != -1:
            idx = int( arr[0].strip('.') )
            assert idx not in fmap
            fmap[ idx ] = {}
            ftype = arr[1].strip(':')
            content = arr[2]
        else:
            content = arr[0]
        # 解析取值说明
        # fmap是为特征的每个取值分配一个唯一标示的索引，nmap为处理后的新特征重新命名
        for it in content.split(','):
            if it.strip() == '':
                continue
            k , v = it.split('=')
            fmap[ idx ][ v ] = len(nmap) + 1
            nmap[ len(nmap) ] = ftype+'='+k
   return fmap, nmap


def write_nmap( fo, nmap ):
    for i in range( len(nmap) ):
        fo.write('%d\t%s\ti\n' % (i, nmap[i]) )

# start here
# 解析特征描述文件
fmap, nmap = loadfmap( 'datafile/agaricus-lepiota.fmap' )
# 保存处理后的新特征索引和名称的映射
fo = open( 'dataFile/featmap.txt', 'w' )
write_nmap( fo, nmap )
fo.close()

# 通过新特征索引处理原始数据，生成转化后的数据
fo = open( 'dataFile/agaricus.txt', 'w' )
for l in open( 'dataFile/agaricus-lepiota.data' ):
    arr = l.split(',')
    # 蘑菇分类为p（有毒）时，label为1，否则为0
    if arr[0] == 'p':
        fo.write('1')
    else:
        assert arr[0] == 'e'
        fo.write('0')
    # 若特征存在某取值，则该取值对应的新特征取值为1
    for i in range( 1,len(arr) ):
        fo.write( ' %d:1' % fmap[i][arr[i].strip()] )
    fo.write('\n')

fo.close()