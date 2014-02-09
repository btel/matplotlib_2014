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

    # ENTER YOUR SOLUTION BELOW
    # ...
    
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

    # ENTER YOUR SOLUTION BELOW
    # ...
    
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

    # ENTER YOUR SOLUTION BELOW
    # ...
    
    # add legend in figure coordinates
    leg_handlers = [ lines[np.where(class_id==id)[0][0]] 
                    for id in range(n_labels)]
    plt.legend(leg_handlers, ulabels, frameon=False, loc='upper left',
               ncol=len(labels),
               bbox_to_anchor=(0.1, 0.06, 0.9, 0.02),
               bbox_transform=fig.transFigure)
    
    # set leftmost axis as the default for labelling
    plt.sca(axes[0])

