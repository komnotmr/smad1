#!/usr/bin/python

x_d = [-1.0, 1.0] # [xmin,xmax] 
t = [0.5, 1, 0.01, 0.01, -1] # default theta
h = 0.25 # step
x1 = x_d[0] # while var 1
x2 = x_d[0] # while var 2
p = 0.15 # % from w
m = 0 # math ozhydanie
def n(x,t): # model 
    return t[0]+t[1]*x[0]+t[2]*x[0]**2+t[3]*x[1]+t[4]*x[1]**2

# !!! sygm shoud be last line in this file!
sygm = 0.0835923427734