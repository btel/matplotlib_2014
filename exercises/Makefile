all : templates  docs

archive : datavis.tgz

.PHONY : templates docs figures

templates: templates/olympics_vis.py 

figures : figures/ex1_parallel_coordinates.png figures/ex2_summer_olympics.png figures/ex3_normalised_coordinates.png

docs : docs/exercises.html

docs/exercises.html : docs/exercises.rst figures
	cp figures/*.png docs/
	rst2html.py $< > $@

templates/%.py : solutions/%.py code/remove_solutions.py
	python code/remove_solutions.py $< templates/

figures/%.png : templates/%.py code/save_plot.py solutions/olympics_vis.py
	PYTHONPATH=$(PYTHONPATH):solutions/ python code/save_plot.py $< figures/

datavis.tgz: docs templates
	mkdir datavis
	mkdir datavis/data
	mkdir datavis/docs
	
	cp templates/* datavis
	cp data/summer_olympics_full.csv datavis/data
	cp docs/exercises.html figures/*.png datavis/docs
	tar czf datavis.tgz datavis
	rm -fr datavis
