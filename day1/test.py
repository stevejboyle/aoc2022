#!/usr/bin/env python

with open("input.txt", "r") as input_line:
    max_elf = 0
    cur_elf = 0

    max_val = 0
    cur_val = 0
    for line in input_line:
        if line.strip() == "":
            if cur_val > max_val:
                max_elf = cur_elf
                max_val = cur_val
            cur_val = 0
        else:
            cur_val += int(line)
    print(max_val)
