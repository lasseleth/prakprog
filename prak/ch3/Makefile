CFLAGS = -Wall -std=gnu99 -O
LDLIBS = -lm

.PHONEY:all
all: out.txt
	cat out.txt

out.txt : main
	./main > out.txt

main	:	main.o

main.o	:	main.c
	$(CC) $(CFLAGS) -c $<

clean		:
	$(RM) out.txt *.o 