CFLAGS = -Wall -std=gnu11
LDLIBS = -lm
.PHONEY:all
all:out.txt
	cat $^
out.txt:main	
	./$^ > $@

clean:
	$(RM) main *.o out*
