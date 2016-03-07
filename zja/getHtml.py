#!/usr/bin/python

from bs4 import BeautifulSoup

finput = open("index.html", "r")

html_doc = finput.read()
soup = BeautifulSoup(html_doc, "html.parser", from_encoding='utf-8')
#html_code = soup.find("div", class_='link').find_all("option")
html_code = soup.find("div", class_="menu_up").find_all("a")
html_code_1 = soup.find_all("div", class_="menu_list")
f = open("output_1.html", 'w')

f.write("<meta charset='utf-8'>")
for content in html_code:
    try:
        #f.write(content['value'])
        f.write(content.get_text().encode("utf-8"))
        f.write("</br>")
       # f.write("%s, %s" % (content['value'], content.get_text().uncode('utf-8')))
    except:
        print "value"
#    print content

f.write("xxxxxxxxx</br>")
for x in html_code_1:
    f.write('xx</br>')
    myxcontent = x.find_all("a")
    for myx in myxcontent:
        f.write(myx.get_text().encode("utf-8")) 
        f.write("</br>")

finput.close()
f.close()
