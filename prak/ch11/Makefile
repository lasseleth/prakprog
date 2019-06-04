CFLAGS = -Wall -std=gnu99
CFLAGS += $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)
PLOTTER = gnuplot

all: out.txt out_square.txt plot.svg

out.txt: rosen
	./rosen > out.txt

rosen: rosen.o

out_square.txt: square
	./square > out_square.txt

square: square.o

plot.svg: plot.gpi plot.txt
	gnuplot $<

plot.txt: square
	./$< > $@ 

.PHONY: clean
clean:
	$(RM) *.o *.txt *.pdf *.svg rosen square