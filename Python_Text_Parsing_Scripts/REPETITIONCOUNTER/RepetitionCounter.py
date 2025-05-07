import json
from collections import Counter

with open("DATASETS\TOKENS\Tokens.json", "r", encoding="utf-8") as f:
    tokens = json.load(f)

with open(r"DATASETS\FULL_CORPUS\Full_Repeated_Corpus.txt", "r", encoding="utf-8") as f:
    palabras = f.read().splitlines()


frecuencias = Counter(palabras)

for token in tokens:
    token["Frequency"] = frecuencias.get(token["Word"], 0)

with open(r"DATASETS\TOKENS\Tokens.json", "w", encoding="utf-8") as f:
    json.dump(tokens, f, indent=2, ensure_ascii=False)
