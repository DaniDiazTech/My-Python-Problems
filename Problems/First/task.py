# read test_file.txt
file = open("test_file.txt", encoding="utf-16")
for lines in file:
    print(lines)
    break
file.close()