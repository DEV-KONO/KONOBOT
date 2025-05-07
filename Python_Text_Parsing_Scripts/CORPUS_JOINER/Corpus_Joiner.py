#unir los corpus

from random import shuffle


Full_Repeated_Corpus = ""
Full_Unique_Corpus = ""

with open("DATASETS/BOOK_CORPUS/Unedited_Book_Corpus.txt", "r", encoding="utf-8") as f:
    Full_Repeated_Corpus += f.read()

with open("DATASETS/CHAT_CORPUS/Unedited_Chat_Corpus.txt", "r", encoding="utf-8") as f:
    Full_Repeated_Corpus += f.read()

with open("DATASETS/BOOK_CORPUS/Unique_Book_Corpus.txt", "r", encoding="utf-8") as f:
    Full_Unique_Corpus += f.read()

with open("DATASETS/CHAT_CORPUS/Unique_Chat_Corpus.txt", "r", encoding="utf-8") as f:
    Full_Unique_Corpus += f.read()

Full_Unique_Corpus = Full_Unique_Corpus.split()
shuffle(Full_Unique_Corpus)

with open("DATASETS/FULL_CORPUS/Full_Repeated_Corpus.txt", "w", encoding="utf-8") as f:
    f.write(Full_Repeated_Corpus)

with open("DATASETS/FULL_CORPUS/Full_Unique_Corpus.txt", "w", encoding="utf-8") as f:
    for word in Full_Unique_Corpus:
        f.write(f"{word}\n")