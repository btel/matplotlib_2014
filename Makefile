NOTEBOOKS=01_visualising_patterns_over_time.ipynb 02_visualising_proportions.ipynb 03_visualising_distributions.ipynb 04_visualising_correlations.ipynb 05_finding_patterns.ipynb 06_making_maps_with_matplotlib.ipynb
PDFFILES=$(patsubst %.ipynb,build/%.pdf,$(NOTEBOOKS))

all: handouts.pdf 


build/%.pdf : notebooks/%.ipynb
	ipython nbconvert $< --to latex --post pdf
	mv $*.pdf $@
	rm -fr $*_files $*.tex

handouts.pdf: $(PDFFILES)
	pdfunite $^ $@
