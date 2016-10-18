# -*- coding: utf-8 -*-
def cmpDatas(x,y):
        if x.get('birthday') is None or y.get('birthday') is None:
            return 0
        if x['birthday']<y['birthday']:
            return 1
        elif x['birthday']>y['birthday']:
            return -1
        else:
            return 0

class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    def collect_data(self,data):
        #print "collect_data in"
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        self.datas.sort(cmpDatas)
        fout=open("output.html",'w')
        fout.write("<html>")
        fout.write("<meta charset=\"UTF-8\">")
        fout.write("<body>")
        fout.write("<div>")
        for data in self.datas:
            fout.write("<div>")
            if data.get('url') is not None:
                fout.write("<b>%s</b><br>"%data['url'].encode("utf-8"))
            if data.get('title') is not None:
                fout.write("%s<br>"%data['title'].encode("utf-8"))
            if data.get('price') is not None:
                fout.write("%f万<br>"%data['price'])
            if data.get('birthday') is not None:
                fout.write("出厂：%s<br>"%data['birthday'].encode("utf-8"))
            if data.get('distance') is not None:
                fout.write("里程：%s<br>"%data['distance'].encode("utf-8"))
            if data.get('amtmode') is not None:
                fout.write("变速箱：%s<br>"%data['amtmode'].encode("utf-8"))
            if data.get('intype') is not None:
                fout.write("迁入标准：%s<br>"%data['intype'].encode("utf-8"))
            if data.get('city') is not None:
                fout.write("上牌地：%s<br>"%data['city'].encode("utf-8"))
            if data.get('img_src') is not None:
                fout.write("<img src=%s><br><hr>"%data['img_src'].encode("utf-8"))
                fout.write("</div>")
        fout.write("</div>")
        fout.write("</body>")
        fout.write("</html>")
    
    