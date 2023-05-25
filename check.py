#!/usr/bin/env python3

#WORK IN PROGRESS!

targets = [(t[0], t[1]) for t in ('bl', 'ch', 'dg', 'dr', 'lv', 'no', 'rv', 'st', 'us')]
#print(targets)

with open('./words_lc', 'r') as f:
    words = {w.rstrip(): 0 for w in f.readlines() if len(w) == 6}
#print(list(words.keys())[:10])

for word in words:
    for target in targets:
        if target[0] in word or target[1] in word:
            words[word] += 1

best = max(words.values())
print('\n'.join(word for word, score in words.items() if score == best))
