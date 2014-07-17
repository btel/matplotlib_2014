#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from sklearn import cluster
from scipy import spatial

if __name__ == "__main__":
    centers = np.array([[2, 3], [3, 2], [2.8, 3]])
    data = np.concatenate([np.random.randn(100,2)*0.1+ c[None,:] for c in centers], axis=0)
    labels = np.repeat([1,2,3], 100)
    ax=  plt.subplot(111)
    plt.scatter(data[:, 0], data[:,1], c=labels, edgecolor="none")

    vor = spatial.Voronoi(centers)
    spatial.voronoi_plot_2d(vor, ax)
    plt.plot(centers[:, 0], centers[:, 1], 'o', mfc='white')
    plt.xlim([1.6, 3.4])
    plt.ylim([1.6, 3.4])
    ax.set_axis_off()
    plt.savefig('figures/kmeans_demo.svg', transparent=True)
    #main

