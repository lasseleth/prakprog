CFLAGS = -Wall -std=gnu99
CFLAGS += $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)
PLOTTER = gnuplot

all: out.txt out_hydro.txt plot.svg

out.txt: main
	./main > out.txt

main: main.o

out_hydro.txt: hydro
	./hydro > out_hydro.txt

hydro: hydro.o Aux.o

plot.svg: plot.gpi plot.txt
	gnuplot $<

plot.txt: hydro
	./$< > $@

.PHONY: clean
clean:
	$(RM) *.o *.txt *.pdf *.data *.svg integ hydro

