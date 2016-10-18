# ============================================================================
# Name        : Makefile
# ============================================================================

.PHONY: all clean

.SUFFIXES: .for

FC=gfortran -g3 -ggdb
LIBS=-lpthread
FLAGS=
FLAGS+=$(INCS) $(LIBS)

SOURCES=mallador.for mtxutil.for meshutil.for

OBJECTS=$(SOURCES:.for=.o)

all: $(SOURCES) mallador

mallador: $(OBJECTS)
	$(FC) $(FLAGS) -o $@ $(OBJECTS)


.for.o:
	$(FC) $(INCS) -c $< -o $@

clean:
	rm -f mallador *.mod *.o

echo:
	echo $(OBJS)
