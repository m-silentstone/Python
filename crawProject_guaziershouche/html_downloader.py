# -*- coding: utf-8 -*-
import urllib2
class HtmlDownloader(object):
    def __init__(self):
        pass

    def download(self,url):
    	#print "download in"
        if url is None:
            return None
        response=urllib2.urlopen(url)
        #print "urlopen finished"
        if response.getcode()!=200:
            #print "urlopen code not 200"
            return None
        #print "urlopen code 200,successfully"
        return response.read()
