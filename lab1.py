#!/usr/bin/python

import sys
import random
import numpy as np
import chart

keys = ['--gen-sigm', '--gen-points', '--error', '--no-error', '--c']

def func(x,t):
    return t[0]+t[1]*x[0]+t[2]*x[0]**2+t[3]*x[1]+t[4]*x[1]**2

def e(m,s):
    return random.normalvariate(m,s)

def getS(u):
    s = sum(u) / len(u)
    u_s = [ (e - s)**2 for e in u]
    return sum(u_s)/(len(u_s)-1)

def help():
    print 'Error, usage: '+sys.argv[0]+' <key1> <key2> <file name>'
    print 'Keys:'
    print keys[0]+' -for generation sigma (key1)'
    print keys[1]+' -for generation points (key1)'
    print keys[2]+' -with error (key2)'
    print keys[3]+' -no error (key2)'
    print keys[4]+' -get chart'

if __name__ == '__main__':
    if len(sys.argv) < 4:
        if len(sys.argv) > 2:
            if sys.argv[1] != keys[4] or sys.argv[2] not in [keys[2],keys[3]]:
                help()
                sys.exit()
        else:
            help()
            sys.exit()
    elif not (sys.argv[1] in [keys[0], keys[1]] and sys.argv[2] in [keys[2],keys[3]]):
        help()
        sys.exit()
    if (sys.argv[1] != keys[4]):
        filename = sys.argv[3]
        f_out = open(filename, 'w')
        if not f_out:
            print 'Error, can\'t create file'
    x_d = [-1.0, 1.0]
    t = [0.5, 1, 0.01, 0.01, -1]
    h = 0.25
    s = 0.0835923427734
    m = 0
    x1 = x_d[0]
    x2 = x_d[0]
    resultsxyz = [[],[],[]]
    while(x1 <= x_d[1]):
        while(x2 <= x_d[1]):
            resultsxyz[0].append(x1)
            resultsxyz[1].append(x2)
            if sys.argv[2] == keys[2]:
                resultsxyz[2].append(func([x1,x2],t) + e(m, s))
            else:
                resultsxyz[2].append(func([x1,x2],t))
            x2 = x2 + h
        x1 = x1 + h
        x2 = x_d[0]
    if (sys.argv[1] != keys[4]):
        if keys[0] == sys.argv[1]:
            f_out.write(str(getS(resultsxyz[2])*0.15))
            f_out.write('\n')
        elif keys[1] == sys.argv[1]:
            for i in range(len(resultsxyz[0])):
                f_out.write(str(resultsxyz[0][i])+'\t'+str(resultsxyz[1][i])+'\t'+str(resultsxyz[2][i])+'\n')
        f_out.close()

    chart.draw3D(resultsxyz)