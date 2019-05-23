PYTHON = python3

.PHONEY: all
all: out.txt
out.txt: main.py GR.py
	$(PYTHON) $< > $@

.PHONEY: clean
clean:
	$(RM) *.txt
	$(RM) *.svg