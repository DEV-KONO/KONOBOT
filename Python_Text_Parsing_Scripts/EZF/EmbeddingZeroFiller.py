import json

with open(r"DATASETS\TOKENS\Tokens.json", "r", encoding="utf-8") as f:
    tokens = json.load(f)
    for token in tokens:
        token["Embedding"] = [0.0] * 128

with open(r"DATASETS\TOKENS\Tokens.json", "w", encoding="utf-8") as f:
    json.dump(tokens, f, indent=1)