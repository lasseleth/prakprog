PYTHON = python3
PLOTTER = gnuplot

.PHONEY: all
all: MC.txt plot_err.svg

plot_err.svg: plot_err.gpi error.txt
	$(PLOTTER) $<

error.txt: error.py MonteCarlo.py
	$(PYTHON) $< > $@

MC.txt: main.py MonteCarlo.py
	$(PYTHON) $< > $@

.PHONEY: clean
clean: 
	$(RM) *.txt
	$(RM) *.svg
	