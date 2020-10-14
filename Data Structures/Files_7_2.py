# Use the file name mbox-short.txt as the file name



fname = input("Enter file name: ")

fh = open(fname)
total_int = 0.0
count_int = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        ipos = line.find(":")+1
        val= float(line[ipos:].strip())
        total_int = total_int + val
        count_int = count_int + 1


average = total_int/count_int
print("Average spam confidence:", average)
