#!/usr/bin/env python

with open("input.txt", "r") as input_line:
    grand_total = 0
    elf_list = []
    i = 0

    elf_list.append(0)
    for line in input_line:
        if line.strip() == "":
            i += 1
            elf_list.append(0)
        else:
            elf_list[i] += int(line)
    elf_list.sort()
    grand_total = sum(elf_list[-3:])
    print(grand_total)
