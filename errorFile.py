#!/usr/bin/python
try:
    with open("1.text") as f:
        print "in with f.read" , f.read()
except:
    print "error"
