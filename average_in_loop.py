#average in a loop

sum = 0
counter = 0

for array in [5,14,3,45,77,32]:
    counter=counter+1
    sum=sum+array
    print(counter,"  ",array,"  Sum right now:  ", sum)

print("Items: ",counter)
print("Total: ", sum)
print("Mean: ",sum/counter)
