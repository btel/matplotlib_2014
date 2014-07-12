#!/usr/bin/env python
#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

titleprops = dict(family='monospace', color='maroon')

plt.figure(figsize=(5,3.5))
plt.subplots_adjust(hspace=0.5)

plt.subplot(231, frameon=False)
plt.title('plot', fontdict=titleprops)
plt.plot([2.5, 1, 3, 2], color='k')
plt.xticks([])
plt.yticks([])

plt.subplot(232, axisbg='none')
plt.title('scatter', fontdict=titleprops)
plt.scatter([1, 3, 2], [1, 2, 3], [100,100,200], facecolor='none')
plt.xticks([])
plt.yticks([])

plt.subplot(233, frameon=False)
plt.title('bar', fontdict=titleprops)
plt.bar([1, 3, 2], [1,2,3], facecolor='none', linewidth=2,
        clip_on=False)
plt.xticks([])
plt.yticks([])

ax=plt.subplot(234, polar=True)
plt.title('polar', fontdict=titleprops)
theta= np.linspace(0, 2*np.pi, 15)
r = np.ones(len(theta), dtype=np.float)
r[::2] = 2.
ax.plot(theta, r, 'k-')
ax.set_rmax(3)
plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)

plt.subplot(235, axisbg='none')
plt.title('contour', fontdict=titleprops)
XX, YY = np.mgrid[-2:2:10j, -2:2:10j]
ZZ = -XX**2+YY**2
cs = plt.contour(XX, YY, ZZ, 5, colors='k')
plt.clabel(cs, [-1.5, 0, 1.5], fontsize=8)
plt.xticks([])
plt.yticks([])


import matplotlib.cm as cm
X = 10*np.random.rand(3,3)
plt.subplot(236)
plt.title('imshow', fontdict=titleprops)
plt.imshow(X, cmap=cm.gray, interpolation='nearest')
plt.xticks([])
plt.yticks([])
plt.savefig('figures/plot_types.svg', transparent=True)
