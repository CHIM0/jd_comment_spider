import re
import jieba
import pandas as pd
import numpy
from wordcloud import WordCloud,ImageColorGenerator,get_single_color_func
import matplotlib.pyplot as plt
import matplotlib
from os import path
from PIL import Image

def add_stopword(str1,stopwords):
    s = pd.Series({'stopword':str1})
    stopwords = stopwords.append(s, ignore_index=True)
    return stopwords


matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
file1 = open("D:\\PycharmProject\\spider\\comment\\allcomment.txt", 'r')
xt = file1.read()
pattern = re.compile(r'[\u4e00-\u9fa5]+')
filedata = re.findall(pattern, xt)
finaldata = ''.join(filedata)
file1.close()
#读取文件
file2 = open("D:\\PycharmProject\\spider\\comment\\allcomment1.txt", 'w')
file2.write(finaldata)
clear = jieba.cut(finaldata)
cleared = pd.DataFrame({'clear': list(clear)})
#print(clear)
stopwords = pd.read_csv("chineseStopWords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'], encoding='GBK')
#添加额外停止词
stopwords = add_stopword("手机",stopwords)
# print(str(stopwords))
cleared = cleared[~cleared.clear.isin(stopwords.stopword)]
#清洗数据
count_words=cleared.groupby(by=['clear'])['clear'].agg({"num": numpy.size})
count_words=count_words.reset_index().sort_values(by=["num"], ascending=False)

#词云展示
RGB_coloring =numpy.array(Image.open(path.join("RGB.png")))
image_colors = ImageColorGenerator(RGB_coloring)
wordcloud=WordCloud(color_func=get_single_color_func('red'),font_path="simhei.ttf",background_color="white",max_font_size=300,height=800,width=1000,random_state=None) #指定字体类型、字体大小和字体颜色
word_frequence = {x[0]:x[1] for x in count_words.head(400).values}
wordcloud=wordcloud.fit_words(word_frequence)
plt.imshow(wordcloud,interpolation="bilinear")
# plt.imshow(wordcloud.recolor(color_func=get_single_color_func('white')),interpolation="bilinear")
plt.axis("off")
plt.show()

#词频统计
file3 = open("D:\\PycharmProject\\spider\\comment\\word_counting.txt",'w')
file3.write("词频统计结果：\n")
file3.close()
file3 = open("D:\\PycharmProject\\spider\\comment\\word_counting.txt",'a')
for y in count_words.head(20).values:
    file3.write(str(y[0])+":"+str(y[1])+"\n")
file3.close()
