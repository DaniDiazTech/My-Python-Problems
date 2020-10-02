# read sample.txt and print the number of lines
file = open("sample.txt", "r")
len_of_file = file.readlines()
print(len(len_of_file))
file.close()
