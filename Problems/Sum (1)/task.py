# read sums.txt
file = open("sums.txt")
for line in file:
    line_as_list = line.split()
    print(int(line_as_list[0]) + int(line_as_list[1]))
file.close()
