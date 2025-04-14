#include <stdio.h>
#include "C:\Users\samue\Documents\DEV\KONOBOTLLM\KONOBOT\CUSTOMLIBS\FILEREADER\FileReader.h"
#include "Tolkien.h"
#include <stdlib.h>

//Usar gcc -I./CUSTOMLIBS/FileReader Tokenizer.c CUSTOMLIBS/FileReader/FileReader.c -o nombre_del_exe
//en la consola, para poder hacer un ejecutable.

int main() {
    
    const char *fileroute = "C:/Users/samue/Documents/DEV/KONOBOTLLM/DATASET/Final/Edited_Corpus.txt";

    Tolkien *TolkienArray = malloc(WordCount(true, fileroute)*sizeof(Tolkien));

    int TID = 0;

    int TotalWords = WordCount(true, fileroute);

    char *word = FileReader(fileroute);

    while (word!=NULL) {
        // printf("%s\n", word);

        Tolkien tolkien = {word, TID++};

        TolkienArray[tolkien.Id] = tolkien;
    
        free(word);

        word = FileReader(fileroute);
    }

    for (int i = 0 ; i<TotalWords ; i++) {
        PrintTolkien(TolkienArray[i]);
    }

    free(TolkienArray);

    return 0;

}

void TolkienToJson(Tolkien *TA) {

}

void PrintTolkien(Tolkien T) {
    printf("Word: %s,\nId: %d,\n", T.Word, T.Id);
}