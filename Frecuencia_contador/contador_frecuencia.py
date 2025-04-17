from collections import Counter

def read_corpus_from_file(file_path):
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Eliminar signos de puntuación y dividir por espacios
                line_words = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in line).split()
                words.extend(line_words)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{file_path}'")
    
    return words

if __name__ == "__main__":
    # Preguntar al usuario cómo quiere proporcionar el corpus
    mode = input("¿Cómo deseas proporcionar el corpus? (1: Desde archivo, 2: Manualmente): ")
    
    corpus = []
    if mode == "1":
        # Leer desde archivo
        file_path = input("Ingresa la ruta del archivo que contiene el corpus: ")
        corpus = read_corpus_from_file(file_path)
        if not corpus:
            print("No se pudo leer el corpus. Finalizando programa.")
            exit()
    else:
        # Ingreso manual
        text = input("Ingresa el texto del corpus (las palabras separadas por espacios): ")
        corpus = text.split()
    
    # Convertir todo a minúsculas para uniformidad
    corpus_lower = [word.lower() for word in corpus]

    # Contar todas las palabras
    word_counts = Counter(corpus_lower)

    # Mostrar resultados ordenados por frecuencia (de mayor a menor)
    print("\nFrecuencia de todas las palabras (ordenadas):")
    for word, count in word_counts.most_common():
        print(f"'{word}': {count} veces")
