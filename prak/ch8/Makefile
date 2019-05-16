CFLAGS += -O -std=gnu11 -Wall $$(gsl-config --cflags)
LDLIBS += $$(gsl-config --libs)


.PHONY:all clean

all:logistic_plot.svg orbital_plot.svg

out.txt:logistic_plot.svg orbital_plot.svg mylogistic.c myorbital.c
	
orbital_plot.svg:orbitals.gpi orbital.data Makefile
	gnuplot $< > $@ 
	
logistic_plot.svg:logistic.gpi logistic.data Makefile
	gnuplot $< > $@

logistic.data orbital.data:main
	./$< 1> logistic.data  2> orbital.data

main:main.o mylogistic.o myorbital.o

clean:
	$(RM) *.o *.data main *.svg 