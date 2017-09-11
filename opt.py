#!/usr/bin/python

from scipy.optimize import minimize
import sys
import chart

def f(x):
    return (-1.69-x[0]-x[1])**2+(-0.94-x[0]-x[1]*0.5625)**2+(-0.75-x[0]-x[1]*0.0625)**2


'''
def help():
    print 'Error, usage: '+sys.argv[0]+' <key1> <filename>'
    print 'Keys:'
    print keys[0]+' -for generation sigma (key1)'
    print keys[1]+' -for generation points (key1)'
    print keys[2]+' -with error (key2)'
    print keys[3]+' -no error (key2)'
    print keys[4]+' -get chart'
'''
if __name__ == '__main__':
   # if len(sys.argv)  < 1:
    #    print 'error'
    T = (0.5, 0.5)
    res = minimize(f, T)
    print res
    print 'param T'
    print res.x
    resultsxyz = [[],[],[]]


