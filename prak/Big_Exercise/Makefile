CFLAGS += -Wall -std=c11 `gsl-config --cflags`
CFLAGS += -march=native -Ofast -DHAVE_INLINE -DGSL_RANGE_CHECK_OFF
LDLIBS += `gsl-config --libs`
CC = gcc
PLOTTER = gnuplot

all: out.txt plot.pdf
#If you wish to change the size of the matrix, make clean and the type "make n= >>value<<"

plot.pdf: plot.gpi out.txt
	gnuplot $<

out.txt: main Makefile
	./main $(n) > $@

main: main.o Jacobi.o


clean:
	rm -f main *.o out* *.pdf *.svg log* *log
