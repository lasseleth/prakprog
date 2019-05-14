CFLAGS = -Wall -std=gnu99
CFLAGS += $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)
PLOTTER = gnuplot

all: out.txt hamilplot.svg

out.txt: integ
	./integ > out.txt

integ: integ.o

hamilplot.svg: hamil.gpi hamilout.txt
	gnuplot $<

hamilout.txt: hamil
	./$< > $@

.PHONY: clean
clean:
	$(RM) *.o *.txt *.pdf *.data *.svg integ hamil
