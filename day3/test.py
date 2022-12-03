#!/usr/bin/env python

with open("input.txt", "r") as input_line:
    tot = 0
    val = 0

    for line in input_line:
        sack = list(line.strip())
        h1 = sack[:len(sack)//2]
        h2 = sack[len(sack)//2:]
        res = set(h1).intersection(h2)
        x = res.pop()
        if x >= 'a' and x <= 'z':
            val = ord(x) - ord('a') + 1
        else:
            val = (ord(x) - ord('A') + 1)+26
        tot += val
        val = 0
    print(tot)
