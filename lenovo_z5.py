from urllib import request
import json
import re

class Spider():
    url1='https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv2789&productId=7621213&score=1&sortType=5&page='
    url3='&pageSize=10&isShadowSku=0&fold=1'
    u1 = "D:\\PycharmProject\\spider\\comment\\comment_page_"
    u3 = ".json"

    def __get_content(self,page):
        txt = open("D:\\PycharmProject\\spider\\comment\\allcomment.txt", "w")
        txt.close()

        for i in range(0,page):
            full_web_url = self.url1 + str(i) + self.url3
            r = request.urlopen(full_web_url)
            html = r.read()
            html = str(html,encoding='GBK')
            json_data = json.loads(html[26:-2])

            if json_data['comments'] == [] :
                break
            full_local_url = self.u1 + str(i + 1) + self.u3
            file = open(full_local_url, "w")
            file.write("Comment Page "+str(i+1)+"\n")
            file.close()
            index = 0
            for a in json_data['comments']:
                index += 1
                file = open(full_local_url, "a")
                file.write(str(index)+"\n"+a['content']+"\n\n")
                txt = open("D:\\PycharmProject\\spider\\comment\\allcomment.txt", "a")
                txt.write(a['content'])
            file.close()

        txt.close()



    def run(self):
        self.__get_content(40)

spider=Spider()
spider.run()


