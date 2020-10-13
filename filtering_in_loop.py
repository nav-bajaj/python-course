#filtering out even numbers in an array and summing even ones

count = 0
evensum = 0
for array in [23,4,56,3,12,8,7,33456,4343124621]:
    if array%2==0:
        count = count+1
        evensum= evensum+array

        print(array, "This is even ")
    else:
        print(array, "This is odd")

print("Sum of even numbers",evensum, "Number of even numbers:",count)
