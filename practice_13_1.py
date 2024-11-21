alphabet = {
 'a': 0,
 'b': 0,
 'c': 0,
 'd': 0,
 'e': 0,
 'f': 0,
 'g': 0,
 'h': 0,
 'i': 0,
 'j': 0,
 'k': 0,
 'l': 0,
 'm': 0,
 'n': 0,
 'o': 0,
 'p': 0,
 'q': 0,
 'r': 0,
 's': 0,
 't': 0,
 'u': 0,
 'v': 0,
 'w': 0,
 'x': 0,
 'y': 0,
 'z': 0
}

legnt = 0
with open('gadsby.txt', "r") as file:
    lines = file.read()
    for i in lines.split(" "):
        for g in i.lower():
            if g in alphabet:
                legnt += 1
                alphabet[g] += 1

res = []

for i in alphabet.values():
    res.append(i)
res = sorted(res)
for i in res[:-6:-1]:
    for g in alphabet.keys():
        if i == alphabet[g]:
            print(g, round(((alphabet[g] * 100) / legnt), 3))
print("------------------------------")
for i in res[4::-1]:
    for g in alphabet.keys():
        if i == alphabet[g]:
            print(g, round(((alphabet[g] * 100) / legnt), 3))