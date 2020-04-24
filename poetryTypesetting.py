'''
本程序无法识别诗的标题
文本文件中诗的内容不能包含空格回车
'''
import os
import random
import comtypes.client
import chardet
fname = input('''请输入您需要排版的古诗的文件名（包含后缀）
并将该文件与本程序放在同一文件夹：''')
f = open(os.path.dirname(os.path.abspath(__file__)) + "\\{}".format(fname)) 
poetry = f.read()
f.close()
#读取关闭文件
Punctuation = ['，','。','？']
#通过标点记录换行
wordnumber = 0
#总字数（汉字加标点，不是字符数）
linenumber = 0
#诗的行数
n = 0
for i in poetry:
    if i in Punctuation:
        print(i)
        linenumber+=1
        wordnumber+=1
    else:
        print(i,end='')
        wordnumber+=1
#逐字读取古诗并记录总字数与行数
NumofSentence = int(wordnumber/linenumber)
#计算每一行的字数
for j in range(NumofSentence):
    print()
    for k in range((linenumber-1),-1,-1):
        print(poetry[k*NumofSentence+j],end='')
#输出(linenumber-1)行到第一行的第j个字，每一列的字输出完成换行