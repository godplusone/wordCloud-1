# coding:utf-8

from os import path
import chnSegment
import plotWordcloud
import pdb

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


if __name__=='__main__':

    # # 读取文件
    # d = path.dirname(__file__)
    # #  text = open(path.join(d, 'doc//十九大报告全文.txt')).read()
    # # text = open(path.join(d,'doc//alice.txt'), 'r', encoding='utf-8').read()

    # text = open(path.join(d,'doc//nips2020paperlist.txt'), 'r', encoding='utf-8').read()
    

    # # 若是中文文本，则先进行分词操作
    # # text=chnSegment.word_segment(text)
    
    # # 生成词云
    # plotWordcloud.generate_wordcloud(text)


    d = path.dirname(__file__)
    f = open(path.join(d,'doc/nips2020paperlist.txt'), 'r', encoding='utf-8')
    paper = f.readlines()
    text = ''
    for i in range(len(paper)):
        if i % 2 ==0:
            line = paper[i].split("\n")[0]
            print(line)
            text+=line


    # 若是中文文本，则先进行分词操作
    # text=chnSegment.word_segment(text)
    
    # 生成词云
    plotWordcloud.generate_wordcloud(text)
