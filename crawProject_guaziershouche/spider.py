# -*- coding: utf-8 -*-
import url_manager,html_downloader,html_parser,html_outputer
class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count=0
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                if new_url is None:
                    print "There is no new url"
                    break
                print "count %d:%s" % (count+1,new_url)
                
                html_content=self.downloader.download(new_url)
                #print html_content
                new_urls,new_data=self.parser.parse(new_url,html_content)
                self.urls.add_new_urls(new_urls)
                if new_data is not None:
                    count+=1
                    self.outputer.collect_data(new_data)
                
            except:
                print "count %d:craw failed" %count
            if count>=20:
                break
        #print "count:%d"%count
        self.outputer.output_html()

if __name__=="__main__":
    #print "start!"
    root_url="https://www.guazi.com/www/buy/b0e10h6i7u5l3/"
    objSpider=SpiderMain()
    objSpider.craw(root_url)

