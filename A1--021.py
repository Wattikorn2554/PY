year = int(input())

if year <= 1582:
    print('yes')
else:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("yes")
    else:
        print("no")
