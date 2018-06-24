#https://list.jd.com/list.html?cat=9987,653,655&ev=exprice_M1000L1699&sort=sort_dredisprice_desc&trans=1&JL=2_1_0#J_crumbsBar
#

from urllib import request
import re

class goods_list_Spider():
    root_pattern = '<div class="gl-i-wrap j-sku-item" data-sku="([\s\S]*?)"'

    def __init__(self,url1):
        self.url = url1

    def __fetch_content(self):
        r = request.urlopen(self.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        result = re.findall(goods_list_Spider.root_pattern,htmls)
        return result


    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        return anchors
