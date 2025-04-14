from dateutil import parser

file = open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\WhatsApp Chat - Éricka\_chat.txt", "r", encoding="UTF-8")

parsed_text = []

def is_valid_date(date_str):
    try:
        parser.parse(date_str)
        return True
    except:
        return False


for line in file:
    line = line.replace("[", "").replace("]", "")

    if line[0] == "‎":
        continue
    # print(line)

    for word in line.split():
        if is_valid_date(word):
            pass
        elif word == "Éricka" or word == "\u200eEliminaste":
            break
        elif word == "Kono:":
            continue
        else:
            parsed_text.append(word)
        # print(word, is_valid_date(word))
    # print(x.replace("[", "").replace("]", ""))

# print(parsed_text)

unique = list(dict.fromkeys(parsed_text))

print(unique)

with open(r'C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\Final\final_ericka.txt', 'w', encoding="UTF-8") as f:
    for word in unique:
        f.write(f"{word}\n")