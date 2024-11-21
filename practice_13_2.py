import fileinput
res_w = []
res_m = []

with fileinput.input(files=[(f"years\yob{i}.txt") for i in range(1880, 2020)]) as file:
    for line in file:
            if file.filelineno() == 1:
                if "F" in line.split(","):
                    f = line.split(",")
                    res_w.append(f[0])
            if file.filelineno() > 1:
                if "F" in line.split(","):
                    id = file.filelineno()
            
            if id == file.filelineno() - 1:
                if "M" in line.split(","):
                    f = line.split(",")
                    res_m.append(f[0])

sp = []
for g in set(res_m):
    sp.append((res_m.count(g), g))
sp = sorted(sp)
for i, x in sp[::-1]:
    print(x, i)
print("----------------------------")
sp = []
for g in set(res_w):
    sp.append((res_w.count(g), g))
sp = sorted(sp)
for i, x in sp[::-1]:
    print(x, i)
                 