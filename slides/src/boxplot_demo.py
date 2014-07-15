#!/usr/bin/python

#
# Example boxplot code
#

import numpy as np
import matplotlib.pyplot as plt

# fake up some data
np.random.seed(1234)
spread= np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(2) * 100 + 100
flier_low = np.random.rand(2) * -100
data = np.concatenate((spread, center, flier_high, flier_low), 0)

fig = plt.figure(figsize=(6,7))
fig.subplots_adjust(left=0,right=1, top=1, bottom=0)
ax = fig.add_subplot(111, frameon=False)

box_artists = plt.boxplot(data, notch=True)

plt.setp(box_artists['fliers'], mec='k')
plt.setp(box_artists['whiskers'],ls ='-', color='k')
plt.setp(box_artists['boxes'], color='k')
plt.setp(box_artists['medians'], color='k')

plt.yticks([])
plt.xticks([])
plt.xlim((-0.5, 2.5))
plt.ylim((-25, 175))

# 161., 94., 65., 54., 50.

plt.annotate("outliers", (1.05, 161.),
             xycoords='data',
             xytext=(1.2, 161.),
             textcoords='data',
             arrowprops=dict(arrowstyle="->", relpos=(0.5,0.5)),
             va='center',
             color='r')
plt.annotate("75th percentile +\n1.5x inter-quartile\n        range", (1.08, 95.),
             xycoords='data',
             xytext=(1.2, 95.),
             textcoords='data',
             arrowprops=dict(arrowstyle="->", relpos=(0.5,0.5)),
             va='center',
             color='r')

plt.annotate("75th\npercentile", (0.9, 65.),
             xycoords='data',
             xytext=(0.7, 65.),
             textcoords='data',
             arrowprops=dict(arrowstyle="->", relpos=(0.5,0.5)),
             va='center',
             ha='right',
             color='r')

plt.annotate("95% confidence\ninterval", (1.08, 54.),
             xycoords='data',
             xytext=(1.2, 54.),
             textcoords='data',
             arrowprops=dict(arrowstyle="->", relpos=(0.5,0.5)),
             va='center',
             color='r')

plt.annotate("median", (0.925, 50.),
             xycoords='data',
             xytext=(0.7, 50.),
             textcoords='data',
             arrowprops=dict(arrowstyle="->", relpos=(0.5,0.5)),
             va='center',
             ha='right',
             color='r')

plt.savefig("figures/boxplot_demo.svg", transparent=True)
