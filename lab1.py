#!/usr/bin/python

import sys  # for keys
import random # for generate e
import chart # draw 3D graph
import globals as G# consist sigma, limitations and other

keys = ['--gen-sigm', '--gen-points', '--error', '--no-error', '--c']

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
            if sys.argv[1] not in [keys[4], keys[0]] or sys.argv[2] not in [keys[2],keys[3]]:
                help()
                sys.exit()
        else:
            help()
            sys.exit()
    elif not (sys.argv[1] in [keys[0], keys[1]] and sys.argv[2] in [keys[2],keys[3]]):
        help()
        sys.exit()
    if (sys.argv[1] != keys[4] and sys.argv[1] != keys[0]):
        filename = sys.argv[3]
        f_out = open(filename, 'w')
        if not f_out:
            print 'Error, can\'t create file'
    resultsxyz = [[],[],[]]
    while(G.x1 <= G.x_d[1]):
        while(G.x2 <= G.x_d[1]):
            resultsxyz[0].append(G.x1)
            resultsxyz[1].append(G.x2)
            if sys.argv[2] == keys[2]:
                resultsxyz[2].append(G.n([G.x1,G.x2], G.t) + e(G.m, G.sygm))
            else:
                resultsxyz[2].append(G.n([G.x1,G.x2], G.t))
            G.x2 = G.x2 + G.h
        G.x1 = G.x1 + G.h
        G.x2 = G.x_d[0]
    if (sys.argv[1] != keys[4]):
        if keys[0] == sys.argv[1]:
            with open('./globals.py') as f:
                text = f.read()
                text = text.split('\n')
                text = text[0:len(text)-1]
            f = open('./globals.py', 'w')
            for t in text:
                f.write(t+'\n')
            f.write('sygm = {s}'.format(s = getS(resultsxyz[2])*G.p ))
            f.close()
        elif keys[1] == sys.argv[1]:
            for i in range(len(resultsxyz[0])):
                f_out.write(str(resultsxyz[0][i])+'\t'+str(resultsxyz[1][i])+'\t'+str(resultsxyz[2][i])+'\n')
            f_out.close()
    chart.draw3D(resultsxyz)