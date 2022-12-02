#!/usr/bin/env python

with open("input.txt", "r") as input_line:
    total = 0

    for line in input_line:
        score = 0
        a, b = line.split(' ', 1)
        b = b.rstrip()
        if b == 'X':
            score += 1
            if a == 'C':
                score += 6
            elif a == 'A':
                score += 3
        elif b == 'Y':
            score += 2
            if a == 'A':
                score += 6
            elif a == 'B':
                score += 3
        elif b == 'Z':
            score += 3
            if a == 'B':
                score += 6
            elif a == 'C':
                score += 3
        total += score
    print(total)
