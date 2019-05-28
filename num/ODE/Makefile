PYTHON = python3
PLOTTER = gnuplot

.PHONEY: all
all: rk.txt sine.txt sine_rk.svg

sine_rk.svg: sine_rk.gpi rk.txt sine.txt
	$(PLOTTER) $<

rk.txt: main.py RungeKutta.py
	$(PYTHON) $< > $@

sine.txt: sin_func.py
	$(PYTHON) $< > $@

.PHONEY: clean
clean:
	$(RM) *.txt
	$(RM) *.svg