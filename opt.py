#!/usr/bin/python

from scipy.optimize import minimize
import sys
import chart
import func
import globals

keys = ['--gen-func', '--optimizeT', '--gen-points', '--optimizeS']

def f(t):
    return func.Z(t)
   
def F(t):
    s = func.S
    return s[0]  + s[1]*t[0] +s[2]*t[0]**2 +s[3]*t[1]+s[4]*t[1]**2

def gen_func():
    f2 = open('func.py', 'w')

    f2.write('#!/usr/bin/python\n\n')
    f2.write('def Z(t):\n')
    f2.write('  return 0 ')
    S = ''
    with open('./points.log') as f1:
        S = f1.readlines()
    s = [s.strip() for s in S]
    for z in s:
        x0 = z.split('\t')[0]
        x1 = z.split('\t')[1]
        y = z.split('\t')[2]
        f2.write(' + ({y} - (t[0] + {x0} * t[1] + {x0}**2*t[2] + {x1}*t[3] + {x1}**2*t[4]))**2 '.format(y = y, x0 = x0, x1 = x1))
    f2.close()

def optimizeT(T):
    res = minimize(f, T)
    print res
    print 'param T'
    r = [x for x in res.x]
    f2 = open('func.py', 'a')
    f2.write('\nS = [')
    for i in r:
        if i != r[len(r)-1]:
            f2.write(str(i)+',')
        else:
            f2.write(str(i)+']')
    f2.close()

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
    x_d = globals.G_x_d
    h = globals.G_h
    x1 = globals.G_x1
    x2 = globals.G_x2
    while(x1 <= x_d[1]):
        while(x2 <= x_d[1]):
            resultsxyz[0].append(x1)
            resultsxyz[1].append(x2)    
            resultsxyz[2].append(F([x1,x2]))
            x2 = x2 + h
        x1 = x1 + h
        x2 = x_d[0]

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
        gen_func()
    elif sys.argv[1] == keys[1]:
        optimizeT((0,0,0,0,0))
    elif sys.argv[1] == keys[3]:
        res = optimizeS()
        print '{res}/{sigm}={r}'.format(res=res, sigm= 0.0835923427734,r=res/0.0835923427734)
    

    
   

