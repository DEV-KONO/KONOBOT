CC = gcc
CFLAGS = -Wall -I./CUSTOMLIBS
SRC = CUSTOMLIBS/TOLKIENIZER/Tolkienizer.c CUSTOMLIBS/FILEREADER/FileReader.c CUSTOMLIBS/VOORHEES/Voorhees.c
OBJ = $(SRC:.c=.o)
OUT = Tolkienizer

all: $(OUT)

$(OUT): $(OBJ)
	$(CC) $(OBJ) -o $(OUT)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(OUT)