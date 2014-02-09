#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

from olympics_vis import parallel_coordinates

if __name__ == '__main__':
    
    values = np.hstack((np.random.randn(4, 10) + 4*np.random.rand(4,1),
                        np.random.randn(4, 8) + 4*np.random.rand(4,1)
                       ))
    labels = np.concatenate((['Label A']*10, ['Label B']*8)) 
    names = map(lambda x: "coord %i" % x, range(4))

    parallel_coordinates(names, values, labels)
    plt.show()
