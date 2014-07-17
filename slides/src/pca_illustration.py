#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(2, 200)

mixin_matrix = np.array([[4, 1], [2, 2]])
y = np.dot(mixin_matrix, x)

corr_mat = np.dot(y, y.T)/y.shape[1]

evals,evecs  = np.linalg.eig(corr_mat)

fig, axes = plt.subplots(2,2)

pvecs = evecs*np.sqrt(evals[None, :])
ax = axes[0,0]
ax.plot(y[0, :], y[1, :], 'k.')
ax.plot([0, pvecs[0, 0]], [0, pvecs[1,0]], lw=2, color='r')
ax.plot([0, pvecs[0, 1]], [0, pvecs[1,1]], lw=2, color='r')
def configure_spines():
    for sp in ['left', 'bottom']:
        ax.spines[sp].set_position(('data', 0))
    for sp in ['top', 'right']:
        ax.spines[sp].set_position(('data', 0))
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
configure_spines()
ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))

ax = axes[0, 1]
y_proj = np.dot(evecs.T, y) 
ax.plot(y_proj[0, :], y_proj[1, :], 'k.')
configure_spines()
ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))

ax = axes[1, 1]
W = evecs.dot(np.diag(1./np.sqrt(evals))).dot(evecs.T)
y_whitened = np.dot(W, y)
ax.plot(y_whitened[0, :], y_whitened[1, :], 'k.')
configure_spines()
ax.set_xlim((-3, 3))
ax.set_ylim((-3, 3))

# dimensionality reduction
ax = axes[1,0]
y_reduced = np.dot(evecs[:,0, None], evecs[:,0, None].T).T.dot(y)
ax.plot(y_reduced[0, :], y_reduced[1, :], 'k.')
configure_spines()
ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))
#axes[1,1].set_axis_off()
plt.savefig('figures/pca_illustration.svg', transparent=True)
