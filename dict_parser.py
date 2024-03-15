import json

with open("words.txt", "r", encoding="utf-8") as f:
	words = f.read().replace(" - ", "\n")
words = words.split("\n")
print(words)
ls = {}
for i in range(0, len(words), 2):
	ls[words[i]] = words[i+1]

with open('dictionary.json', 'w', encoding="utf-8") as f:
    json.dump(ls, f, ensure_ascii=False, indent = 4)
