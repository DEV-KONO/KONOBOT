from pathlib import Path
import sys
sys.path.append(r"CUSTOMLIBS\Python\ZANCE")
from ZanCe import ZanCe

directory = Path('./DATASETS/LIBROS/ESPAÑOL')
files = [file for file in directory.iterdir() if file.is_file()]

joint_books = ""

for f in files:
    with open(f"{f}", "r", encoding="utf-8") as book:
        joint_books += book.read()

joint_books = joint_books.replace("[", "").replace("]", "").replace(",", "").replace('"', "'").replace("—", "").split()

with open("DATASETS/BOOK_CORPUS/Unedited_Book_Corpus.txt", "w", encoding="utf-8") as bc:
    for word in joint_books:
        bc.write(f"{word}\n")

with open("DATASETS/BOOK_CORPUS/Unique_Book_Corpus.txt", "w", encoding="utf-8") as bc:
    for word in ZanCe(joint_books):
        bc.write(f"{word}\n")