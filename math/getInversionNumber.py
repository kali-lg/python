#!/usr/bin/python
#coding:utf-8

def getVersionNumber(num):

    i = j = m = 0
    while(i < len(num)):
        j = i + 1
        while (j < len(num)):
            if (num[i] > num[j]):
                m = m + 1
            j = j + 1
        i = i + 1
    return m 


num = raw_input('please input your number:');

print getVersionNumber(num)
