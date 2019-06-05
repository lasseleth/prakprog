CFLAGS += -Wall -std=c11 `gsl-config --cflags`
CFLAGS += -march=native -Ofast -DHAVE_INLINE -DGSL_RANGE_CHECK_OFF
LDLIBS += `gsl-config --libs`
CC = gcc
PLOTTER = gnuplot

all: out.txt plot.pdf Big_exercise.pdf 
#If you wish to change the size of the matrix, make clean and the type "make n= >>value<<"
n=50
plot.pdf: plot.gpi out.txt
	gnuplot $<

out.txt: main Makefile
	./main $(n) > $@

main: main.o Jacobi.o

Big_exercise.pdf: Big_exercise.tex plot.pdf
	pdflatex $<

clean:
	rm -f main *.o *.pdf  log* *log out*
