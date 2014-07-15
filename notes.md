matplotlib @ EuroPython 2014

Introduction:

  * EDA = exploratory data analysis = visual data analysis
  * static print figures
  * open data
  * JDH and brief history of matplotlib

Topics:

# visualising patterns over time

datasets: weather
extra libs: statsmodels, datetime, goodies 
plots:
  • time series plot (`plt.plot`)
customisation:
  * stateful interface:
     - `plt.*` interface
     - `plt.show()` and matplotlib backends ("Qt/Tk/GTK/ipython/Web")
     - setting labels (`xlabel`, `ylabel`)
     - manual tick positions (?) (`plt.xticks`)
  * datetime support
  • choosing automatic ticker locators (YearsLocator, MonthLocator)
data analysis:
  • smoothing with LOESS curve (`statsmodels.nonparametric.smoothers_lowess`)

# visualising proportions

datasets: worldcup.db
plots:
  • bar plot (`plt.bar`)
design point:
   * tufte style
customisation:
  * object-oriented interface:
     * stateful design and accessing the state (`gca`)
     * axes container its methods and attributes (spines,x/yaxis)
     * configure spines and ticks ticks position (`set_ticks_position`)
     * set background color (`set_axis_bgcolor`)
  * setting up the grid (`plt.grid`) and putting it below data
  * adding text to figure (`plt.figtext`)

# visualising distributions

datasets: Word Bank GDP
plots:
  • histogram (`plt.hist`)
  • boxplot and standard markers (`plt.boxplot`)
  * vertical lines (`plt.vlines`)
customisation:
  • adding legend (`plt.legend`)
  * axes text (`plt.text/ax.text`)
  * data and axes transform (`ax.transAxes`, `ax.transData`)
data analysis:
  * kernel density estimators (`scipy.stats.gaussian_kde`)
  * statistical test K-S (`scipy.stats.ks_2samp`)

# spotting differences — multivariate data 

datasets: Allen Brain Atlas
plots:
  • 2d x/y plots (`plt.plot`)
  • heatmap (`plt.imshow`)
design points:
  * small mutiplies
  * using colors
customisation: 
  * choosing marker styles in `plt.plot`
  • faceted plotting with subplots (`plt.subplots`)
  • choosing color scales (`matplotlib.cm`)

# data reduction/finding patterns 

datasets: Allen Brain Atlas
extra libs: sklearn
plots:
  • scatter plot (`plt.scatter`)
  * pcolor for matrix plotting (`plt.pcolor`)
  * svg processing
customisation:
  * using colormaps "by hand" (`mcolors.normalize`, `cm.get_cmap`)
data analysis points:
  * pca using correlation matrix
  * whitening (or sphering) procedure
  * clustering kmeans (`sklearn.cluster.k_means`)

# spatial relationships

datasets: 
   * AVHRR sea temp,
   * RATP stops,
   * MapQuest tiles,
   * Ile de France population
extra libs: cartopy, netCDF4 (for reading data)
desing points:
   * ColorBrewer colors
plots:
   * contour plot (`plt.contourf`)
   * Choropleth map 
customisation:
   * cartopy graphical features:
       * base PNG tiles
       * coastlines, borders
   * working with geographic projections
   * custom axes classes 
   * graphical primitives (setting face and edgecolors of paths)
data analysis points:
   * data cube for contour plots
   * combining data from different sources
   * geometric analysis (?)

# putting it all together

datasets:
extra libs: svg_utils
plots:
  • data dashboard
customisation:
  • exporting to data formats
