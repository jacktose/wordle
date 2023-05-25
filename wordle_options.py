#!/usr/bin/env python3
from __future__ import annotations
import sys
import string
#from timeit import timeit

with open('./words_lc', 'r') as f:
    dictionary = f.read().splitlines()

#def fill_dots(pattern: str, letters_avail: iter[str]) -> list[str]:
#    filled = []
#    if (i := pattern.find('.') ) >= 0:
#        for letter in letters_avail:
#            filled += fill_dots(pattern[:i] + letter + pattern[i+1:], letters_avail)
#        return sorted(filled)
#    elif (i := pattern.find('[') ) >= 0:
#        j = pattern.index(']', i+1)
#        for letter in letters_avail:
#            if letter in pattern[i+1:j]:
#                filled += fill_dots(pattern[:i] + letter + pattern[j+1:], letters_avail)
#        return filled
#    else:
#        return [pattern]

def fill_dots_2(pattern: str, letters_avail: iter[str]) -> list[str]:
    filled = []
    for i, l in enumerate(pattern):
        if l == '.':
            for letter in letters_avail:
                filled += fill_dots_2(pattern[:i] + letter + pattern[i+1:], letters_avail)
            return filled
        elif l == '[':
            j = pattern.index(']', i+1)
            for letter in letters_avail:
                if letter in pattern[i+1:j]:
                    filled += fill_dots_2(pattern[:i] + letter + pattern[j+1:], letters_avail)
            return filled
    else:
        return [pattern]

#def fill_dots_3(pattern: str, letters_avail: iter[str]) -> list[str]:
#    for i, l in enumerate(pattern):
#        if l == '.':
#            return [word \
#                    for letter in letters_avail \
#                    for word in fill_dots_3(pattern[:i] + letter + pattern[i+1:], letters_avail)
#                   ]
#        elif l == '[':
#            j = pattern.index(']', i+1)
#            return [word \
#                    for letter in letters_avail if letter in pattern[i+1:j] \
#                    for word in fill_dots_3(pattern[:i] + letter + pattern[j+1:], letters_avail)
#                   ]
#    else:
#        return [pattern]
#    
#def fill_dots_4(pattern: str, letters_avail: iter[str]) -> list[str]:
#    for i, l in enumerate(pattern):
#        if l == '.':
#            options = letters_avail
#            suffix = pattern[i+1:]
#        elif l == '[':
#            j = pattern.index(']', i+1)
#            options = [letter for letter in letters_avail if letter in pattern[i+1:j]]
#            suffix = pattern[j+1:]
#        else:
#            continue
#        return [word for letter in options for word in fill_dots_4(pattern[:i] + letter + suffix, letters_avail)]
#    else:
#        return [pattern]
#
#def fill_dots_5(pattern: str, letters_avail: iter[str]) -> list[str]:
#    pointer = 0
#    letters = []
#    while pointer < len(pattern):
#        if pattern[pointer] in string.ascii_uppercase:
#            letters.append([pattern[pointer]])
#        elif pattern[pointer] == '.':
#            letters.append(string.ascii_uppercase)
#        elif pattern[pointer] == '[':
#            close = pattern.find(']', pointer+1)
#            letters.append(sorted(pattern[pointer+1:close]))
#            pointer = close
#        else:
#            raise ValueError(f'Invalid character: {pattern[pointer]}')
#        pointer += 1
#
#    print(letters)
#    breakpoint()
#
#    #TODO: letters -> words
#
#    return words


def main():
    pattern = sys.argv[1].upper()
    try:
        gray = sys.argv[2].upper()
    except IndexError:
        gray = ''
    letters_avail = [l for l in string.ascii_uppercase if l not in gray]

    if len(sys.argv) > 3 and sys.argv[3] == '--filter':
        real_words_only = True
    else:
        real_words_only = False

    options = fill_dots_2(pattern, letters_avail)
    if real_words_only:
        options = [w for w in options if w.lower() in dictionary]
    print('\n'.join(options))

    #results = {}
    #for f in [
    #    #fill_dots,
    #    fill_dots_2,
    #    fill_dots_3,
    #    fill_dots_4,
    #    #fill_dots_5,
    #]:
    #    results[f] = f(pattern, letters_avail)
    #    print(f)
    #    #print(results[f])
    #    print(timeit('f(pattern, letters_avail)', globals=locals(), number=10_000))
    #breakpoint()
# end main

if __name__ == '__main__':
    sys.exit(main())

