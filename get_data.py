from urllib import request
import json
import os

class Spider():
    url1='https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv2789&productId='
    url2=''
    url3='&score=0&sortType=5&page='
    url4='&pageSize=10&isShadowSku=0&fold=1'
    u1 = "D:\\PycharmProject\\spider\\comment\\"
    u3 = '\\comment_page_'
    u4 = ".json"

    def __init__(self,good_id):
        self.url2 = good_id


    def __get_content(self,page):
        if not os.path.exists("D:\\PycharmProject\\spider\\comment\\"+ self.url2):
            os.makedirs("D:\\PycharmProject\\spider\\comment\\"+ self.url2)
        txt = open("D:\\PycharmProject\\spider\\comment\\"+ self.url2 +"\\allcomment.txt", "w")
        txt.close()

        for i in range(0,page):
            full_web_url = self.url1+self.url2+self.url3+str(i) + self.url4
            r = request.urlopen(full_web_url)
            html = r.read()
            html = str(html,encoding='GBK')
            json_data = json.loads(html[26:-2])

            if json_data['comments'] == [] :
                break
            full_local_url = self.u1 + self.url2 + self.u3 + str(i + 1) + self.u4
            file = open(full_local_url, "w")
            file.write("Comment Page "+str(i+1)+"\n")
            file.close()
            index = 0
            for a in json_data['comments']:
                index += 1
                file = open(full_local_url, "a")
                file.write(str(index)+"\n"+a['content']+"\n\n")
                txt = open("D:\\PycharmProject\\spider\\comment\\"+ self.url2 +"\\allcomment.txt", "a")
                txt.write(a['content'])
            file.close()

        txt.close()



    def run(self):
        self.__get_content(10)



