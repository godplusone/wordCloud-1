# coding:utf-8

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pdb

def generate_wordcloud(text):
    '''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
    # 设置显示方式
    d=path.dirname(__file__)
    # alice_mask = np.array(Image.open(path.join(d, "Images//alice_mask.png")))
    font_path=path.join(d,"font//msyh.ttf")
    # stopwords = set(STOPWORDS)
    stopwords = {"Learning","via", "Network", "Neural Network", "for", "and", "with", "in", "of", "the", "to", "by", "An", "A", "on", "Method", "Non", "from"}
    
    wc = WordCloud(width=800, height=400, background_color="white",# 设置背景颜色
           max_words=1000, # 词云显示的最大词数  
           # mask=alice_mask,# 设置背景图片       
           stopwords=stopwords, # 设置停用词
           font_path=font_path, # 兼容中文字体，不然中文会显示乱码
                  )

    pdb.set_trace()
    dit = {}
    text_split = text.split(" ")
    for word in text_split:
        if word in dit and word not in stopwords:
            dit[word] += 1
        else:
            dit[word] = 1
    pdb.set_trace()

    def foc(i):
        return i[1]
     
    lt = list(dit.items())
    lt.sort(key=foc)
    lt.reverse()
    for i in lt[:100]:
        print(i)
    pdb.set_trace()

    # 生成词云 
    wc.generate(text)

    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, "Images/haha.png"))

    # 显示图像
    # plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    # plt.axis("off")# 关掉图像的坐标
    # plt.show()

