CFLAGS += -Wall -std=c11 `gsl-config --cflags`
CFLAGS += -march=native -Ofast -DHAVE_INLINE -DGSL_RANGE_CHECK_OFF
LDLIBS += `gsl-config --libs`
CC = gcc

all: out.txt
	cat $<
#If you wish to change the size of the matrix, make clean and the type "make n= >>value<<"

out.txt: main Makefile
	./main $(n) 2> $@

main: main.o Jacobi.o

clean:
	rm -f main *.o out* *.png *.svg log* *log
