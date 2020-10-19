import re


file = "regex_sum_42.txt"
handle = open(file)

lines = list()
count = 0
total = 0
for line in handle:
    line = line.rstrip()
    for lines = re.findall('[0-9]',line):
        number = count + 1
        totalnumber = total + lines
    print(lines)
