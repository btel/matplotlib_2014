#!/usr/bin/env python
#coding=utf-8

import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

plt.plot([1,2])

plt.savefig('figures/mpl_backend.png', transparent=True)
plt.savefig('figures/mpl_backend.svg', transparent=True)
plt.savefig('figures/mpl_backend.pdf', transparent=True)
