deck = input().split()
num_shuffles = int(input())

l = len(deck)
cut = int(l / 2)
for i in range(num_shuffles):
    new_deck = []
    for j in range(cut):
        deck.append(deck[j])
        deck.append(deck[j + cut])

    deck = new_deck

print(deck)
