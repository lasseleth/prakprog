CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

all: out.txt plot.pdf erflatex.pdf

plot.pdf: plot.gpi out.txt
	gnuplot $<

out.txt: int
	./int 0.5 1.5 0.05	> $@

int: int.o

erflatex.pdf: text.tex plot.pdf
	pdflatex $<

.PHONEY: clean
clean:
	$(RM) *.o *.svg *.txt *.pdf int