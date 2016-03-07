#!/usr/bin/python
# coding:utf8

from bs4 import BeautifulSoup

f = open('index.html', "r")
html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding = 'utf-8')

links = soup.find_all("a")

#for link in links:
#    print link.name, link["href"], link.get_text()

link_code = soup.find("a")
print link_code["href"]

link_code = soup.find("a", href=re.compile(r"ill"))
link_code = soup.find("a", class_="")


f.close()

