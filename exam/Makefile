PYTHON = python3

#If you wish to change the function, go to the main.py file and change the "func1" to func2 or 3
.PHONEY: all
all: out.txt plot.pdf
	cat $<

out.txt: main.py exam.py
	$(PYTHON) $< > $@

.PHONEY: clean #removes just the newly created plot and txt
clean: 
	$(RM) plot.pdf *.txt 

.PHONEY: clean_all #removes all the plots
clean_all:
	$(RM) *.pdf *.txt