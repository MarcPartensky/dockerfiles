CC=gcc
CFLAGS=-Wall -Wextra -Werror -std=c11 -O3
LDFLAGS=-lpqcrypto

all: myapp

myapp: myapp.o pqcrypto_keyexchange.o
    $(CC) -o myapp myapp.o pqcrypto_keyexchange.o $(LDFLAGS)

myapp.o: myapp.c pqcrypto_keyexchange.h
    $(CC) -c -o myapp.o myapp.c $(CFLAGS)

pqcrypto_keyexchange.o: pqcrypto_keyexchange.c pqcrypto_keyexchange.h
    $(CC) -c -o pqcrypto_keyexchange.o pqcrypto_keyexchange.c $(CFLAGS)

clean:
    rm -f myapp myapp.o pqcrypto_keyexchange.o

