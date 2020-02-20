#!/usr/bin/python

def calc_fuel(input):
    fuel = int((int(input) / 3.0) - 2)
    if (fuel <= 0.0):
        return 0
    else:
        return fuel + calc_fuel(fuel)

input_file = 'input'
total_fuel = 0

with open(input_file) as fp:
    line = fp.readline()
    while line:
        total_fuel += calc_fuel(int(line))
        line = fp.readline()

print(total_fuel)
