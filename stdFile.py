#!/usr/bin/python
'''
import sys

type(sys.stdin)
print sys.stdin.mode, sys.stdin.fileno()

a = raw_input("please input your word:\n")
print a

type(sys.stdout)
print sys.stdout.mode, sys.stdout.fileno()

sys.stdout.write("ok")

type(sys.stderr)
print sys.stderr.mode, sys.stderr.fileno()
sys.stderr.write("err")
'''

import sys

if __name__ == '__main__':
    print len(sys.argv)
    for arg in sys.argv:
        print arg
