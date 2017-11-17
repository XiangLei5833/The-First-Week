#!/usr/bin/env python3

def char_count(str):
    char_dict = {}
    for char in str:
        c = char_dict.get(char)
        if c == None:
           char_dict[char] = 1
        else:
           char_dict[char] += 1
    print(char_dict)

if __name__ == '__main__':
    s = input('Enter a string:')
    char_count(s)
