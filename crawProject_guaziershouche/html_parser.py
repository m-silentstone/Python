# -*- coding: utf-8 -*-
import bs4,re,urlparse
class HtmlParser(object):
    def __init__(self):
        pass

    def _get_new_data(self,url,soup,titleKeyWords):
        #print "_get_new_data in"
        res_data={}
        res_data['url']=url
        title_node=None
        price_node=None
        birthday_node=None
        distance_node=None
        amt_node=None
        intype_node=None
        city_node=None

        title_node=soup.find('h1',class_="dt-titletype")
        if title_node is None:
            return None
        title=title_node.get_text()
        
        hit=False
        for keyWord in titleKeyWords:
            if title.find(keyWord)>=0:
                hit=True
                break
        if hit==False:
            return None

        if title_node is None:
            res_data['title']=""
        else:
            res_data['title']=title_node.get_text()

        price_node=soup.find('span',class_="fc-org pricestype")
        if price_node is not None:
            price_node=price_node.find('b',class_="f30 numtype")
        if price_node is None:
            res_data['price']=""
        else:
            price=float(price_node.get_text()[1:])
            res_data['price']=price
            
        birthday_node=soup.find('ul',class_="assort clearfix")
        if birthday_node is not None:
            birthday_node=birthday_node.find('li')
        if birthday_node is None:
            res_data['birthday']=""
        else:
            birthday=birthday_node.get_text()[:-4]
            res_data['birthday']=birthday

        if birthday_node is not None:
            distance_node=birthday_node.find_next_sibling("li")
            res_data['distance']=distance_node.get_text()[:-2]
        else:
            res_data['distance']=""

        if distance_node is not None:
            amt_node=distance_node.find_next_sibling("li")
            res_data['amtmode']=amt_node.get_text()[:-3]
        else:
            res_data['amtmode']=""

        if amt_node is not None:
            intype_node=amt_node.find_next_sibling("li")
            res_data['intype']=intype_node.get_text()[:-4]
        else:
            res_data['intype']=""

        if intype_node is not None:
            city_node=intype_node.find_next_sibling("li")
            res_data['city']=city_node.get_text()[:-3]
        else:
            res_data['city']=""

        img_node=soup.find('ul',class_="dt-thumb-img clearfix")
        if img_node is not None:
            img_node=img_node.find('img')
        if img_node is None:
            res_data['img_src']=""
        else:
            src=img_node['src']
            atIndex=src.find('@')
            if atIndex > 0:
                src=src[0:atIndex]
            res_data['img_src']=src
        return res_data

    def parse_findUrls(self,url,html_content):
        if url is None or html_content is None:
            return None
        soup=bs4.BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')    
        new_urls=set()
        new_dataUrls=set()
        pattern=r"/ty/buy/[a-z0-9]+/$"
        if re.search(pattern,url):
            links=soup.find_all('a',href=re.compile(pattern))
            for link in links:
                new_url=link['href']
                new_full_url=urlparse.urljoin(url,new_url)
                new_urls.add(new_full_url)
            links1=soup.find_all('a',href=re.compile(r"/[a-z]+/\d+x\.htm$"))
            for link in links1:
                new_url=link['href']
                new_full_url=urlparse.urljoin(url,new_url)
                new_dataUrls.add(new_full_url)
        return new_urls,new_dataUrls

    def parse_parseData(self,url,html_content,titleKeyWords):
        if url is None or html_content is None:
            return None
        soup=bs4.BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
        return self._get_new_data(url,soup,titleKeyWords)