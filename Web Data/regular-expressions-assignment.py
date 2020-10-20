import re


file = "regex_sum_995413.txt"
handle = open(file)

lines = list()
count = 0
total = 0
number = int()
for line in handle:
    line = line.rstrip()
    data = re.findall('(\s?[0-9]+\s?)',line)
    
    if len(data) != 0: 
        for num in data:
            total = total + int(num)
            count = count + 1


print(total)        
print(count)

