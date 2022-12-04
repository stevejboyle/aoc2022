#!/usr/bin/env python

with open("input.txt", "r") as input_line:
    tot = 0

    for line in input_line:
        e1, e2 = line.split(',')
        l1, u1 = e1.split('-')
        l2, u2 = e2.split('-')

        l1 = int(l1)
        u1 = int(u1)
        l2 = int(l2)
        u2 = int(u2)

        if (l1 <= l2 and u1 >= u2) or (l2 <= l1 and u2 >= u1):
            tot += 1
    print(tot)
