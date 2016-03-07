#!/usr/bin/python

import os

fd = os.open('imooc-os.txt',os.O_CREAT | os.O_RDWR)

n = os.write(fd, "imooc-os")

L = os.lseek(fd, 0, os.SEEK_SET)
#print L
print os.read(fd, 5)

os.close(fd)
