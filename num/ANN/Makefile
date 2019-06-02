PYTHON = python3
PLOTTER = gnuplot

.PHONEY: all
all: out.txt plot1D.svg plot2D.svg

plot2D.svg: plot2D.gpi out.txt
	$(PLOTTER) $<

plot1D.svg: plot2D.gpi out.txt
	$(PLOTTER) $<

out.txt: main.py ANN.py
	## This takes time, please have some patience ##
	$(PYTHON) $< > $@

.PHONEY: clean
clean: 
	$(RM) *.txt
	$(RM) *.svg