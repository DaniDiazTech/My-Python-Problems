number_of_input = int(input())
divisible_by_seven = []
useful_variable = 0

for _ in range(number_of_input):
    useful_variable = int(input())
    if useful_variable % 7 == 0:
        divisible_by_seven.append(useful_variable)
    else:
        continue

for square in divisible_by_seven:
    print(square ** 2)
