#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

x = np.linspace(0, 2*np.pi, 100)

ax.plot(x, np.sin(x), 'k-')
ax.set_xlabel('angle (rad)')
ax.set_ylabel('amplitude')

plt.annotate("Line2D", (np.pi/3, np.sqrt(3)/2),
             xycoords="data",
             xytext=(10, -50), textcoords="offset points",
             arrowprops=dict(arrowstyle="->"),
             color='r')

plt.annotate("right spine", (1, 0.8),
             xycoords="axes fraction",
             xytext=(0.8, 0.8), textcoords="axes fraction",
             arrowprops=dict(arrowstyle="->", relpos=(0,0.5)),
             color='r')

plt.annotate("x-tick", (2, -0.95),
             xycoords="data",
             xytext=(-10, 20), textcoords="offset points",
             arrowprops=dict(arrowstyle="->"),
             color='r')

plt.annotate("y-label", (0.05, 0.4),
             xycoords="figure fraction",
             xytext=(0.05, 0.2), 
             textcoords="figure fraction",
             arrowprops=dict(arrowstyle="->", relpos=(0.5,0.5)),
             ha='center',
             color='r')

plt.figtext(0.98, 0.98, "Figure", color='r', ha='right', va='top')
plt.text(0.95, 0.95, 'Axes', color='r', va='top', ha='right',
         transform=ax.transAxes)

plt.savefig('figures/mpl_axes.svg', transparent=True)
