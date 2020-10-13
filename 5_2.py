largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        number = int(num)
        if number> largest:
            largest = number

        if smallest is None:
            smallest = number
        elif number<smallest:
            smallest = number



    except:
        if num == "done" :
            break
        else:
            print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
