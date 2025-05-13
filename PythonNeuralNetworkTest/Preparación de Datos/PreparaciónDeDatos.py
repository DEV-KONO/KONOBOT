import json

#Guardamos el archivo .json en memoria
with open(r"DATASETS\TOKENS\tokensWembedding\tokensWembedding.json", "r", encoding="utf-8") as t:
    tokens = json.load(t)

#Hacemos 3 diccionarios, uno para guardar palabra:id, otro para guardar id:palabra y 
#otro para guardar id:embedding

word2id = {}
id2word = {}
embedding = {}

for token in tokens["embeddings"]:
    word2id[f"{token["word"]}"] = token["token_id"]
    id2word[f"{token["token_id"]}"] = token["word"]
    embedding[f"{token["token_id"]}"] = token["vector"]

with open(r"PythonNeuralNetworkTest\Preparación de Datos\Word2ID.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(word2id))

with open(r"PythonNeuralNetworkTest\Preparación de Datos\ID2Word.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(id2word))

with open(r"PythonNeuralNetworkTest\Preparación de Datos\embeddings.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(embedding))


print(f"ID2Word['158965'] = {id2word["158965"]}")
print(f"Embedding['158965'] = {embedding["158965"]}")

print(f"ID2Word['158966'] = {id2word["158966"]}")
print(f"Embedding['158966'] = {embedding["158966"]}")