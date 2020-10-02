# write your code here
with open("salary.txt") as month, \
        open("salary_year.txt", "a") as year:
    for line in month:
        line.rstrip("\n")
        line_year = int(line) * 12
        result = str(line_year) + "\n"
        year.write(result)
