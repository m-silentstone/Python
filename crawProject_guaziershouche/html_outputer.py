# -*- coding: utf-8 -*-
def cmpDatas(x,y):
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
            fout.write("<b>%s</b><br>"%data['url'].encode("utf-8"))
            fout.write("%s<br>"%data['title'].encode("utf-8"))
            fout.write("%f万<br>"%data['price'])
            fout.write("出厂：%s<br>"%data['birthday'].encode("utf-8"))
            fout.write("里程：%s<br>"%data['distance'].encode("utf-8"))
            fout.write("变速箱：%s<br>"%data['amtmode'].encode("utf-8"))
            fout.write("迁入标准：%s<br>"%data['intype'].encode("utf-8"))
            fout.write("上牌地：%s<br>"%data['city'].encode("utf-8"))
            fout.write("<img src=%s><br><hr>"%data['img_src'].encode("utf-8"))
            fout.write("</div>")
        fout.write("</div>")
        fout.write("</body>")
        fout.write("</html>")
    
    