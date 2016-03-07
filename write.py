#!/usr/bin/python

f = open("imooc.txt","w")

s = ["Nothing is true, everything is premitted.\n","The quieter you become,the more you are able to hear.\n"]
f.writelines(s)

print f.fileno(), f.mode, f.encoding

f.close()

print "ok"

