CFLAGS = -Wall -std=gnu99
CFLAGS += $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)     
PLOTTER = gnuplot

all: diff.svg circ.svg ellip.svg orb.svg

diff.svg: diff.gpi diff.data
	gnuplot $<

diff.data: diffeq
	./$< > $@

circ.svg: circ.gpi circ.data
	gnuplot $<

circ.data: orbit makefile
	./orbit -p 0.0 -e 0.0> $@

ellip.svg: ellip.gpi ellip.data
	gnuplot $<

ellip.data: orbit makefile
	./orbit -p -0.5 -e 0.0> $@

orb.svg: orb.gpi orb.data
	gnuplot $<

orb.data: orbit makefile
	./orbit -p -0.5 -e 0.01> $@


.PHONY: clean
clean: 
	$(RM) *.o *.txt *.pdf *.data *.svg orbit diffeq