num1 = int(input())
num2 =list(map(int , input()))

result = []

for x in num2:
    if num2.count(x) == 1:
        result.append(x)
        
result.sort()

if result:
    print(*result)
else:
    print()
               