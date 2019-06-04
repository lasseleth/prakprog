CFLAGS = -Wall -std=gnu99
CFLAGS += $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

all: output.txt
	cat output.txt

output.txt: main
	./$< > $@

main: main.o

.PHONEY: clean
clean: 
	$(RM) main *.txt *.o