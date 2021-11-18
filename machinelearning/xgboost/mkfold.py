#!/usr/bin/python
#
# D:\ProgramData\Anaconda3\python.exe D:/program/PycharmProjects/machinelearning/xgboost/mkfold.py dataFile/agaricus.txt 1
#划分数据集为训练集和测试集，
# 需要读取文件dataFile/agaricus.txt
#运行，添加参数  dataFile/agaricus.txt 1
# dataFile/agaricus.txt 1
import sys
import random

if len(sys.argv) < 2:
    print ('Usage:<filename> <k> [nfold = 5]')
    exit(0)

random.seed( 10 )

k = int( sys.argv[2] )
if len(sys.argv) > 3:
    nfold = int( sys.argv[3] )
else:
    nfold = 5

fi = open( sys.argv[1], 'r' )
ftr = open( sys.argv[1]+'.train1', 'w' )
fte = open( sys.argv[1]+'.test1', 'w' )
for l in fi:
    if random.randint( 1 , nfold ) == k:
        fte.write( l )
    else:
        ftr.write( l )

fi.close()
ftr.close()
fte.close()
