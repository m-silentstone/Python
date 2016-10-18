# -*- coding: utf-8 -*-
import url_manager,html_downloader,html_parser,html_outputer
startPage="https://www.guazi.com/ty/buy/b5e11h6i3l2z16/"
maxTry=1000
targetCount=50
titleKeyWords=[u"思域",u"速腾",u"卡罗拉",u"马自达6",u"明锐",u"轩逸",u"科鲁兹"]

class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self,root_url):
        _targetCount=targetCount
        _maxTry=maxTry
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            if _targetCount<=0 or _maxTry<=0:
                break
            try:
                new_url=self.urls.get_new_url()
                if new_url is None:
                    print "There is no new url"
                    break
                html_content=self.downloader.download(new_url)
                new_urls,new_dataUrls=self.parser.parse_findUrls(new_url,html_content)
                if len(new_urls)>0:
                    self.urls.add_new_urls(new_urls)
                if len(new_dataUrls)>0:
                    for dataUrl in new_dataUrls:
                        if self.urls.dataUrl_is_exist(dataUrl):
                            continue
                        _maxTry-=1
                        print "%d:%s" %(_maxTry,dataUrl)
                        self.urls.dataUrl_add(dataUrl)
                        dataUrl_content=self.downloader.download(dataUrl)
                        new_data=self.parser.parse_parseData(dataUrl,dataUrl_content,titleKeyWords)
                        if new_data is not None:
                            print "targetCount %d:%s" % (_targetCount,dataUrl)
                            _targetCount-=1
                            self.outputer.collect_data(new_data)
                        if _targetCount<=0 or _maxTry<=0:
                            break
            except:
                print "targetCount %d:craw failed" %_targetCount
        self.outputer.output_html()

if __name__=="__main__":
    root_url=startPage
    objSpider=SpiderMain()
    objSpider.craw(root_url)

