f = open("Data.txt", "r")
data = f.readlines()

hands, bids, types, rank = [], [], [], []
cards = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "Q": 11, "K": 12, "A": 13}
for line in data:
    hand, bid = line.split()
    hands.append(hand)
    bids.append(bid)

def joker(hand):
    while hand.find("J") != -1:
        a, b, c, d, e = hand.count(hand[0]), hand.count(hand[1]), hand.count(hand[2]), hand.count(hand[3]), hand.count(hand[4])
        joker = {a: 0, b: 1, c: 2, d: 3, e: 4}
        f = max([a, b, c, d, e])
        hand = [*hand]
        hand[[*hand].index("J")] = hand[joker[f]]
        hand = "".join(hand)
    return hand

for hand in range(len(hands)):
    hands[hand] = joker(hands[hand])

def checktype(h):
    if h.count(h[0]) == 5:
        type = "Five"
    elif h.count(h[0]) == 4 or h.count(h[1]) == 4:
        type = "Four"
    elif h.count(h[0]) == 3 or h.count(h[1]) == 3 or h.count(h[2]) == 3:
        if h.count(h[0]) == 2 or h.count(h[1]) == 2 or h.count(h[2]) == 2 or h.count(h[3]) == 2 or h.count(h[4]) == 2:
            type = "Full"
        else:
            type = "Three"
    elif [h.count(h[0]), h.count(h[1]), h.count(h[2]), h.count(h[3]), h.count(h[4])].count(2) == 4:
        type = "TwoPair"
    elif [h.count(h[0]), h.count(h[1]), h.count(h[2]), h.count(h[3]), h.count(h[4])].count(2) == 2:
        type = "OnePair"
    else: 
        type = "HighCard"
    return type

def customSort(i):
    if i[0] == "Five":
        return 6
    elif i[0] == "Four":
        return 5
    elif i[0] == "Full":
        return 4
    elif i[0] == "Three":
        return 3
    elif i[0] == "TwoPair":
        return 2
    elif i[0] == "OnePair":
        return 1
    return 0
def customSortTwo(i):
    output = 0
    for j in range(5):
        if j == 0:
            output += 10000000000*cards[i[1][j]]
        elif j == 1:
            output += 10000000*cards[i[1][j]]
        elif j == 2:
            output += 10000*cards[i[1][j]]
        elif j == 3:
            output += 100*cards[i[1][j]]
        elif j == 4:
            output += cards[i[1][j]]
    return output
    
for h in range(len(hands)):
    types.append([checktype(hands[h]), hands[h], bids[h]])
types.sort(reverse=True, key=customSort)

five, four, full, three, two, one, high = [], [], [], [], [], [], []
for type in types:
    if type[0] == "Five":
        five.append(type)
    elif type[0] == "Four":
        four.append(type)
    elif type[0] == "Full":
        full.append(type)
    elif type[0] == "Three":
        three.append(type)
    elif type[0] == "TwoPair":
        two.append(type)
    elif type[0] == "OnePair":
        one.append(type)
    elif type[0] == "HighCard":
        high.append(type)

types = []
for t in [five, four, full, three, two, one, high]:
    t.sort(reverse=True, key=customSortTwo)
    if t != []:
        for l in t:
            types.append(l)

final = 0
for o in range(len(types)):
    rank = len(types) - o
    output = rank * int(types[o][2])
    final += output
    print(output, rank, types[o])

print(final)
