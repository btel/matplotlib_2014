#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from cartopy import crs

if __name__ == "__main__":

    ax = plt.subplot(221, projection=crs.InterruptedGoodeHomolosine())
    ax.coastlines()
    ax.set_title("Goode homolosine")
    ax = plt.subplot(222, projection=crs.Mercator())
    ax.set_title("Mercator")
    ax.coastlines()
    ax = plt.subplot(223, projection=crs.Geostationary())
    ax.set_title("Geostationary")
    ax.coastlines()
    ax = plt.subplot(224, projection=crs.Mollweide())
    ax.coastlines()
    ax.set_title("Mollweide")
    plt.savefig('figures/geo_projections.svg', transparent=True)
