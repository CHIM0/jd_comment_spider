import get_list     #获取商品列表
import get_data     #获取商品评论
import word_cloud   #处理评论并输出结果

#获取商品id列表
goods_list_url = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exprice_M2800L4499&sort=sort_rank_asc&trans=1&JL=2_1_0#J_crumbsBar'
goods_list_spider = get_list.goods_list_Spider(goods_list_url)
goods_list = goods_list_spider.go()

# 整合txt
txt = open("D:\\PycharmProject\\spider\\comment\\allcomment.txt","w")
txt.close()
txt = open("D:\\PycharmProject\\spider\\comment\\allcomment.txt","a")
for index in range(0,10):
    comment_data_spider = get_data.Spider(goods_list[index])
    comment_data_spider.run()
    txt_temp = open("D:\\PycharmProject\\spider\\comment\\"+goods_list[index]+"\\allcomment.txt","r")
    r = txt_temp.read()
    txt.write(r)
txt.close()

#评论分词 生成词频统计表txt 生成基于词频的词云图 生成词频统计条形图
word_cloud_maker =word_cloud.word_cloud_maker()
word_cloud_maker.run()
