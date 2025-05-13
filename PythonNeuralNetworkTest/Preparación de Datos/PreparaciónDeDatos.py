import json

#Guardamos el archivo .json en memoria
with open(r"DATASETS\TOKENS\embedings.json", "r", encoding="utf-8") as t:
    tokens = json.load(t)

#Hacemos un diccionario que guarde palabra: id y otro que guarde id: palabra

word2id = {}
id2word = {}

for token in tokens["embeddings"]:
    word2id[f"{token["word"]}"] = token["token_id"]
    id2word[f"{token["token_id"]}"] = token["word"]

print(f"Word2ID['mamay'] = {word2id["mamay"]}")
print(f"ID2Word[0] = {id2word["0"]}")