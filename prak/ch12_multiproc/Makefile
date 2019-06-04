CFLAGS += -Wall -O1 -pthread -fopenmp 
LDLIBS += -lm -pthread -lgomp
CC = gcc

.PHONY:default

default:out.txt
	cat $<

out.txt:main_pthreads main_openmp 
	./$< > $@
	./$(word 2,$^) >> $@


main_openmp:main_openmp.o shoot.o params.o

main_pthreads:main_pthreads.o shoot.o params.o

clean:
	$(RM) *.o *.txt *.pdf *.svg
