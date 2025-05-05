import random

chema = open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\Final\final_chemamix.txt", "r", encoding="UTF-8")
danter = open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\Final\final_danter.txt", "r", encoding="UTF-8")
diego = open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\Final\final_diego.txt", "r", encoding="UTF-8")
ericka = open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\Final\final_ericka.txt", "r", encoding="UTF-8")
jania = open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\Final\final_jania.txt", "r", encoding="UTF-8")
misal = open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\Final\final_misal.txt", "r", encoding="UTF-8")

file_list = [chema, danter, diego, ericka, jania, misal]

corpus = []

word_counter = 0

for file in file_list:
    for line in file:
        for word in line.split():
            corpus.append(word)

corpus = list(dict.fromkeys(corpus))

random.shuffle(corpus)

with open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\Final\corpus.txt", "w", encoding="UTF-8") as f:
    for word in corpus:
        f.write(f"{word}\n")
        word_counter += 1

print(f"{word_counter} words")