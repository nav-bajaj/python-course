fname = "romeo1.txt"
fh = open(fname)
str = fh.read()

lst = str.split()
new_lst = list()
print(lst)

for word in lst:
    if word not in new_lst:
        new_lst.append(word)

new_lst.sort()
print(new_lst)


