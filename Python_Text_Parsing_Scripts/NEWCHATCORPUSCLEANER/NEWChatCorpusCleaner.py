#primero, unimos todos los textos en un solo documento
#hay que cargarlo primero y despues unirlos todos.
from dateutil import parser
import sys
sys.path.append(r"CUSTOMLIBS\Python\ZANCE")
from ZanCe import ZanCe

file_list = [r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\WhatsApp Chat - Chemamix\_chat.txt", r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\WhatsApp Chat - Dante\_chat.txt", r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\WhatsApp Chat - Éricka\_chat.txt", r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\WhatsApp Chat - Diego Salgado\_chat.txt", r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\WhatsApp Chat - Jania ;)\_chat.txt", r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\WhatsApp Chat - Misal Chicha\_chat.txt"]

joint_files = ""

corpus_list = []

counter = 0

def is_valid_date(date_str):
    try:
        parser.parse(date_str)
        return True
    except:
        return False

for file in file_list:
    with open(file, "r", encoding="utf-8") as f:
        joint_files += f.read()

with open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\NEWCorpusFiles\joint_chats.txt", "w", encoding="utf-8") as f:
    f.write(joint_files)

with open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\NEWCorpusFiles\joint_chats.txt", "r", encoding="utf-8") as f:
    # print(f.read().replace("[", "").replace("]", ""))
    joint_files = ""
    for line in f:
        
        for word in line.split():

            # print(f"Pre: {word}")
            # print(f"Parsed: {word.replace("[", "").replace("]", "").replace(",", "")}")

            word = word.replace("[", "").replace("]", "").replace(",", "").replace('"', "'")

            if is_valid_date(word):
                # print(f"Parsed Date: {word}")
                pass
            elif "\u200e" in word:
                continue
            elif word == "Chemamix:" or "https://" in word or word == "Dante:" or word == "Éricka:" or word == "Diego" or word == "Misal" or word == "Jania":
                break
            elif "Kono:" in word:
                pass
            else:
                # print(word+"\n")
                # counter += 1
                # print(counter)
                joint_files += f"{word}\n"
                # print(f"Final: {word}")
                # input()

with open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\NEWCorpusFiles\Unedited_Corpus.txt", "w", encoding="utf-8") as f:
    f.write(joint_files)
    # print("FINISHED!!!!")

with open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\NEWCorpusFiles\Unedited_Corpus.txt", "r", encoding="utf-8") as f:
    for line in f:
        corpus_list.append(line)

with open(r"C:\Users\samue\Documents\DEV\KONOBOTLLM\DATASET\NEWCorpusFiles\Unique_Corpus.txt", "w", encoding="utf-8") as f:
    for word in ZanCe(corpus=corpus_list):
        f.write(word)
    print("FINISHED!!!!")