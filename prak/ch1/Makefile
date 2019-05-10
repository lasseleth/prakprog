CFLAGS = -Wall -std=gnu99
LDLIBS = -lm

.PHONEY:all
all: out.txt
	cat out.txt

out.txt : hello
	./hello > out.txt

hello	:  hello.o

hello.o	:

.PHONY: clean
clean	:
	$(RM) out.txt hello hello.o
