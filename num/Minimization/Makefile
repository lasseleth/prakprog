PYTHON = python3
PLOTTER = gnuplot

.PHONEY: all
all: out.txt plot.svg decaydata.txt

plot.svg: plot.gpi out.txt decaydata.txt
	$(PLOTTER) $<

decaydata.txt: decaydata.py
	$(PYTHON) $< > $@

out.txt: main.py qr.py functions.py newtonian.py
	$(PYTHON) $< > $@

.PHONEY: clean
clean:
	$(RM) *.txt
	$(RM) *.svg