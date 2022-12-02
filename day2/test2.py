#!/usr/bin/env python

with open("input.txt", "r") as input_line:
    total = 0

    for line in input_line:
        score = 0
        a, b = line.split(' ', 1)
        b = b.rstrip()
        if a == 'A':
            score += 1
        elif a == 'B':
            score += 2
        elif a == 'C':
            score += 3

        if b == 'Y':
            score += 3
        elif b == 'Z':
            score += 6

        total += score
    print(total)
