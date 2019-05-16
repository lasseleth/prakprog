CFLAGS += -O -std=gnu11 -Wall $$(gsl-config --cflags)
LDLIBS += $$(gsl-config --libs)


.PHONY:all clean

all:logistic_plot.svg orbital_plot.svg

out.txt:logistic_plot.svg orbital_plot.svg mylogistic.c myorbital.c
	
orbital_plot.svg:orbitals.gpi orbital.data Makefile
	gnuplot $< > $@ 
	
logistic_plot.svg:logistic.data Makefile
	gnuplot -e "\
		set term svg background 'white'; \
		plot[][] \
		'$<' using 1:2 with lines dt 2 title 'my logistic',\
		'$<' using 1:3 with lines dt 5 title 'math.h logistic'\
		" > $@


logistic.data orbital.data:main
	./$< 1> logistic.data  2> orbital.data

main:main.o mylogistic.o myorbital.o

clean:
	$(RM) *.o *.data main *.svg 