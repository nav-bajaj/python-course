#Assignment Lines

fname = input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print("File name entered incorrectly: ",fname)
    quit()

line_upper = fhandle.read()
line_upper.rstrip()
print(line_upper.upper())
