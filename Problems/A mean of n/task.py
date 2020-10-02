import statistics as s
iterator = int(input())
numbers = []
for i in range(iterator):
    n = int(input())
    numbers.append(n)
    i += 1

print(float(s.mean(numbers)))
