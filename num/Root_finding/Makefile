PYTHON = python3

.PHONEY: all
all: out.txt
	cat $<
	
out.txt: main.py funcs.py newtonian.py qr.py
	$(PYTHON) $< > $@

.PHONEY: clean
clean:
	$(RM) *.txt
	$(RM) *.svg