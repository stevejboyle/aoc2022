#!/usr/bin/env python

with open("input.txt", "r") as input_line:
    tot = 0
    val = 0
    idx = 1

    for line in input_line:
        sack = list(line.strip())
        if idx == 1:
            h1 = sack
            idx = 2
        elif idx == 2:
            h2 = sack
            idx = 3
        else:
            h3 = sack
            idx = 1
            res = set(h1).intersection(h2).intersection(h3)
            x = res.pop()
            if x >= 'a' and x <= 'z':
                val = ord(x) - ord('a') + 1
            else:
                val = (ord(x) - ord('A') + 1)+26
            tot += val
            val = 0
    print(tot)
