# -*- coding: utf-8 -*-
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.dataUrls = set()

    def add_new_url(self,new_url):
        if new_url is None:
            return
        if new_url not in self.new_urls and new_url not in self.old_urls:
        	self.new_urls.add(new_url)

    def add_new_urls(self,new_urls):
    	if new_urls is None or len(new_urls)==0:
    	    return
        for url in new_urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls)>0

    def get_new_url(self):
        if len(self.new_urls)==0:
            return None
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url
    
    def dataUrl_add(self,new_url):
        if new_url is None:
            return
        if new_url not in self.dataUrls:
            self.dataUrls.add(new_url)

    def dataUrl_is_exist(self,new_url):
        if new_url in self.dataUrls:
            return True
        else:
            return False
    