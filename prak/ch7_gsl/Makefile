CFLAGS += -Wall -std=gnu1x $$(gsl-config --cflags)
LDLIBS += $$(gsl-config --libs)

.PHONEY:all
all:	airy.svg airy.data main.data

airy.svg:	airy.gpi airy.data
	gnuplot $<

airy.data:	airy
	./$< > $@

main.data: main
	./$< > $@

.PHONEY:clean
clean:
	find . -type f -executable -delete
	rm -f *.o *.txt *.data *.svg
