#name = "mbox-short.txt"


handle = open("mbox-short.txt")
time = list()
hours = list()
for line in handle :
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    time.append(words[5])

for line in time:
    hour = (line.split(':'))
    hours.append(hour[0])


# we have a list hours that needs to be made into a dictionary with the hour as key, and count as value
# dictionary is hours_dict

hours_dict = dict()
hour_count = int()
hour_name = str()

for counter in hours :
    hours_dict[counter] = hours_dict.get(counter,0) + 1


hours_lst = list()
newtup = tuple()

#x = sorted(hours_dict.items())
#for key,value in x:
#    print(key,value)

for key,value in hours_dict.items():
    newtup = (key,value)
    hours_lst.append(newtup)

hours_lst = sorted(hours_lst)

for key,value in hours_lst:
    print(key,value)
