import re

corpus = open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\Final\corpus.txt", "r", encoding="UTF-8")

EditedCorpus = []

word_counter = 0

for line in corpus:
    if "https" in line:
        continue
    else:
        EditedCorpus.append((line).lower())
        # print(re.sub(r'[^a-zA-Z\s]', '', line).lower())

# print(EditedCorpus)

with open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\Final\Edited_Corpus.txt", "w", encoding="UTF-8") as f:
    for word in EditedCorpus:
        if word == '\n':
            continue
        f.write(f"{word}")
        word_counter += 1

print(f"{word_counter} words")