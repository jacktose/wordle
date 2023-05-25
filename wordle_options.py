#!/usr/bin/env python3
from __future__ import annotations
import sys
import string

def fill_dots(pattern: str, letters_avail: iter[str]) -> list[str]:
    filled = []
    for i, l in enumerate(pattern):
        if l == '.':
            for letter in letters_avail:
                filled += fill_dots(pattern[:i] + letter + pattern[i+1:], letters_avail)
            return filled
        elif l == '[':
            j = pattern.index(']', i+1)
            for letter in letters_avail:
                if letter in pattern[i+1:j]:
                    filled += fill_dots(pattern[:i] + letter + pattern[j+1:], letters_avail)
            return filled
    else:
        return [pattern]

def main():
    # parse input
    # TODO: switch to argparse or something
    pattern = sys.argv[1].upper()
    try:
        gray = sys.argv[2].upper()
    except IndexError:
        gray = ''
    if len(sys.argv) > 3 and sys.argv[3] == '--filter':
        real_words_only = True
    else:
        real_words_only = False

    # generate possibilities:
    letters_avail = [l for l in string.ascii_uppercase if l not in gray]
    options = fill_dots(pattern, letters_avail)

    # filter:
    if real_words_only:
        with open('./words_lc', 'r') as f:
            dictionary = f.read().splitlines()
        options = [w for w in options if w.lower() in dictionary]

    # output:
    print('\n'.join(options))

# end main

if __name__ == '__main__':
    sys.exit(main())

