number = input()
vaible = input()

reverse_num = number[::-1]
sum = int(number) + int(reverse_num)
sum1 = int(number) * int(reverse_num)

if vaible == '+':
    print(f"{number} {vaible} {int(reverse_num)} = {sum} ")
elif vaible == '*':
    print(f"{number} {vaible} {int(reverse_num)} = {sum1} ")
 
