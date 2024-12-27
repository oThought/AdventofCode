data = open("data.txt", "r")
text = data.readlines()
rules, pages = text[:text.index("\n")], text[text.index("\n")+1:]

for r in range(len(rules)):
    rules[r] = rules[r].replace("\n", "")

incorrect = []
for p in pages:
    c = True
    page = p.replace("\n", "").split(",")
    for n in page:
        for r in rules:
            if r.find(n) == 0:
                try:
                    if page.index(r[3:]) < page.index(n):
                        c = False
                        break
                except ValueError:
                    pass
            if r.find(n) == 3:
                try:
                    if page.index(r[:2]) > page.index(n):
                        c = False
                        break
                except ValueError:
                    pass
    if not c:
        incorrect.append(page)
        continue

for i in incorrect:
    j = incorrect.index(i)
    for l in range(10):
        for r in rules:
            try:
                a, b = i.index(r[3:]), i.index(r[:2])
                if a < b:
                    incorrect[j][a], incorrect[j][b] = i[b], i[a]
            except ValueError:
                pass
    
total = 0
for i in incorrect:
    total = total + int(i[int((len(i)-1)/2)])

print(total)