#!/usr/bin/python

input_file = 'input'

total_fuel = 0

with open(input_file) as fp:
    line = fp.readline()
    while line:
        this_fuel = int((int(line) / 3.0) - 2)
        total_fuel += this_fuel
        line = fp.readline()

print(total_fuel)
