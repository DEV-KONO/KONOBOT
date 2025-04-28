#ifndef VOORHEES_H
#define VOORHEES_H

//las funciones van aqui abajo declaradas, solo la primera linea, sigue a los otros archivos .h


#include "C:/Users/samue/Documents/DEV/KONOBOTLLM/KONOBOT/CUSTOMLIBS/FILEREADER/Tolkien.h"  

/**
 * @brief Convierte un array de structs Tolkien a un archivo JSON.
 * @param TolkienArray Array de estructuras Tolkien.
 * @param tokenCount Número de tokens en el array (obtenido con WordCount).
 * @param outputPath Ruta del archivo JSON de salida.
 * @return 0 si éxito, -1 si error.
*/
int TolkienToJSON(Tolkien* TolkienArray, int tokenCount, const char* outputPath);



#endif