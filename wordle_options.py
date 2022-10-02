#!/usr/bin/env python3
import sys
import string

print(sys.argv)
#pattern = '.a.nt'.upper()
#gray = 'cremls'.upper()
pattern = sys.argv[1].upper()
try:
    gray = sys.argv[2].upper()
except IndexError:
    gray = ''
letters_avail = [l for l in string.ascii_uppercase if l not in gray]
if len(pattern) != 5:
    print(f'Pattern length is {len(pattern)}; expected 5.')


def fill_dots(pattern):
    if '.' not in pattern:
        return [pattern]
    i = pattern.find('.')
    filled = []
    for letter in letters_avail:
        filled += fill_dots(pattern[:i] + letter + pattern[i+1:])
    return filled


def main():
    print('\n'.join(fill_dots(pattern)))

if __name__ == '__main__':
    sys.exit(main())

