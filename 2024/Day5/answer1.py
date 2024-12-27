data = open("data.txt", "r")
text = data.readlines()
rules, pages = text[:text.index("\n")], text[text.index("\n")+1:]

correct = []
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
        continue
    correct.append(page)

total = 0
for i in correct:
    total = total + int(i[int((len(i)-1)/2)])

print(total)