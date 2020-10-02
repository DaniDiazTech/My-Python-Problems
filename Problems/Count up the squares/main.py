my_sum = 0
square_sum = []
while True:
    number = int(input())
    square_sum.append(number ** 2)
    my_sum += number
    if my_sum == 0:
        print(sum(square_sum))
        break
