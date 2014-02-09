#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab

from olympics_vis import parallel_coordinates, format_data

if __name__ == '__main__':
    data = mlab.csv2rec('data/summer_olympics_full.csv')

    disciplines = np.array(['Swimming', 
                            'Athletics',
                            'Fencing', 
                            'Basketball',
                            'Judo'])
    countries = ['USA', 'RUS']
    years = np.array([2008, 2004, 2000, 1996])

    # count number of medals per country in different olympics
    medal_count, country_names = format_data(data, disciplines,
                                             countries, years)
    
    parallel_coordinates(disciplines, medal_count, country_names) 
    plt.ylabel('number of medals')
    plt.show()
