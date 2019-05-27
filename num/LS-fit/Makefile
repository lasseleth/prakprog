PYTHON = python3
PLOTTER = gnuplot

.PHONEY: all
all: data.txt plot.svg

plot.svg: plot.gpi data.txt
	$(PLOTTER) $<

data.txt: main.py qr.py
	$(PYTHON) $< > $@

.PHONEY: clean
clean:
	$(RM) *.txt
	$(RM) *.svg