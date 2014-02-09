#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab

from olympics_vis import normalised_coordinates, format_data

if __name__ == '__main__':
    data = mlab.csv2rec('data/summer_olympics_full.csv')

    disciplines = np.array(['Swimming', 
                            'Athletics',
                            'Fencing', 
                            'Basketball',
                            'Judo'])
    countries = ['USA', 'RUS']
    years = np.unique(data['edition'])
    
    #In 1991 Soviet Union dissolves into Russia and other post-Soviet states
    NOCs = data['noc']
    NOCs[NOCs=='URS'] = 'RUS'
    data['noc'] = NOCs

    # count number of medals per country in different olympics
    medal_count, country_names = format_data(data, disciplines,
                                             countries, years)
    
    normalised_coordinates(disciplines, medal_count, country_names) 
    #plt.ylabel('number of medals')
    plt.show()
