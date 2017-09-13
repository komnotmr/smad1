#!/usr/bin/python

import numpy as np
import sys
import chart
import func
import temp_lab_2 as TG
import globals as G

keys = ['--optimizeT', '--optimizeS', '--gen-points']

def F(x):
    return G.n(x,TG.T)

def genX(filename):
    # init list of lists
    with open(filename,'r') as f:
        txt = f.readlines()
    X = [ [] for i in range(len(txt)) ]
    for i in range(len(txt)):
        x = txt[i].split('\t')
        X[i].append(1) #1
        X[i].append(float(x[0])) #x0
        X[i].append(float(x[0])**2) #x0**2
        X[i].append(float(x[1])) #x1
        X[i].append(float(x[1])**2) #x1**2
    return np.array(X)

def genY(filename):
    with open(filename,'r') as f:
        txt = f.readlines()
    Y = []
    for i in range(len(txt)):
        Y.append(float(txt[i].split('\t')[2]))
    return np.array(Y)

def optimizeT(filename):
    Xdefault = genX(filename)
    Xtranspose = Xdefault.transpose()
    Xres = np.linalg.inv(np.dot(Xtranspose,Xdefault))
    Xres = np.dot(Xres,Xtranspose)
    Ydefault = genY(filename)
    Result = np.dot(Xres, Ydefault)
    print 'Theta = {R}'.format(R = Result)
    with open('./temp_lab_2.py', 'r') as f:
        txt = f.readlines()
    with open('./temp_lab_2.py', 'w') as f:
        for i in range(len(txt)-1):
            f.write(txt[i])
        f.write('T = [')
        for i in range(len(Result)):
            if i == len(Result) - 1:
                f.write('{R}]'.format(R = Result[i]))
            else:
                f.write('{R}, '.format(R = Result[i]))

def optimizeS():
    m = len(func.S)
    yk = []
    with open('./points.log') as f1:
        S = f1.readlines()
    s = [s.strip() for s in S]
    for l in s:
        x1 = float(l.split('\t')[0])
        x2 = float(l.split('\t')[1])
        y = float(l.split('\t')[2])
        yk.append(y - F([x1,x2]))
    e = [x*x for x in yk]
    R = sum(e)
    D = len(s) - m
    print 'n-m={d}'.format(d=D)
    return R / D


def gen_points():
    resultsxyz = [[],[],[]]
    while(G.x1 <= G.x_d[1]):
        while(G.x2 <= G.x_d[1]):
            resultsxyz[0].append(G.x1)
            resultsxyz[1].append(G.x2)    
            resultsxyz[2].append(F([G.x1,G.x2]))
            G.x2 = G.x2 + G.h
        G.x1 = G.x1 + G.h
        G.x2 = G.x_d[0]

    f_out = open('opt_out_points.log', 'w')

    for i in range(len(resultsxyz[0])):
        f_out.write(str(resultsxyz[0][i])+'\t'+str(resultsxyz[1][i])+'\t'+str(resultsxyz[2][i])+'\n')
    f_out.close()
    
    chart.draw3D(resultsxyz)

def help():
    print 'Error, usage: '+sys.argv[0]+' keys'
    print 'Keys:'
    print keys[0]+' -generate function'
    print keys[1]+' -find T params'
    print keys[2]+' -generate points'
    print keys[3]+' -find Sigm'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit()
    
    if sys.argv[1] == keys[2]:
        gen_points()
    elif sys.argv[1] == keys[0]:
        optimizeT('./points.log')
    elif sys.argv[1] == keys[1]:
        res = optimizeS()
        print '{res}/{sigm}={r}'.format(res=res, sigm= G.sygm, r=res/G.sygm)
    

    
   

