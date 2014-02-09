#!/usr/bin/env python
#coding=utf-8

"""This module contains solution to Explore Summer Olympics
exercises. To finish the exercises you have to implement the functions
below and run tests provided in seperate Python scripts.

Before runing the scripts please make sure that this module and the
testing scripts are in the same directory
"""

import numpy as np
import matplotlib.pyplot as plt

# EXERCISE 1
# To test your solution run ex1_parallel_coordinates.py
def parallel_coordinates(coordinates, values, labels):
    """Plot 2d array `values` using K parallel coordinates.
    
    Arguments:

        coordinates -- list or array of K elements containg coordinate
            names,
        values -- (K,N)-shaped array of N data points with K
            coordinates, 
        labels -- list or array of one string per data point
            describing its class membership (category)
    """

    # SOLUTION
    ax = plt.subplot(111)

    # find names and number of different classes
    ulabels = np.unique(labels)
    n_labels = len(ulabels)
    
    # for each select distinct colors from Accent pallette
    cmap = plt.get_cmap('Accent')
    colors = cmap(np.arange(n_labels)*cmap.N/(n_labels+1))

    # change the label strings to indices into class names array
    class_id = np.searchsorted(ulabels, labels) 
    lines = plt.plot(values[:,:], 'k')
    [ l.set_color(colors[c]) for c,l in zip(class_id, lines) ]
    

    # add grid, configure labels and axes
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('outward', 5))
    ax.spines['bottom'].set_visible(False)
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('none')
    
    plt.xticks(np.arange(len(coordinates)), coordinates)
    plt.grid(axis='x', ls='-')

    leg_handlers = [ lines[np.where(class_id==id)[0][0]] 
                    for id in range(n_labels)]
    ax.legend(leg_handlers, ulabels, frameon=False, loc='upper left',
            ncol=len(labels),
            bbox_to_anchor=(0, -0.03, 1, 0))

    # END OF SOLUTION

# EXERCISE 2
# To test your solution run ex2_summer_olympics.py
def format_data(data, sel_disciplines, sel_countries, sel_years):
    """Count the medals won by selected countries in selected
    discplines over selected Summer Olympics edition. 
    Shape data in format suitable for parallel_coordinates.

    Arguments:

        data -- record array imported from CSV. Each row in the array
           contains data about a single medal-wining athlete. Fields
           relevant to this function are: `noc` (country codes),
           `edition` (year of the olympics), `discipline`

        sel_disciplines -- numpy array of selected discipline names

        sel_countries -- numpy array of selected country codes

        sel_years -- numpy array of selected Olympic years as integers

    Returns:

        medal_count -- 2D array of total number of medals aggregated
           over all athletes in selected
           disciplines (columns) grouped by Olympic years and country of
           origin (rows). Each row represent one country and one year,
           but different countries can be intermixed.

        country_names -- 1D numpy array with one entry (string) per row
           of `medal_counts`, which identifies the row with country
           name.
    """
    medal_year = data['edition']
    medal_country = data['noc']
    medal_discipline = data['discipline']

    # SOLUTION
    medal_count = []
    country_names = []
    for noc in sel_countries:
        for yr in sel_years:
            #group data by year/country
            country_year_discipline = medal_discipline[(medal_country==noc) &
                                                       (medal_year==yr)]
            #count medals in selected disciplines
            medals =  [(country_year_discipline==disc).sum() 
                       for disc in sel_disciplines]
            medal_count.append(medals)
            country_names.append(noc)
    medal_count = np.array(medal_count).T
    # END OF SOLUTION

    medal_count = np.asarray(medal_count)
    country_names = np.asarray(country_names)

    return medal_count, country_names

# EXERCISE 3
# To test your solution run ex3_normalised_coordinates.py
def normalised_coordinates(coordinates, values, labels):
    """Plot 2d array `values` using K parallel coordinates.
    
    Arguments:

        coordinates -- list or array of K elements containg coordinate
            names,
        values -- (K,N)-shaped array of N data points with K
            coordinates, 
        labels -- list or array of one string per data point
            describing its class membership (category)
    """
    
    K = len(coordinates)
    
    # normalise data
    vmin, vmax = values.min(1), values.max(1)
    normed_values = (values - vmin[:, None])*1. / (vmax[:, None] -
                                                   vmin[:, None])

    # SOLUTION
    
    # create independent, attached axes
    fig, axes = plt.subplots(1, K-1)
    fig.subplots_adjust(wspace=0)
    
    
    # find names and number of different classes
    ulabels = np.unique(labels)
    n_labels = len(ulabels)
    
    # obtain colors
    cmap = plt.get_cmap('Accent')
    colors = cmap(np.arange(n_labels)*cmap.N/(n_labels+1))

    # change the label strings to indices into class names array
    class_id = np.searchsorted(ulabels, labels) 
    
    for i in range(K-1):
        ax = axes[i]

        lines = ax.plot(normed_values[:,:], 'k')

        # set line colors
        [ l.set_color(colors[c]) for c,l in zip(class_id, lines) ]
    
        # configure axes
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_position(('outward', 5))
        ax.spines['bottom'].set_visible(False)
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('none')

        # set limit to show only single line segment
        ax.set_xlim((i, i+1))
        ax.set_xticks([i])
        ax.set_xticklabels([coordinates[i]])

        # set the scale
        ax.set_yticks([0, 1])
        ax.set_yticklabels([vmin[i], vmax[i]])

    # we have to deal with rightmost axis separately
    axes[-1].set_xticks([K-2, K-1])
    axes[-1].set_xticklabels(coordinates[-2:])
    
    ax = axes[-1].twinx()
    ax.tick_params(axis='y', direction='out')
    ax.xaxis.set_ticks_position('none')
    ax.set_yticks([0, 1])
    ax.set_yticklabels([vmin[-1], vmax[-1]])
    
    # END OF SOLUTION

    # add legend in figure coordinates
    leg_handlers = [ lines[np.where(class_id==id)[0][0]] 
                    for id in range(n_labels)]
    plt.legend(leg_handlers, ulabels, frameon=False, loc='upper left',
               ncol=len(labels),
               bbox_to_anchor=(0.1, 0.06, 0.9, 0.02),
               bbox_transform=fig.transFigure)
    
    # set leftmost axis as the default for labelling
    plt.sca(axes[0])

