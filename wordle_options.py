#!/usr/bin/env python3
import sys
import string

pattern = sys.argv[1].upper()
try:
    gray = sys.argv[2].upper()
except IndexError:
    gray = ''
letters_avail = [l for l in string.ascii_uppercase if l not in gray]
#if len(pattern) != 5:
#    print(f'Pattern length is {len(pattern)}; expected 5.')


def fill_dots(pattern):
    #print(pattern)
    filled = []
    if (i := pattern.find('.') ) >= 0:
        for letter in letters_avail:
            filled += fill_dots(pattern[:i] + letter + pattern[i+1:])
        return sorted(filled)
    elif (i := pattern.find('[') ) >= 0:
        j = pattern.index(']', i+1)
        for letter in letters_avail:
            if letter in pattern[i+1:j]:
                filled += fill_dots(pattern[:i] + letter + pattern[j+1:])
        return filled
    else:
        return [pattern]

def parse(pattern):
    thing = []
    i = 0
    while i < len(pattern):
        #match l :=  pattern[i]:
        l =  pattern[i]
        match l:
            case l if l in string.ascii_uppercase:
                thing.append([l])
            case '.':
                thing.append(letters_avail)
            case '[':
                j = pattern.index(']', i+1)
                thing.append([l for l in letters_avail if l in pattern[i+1:j]])
                i = j
            case _:
                raise ValueError(f'Illegal character: {l}')
        i += 1
    return thing

def fill_dots_2(thing):
    if len(thing) == 1:
        return thing[0]
    #words = []
    #for letter in thing[0]:
    #    for suffix in fill_dots_2(thing[1:]):
    #        words.append(letter + suffix)
    #return words
    return [ letter+suffix for letter in thing[0] for suffix in fill_dots_2(thing[1:]) ]


def main():
    print('\n'.join(fill_dots(pattern)))
    #print('\n'.join(fill_dots_2(parse(pattern))))

if __name__ == '__main__':
    sys.exit(main())

