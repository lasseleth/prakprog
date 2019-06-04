CFLAGS = -Wall -std=gnu99
LDLIBS = -lm
CC = gcc
SCRIPT = plot.gpi
FORMAT = svg
PLOTTER = gnuplot

.PHONY: all
all:	out.io.txt out.cmd.txt plot.svg

plot.svg:	plot.gpi out.io.txt out.cmd.txt
	gnuplot plot.gpi

out.io.txt	:	input.data.txt main-stdio
	./main-stdio < input.data.txt > out.io.txt

out.cmd.txt	:	input.data.txt main-cmdline
	./$(word 2,$^)	`cat $<`	>$@

input.data.txt	:	Makefile
	seq 0 0.1 7 > input.data.txt

.PHONY: clean
clean	:
	find ./ -type f -executable -delete
	$(RM) *.dat *.svg *.png *.pdf log* *.txt