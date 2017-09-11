#!/usr/bin/python

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw3D(resultsxyz):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    n = 100
    for c, m, zlow, zhigh in [('r', '.', 0, 0), ('r', '.', 0, 0)]:
        xs = resultsxyz[0]
        ys = resultsxyz[1]
        zs = resultsxyz[2]
        ax.plot_trisurf(resultsxyz[0], resultsxyz[1], resultsxyz[2], linewidth=0.2, antialiased=True)
        ax.scatter(xs, ys, zs, c=c)

    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Y')
    plt.show()