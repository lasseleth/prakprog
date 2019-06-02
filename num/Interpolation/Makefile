PYTHON = python3
PLOTTER = gnuplot

.PHONEY: all
all: spline_plot.svg spline_integ.svg out_interp.txt exact.txt

spline_plot.svg: spline_plot.gpi out_interp.txt exact.txt
	$(PLOTTER) $<

spline_integ.svg: spline_integ.gpi out_interp.txt exact.txt
	$(PLOTTER) $<

out_interp.txt: main.py search.py lspline.py qspline.py cspline.py
	$(PYTHON) $< > $@

exact.txt: check.py
	$(PYTHON) $< > $@

.PHONEY: clean
clean:
	$(RM) *.txt
	$(RM) *.svg