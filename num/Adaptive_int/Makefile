PYHTON = python3

.PHONEY: all
all: out.txt


out.txt:	main.py Integration.py
	#Takes some time, be patient please
	$(PYHTON) $< > $@

.PHONEY: clean
clean:
	$(RM) *.txt
	$(RM) *.svg