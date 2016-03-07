#coding:utf8

class HtmlOutputer(object):
    def __init__(self):
         self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data) 
    
    def output_html(self):
        '''
        for data in self.datas:
            print data["title"].encode("utf-8"), "\n"
        '''        
        fout = open("output.html", "w") 
        
        fout.write("<html><meta charset='utf-8'><body><table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data["title"].encode('utf-8'))
            fout.write("<tr>")

        fout.write("</table></body></html>")
        
        fout.close()
       
