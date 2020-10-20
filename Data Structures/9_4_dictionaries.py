fname = input("Enter File Name: ")  


handle = open(fname)
senders = list()

for line in handle :
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    senders.append(words[1])




counts = dict()
bigsender = int()
bigsendername = str()

for max_sender in senders :
    counts[max_sender] = counts.get(max_sender,0) + 1
    if bigsender is None or bigsender < counts[max_sender]:
        bigsender = counts[max_sender]
        bigsendername = max_sender


print(bigsendername, bigsender)

