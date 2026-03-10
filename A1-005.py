#input
m1 = int(input())
d1 = int(input())

#process
if m1 <= 3:
    if m1 == 3  and d1 >= 21:
        season = "spring"
        print(season)
    else:
        season = "winter"
        print(season)

if m1 > 3 and  m1 <= 6:
    if m1 == 6  and d1 >= 21:
        season = "summer"
        print(season)
    else:
        season = "spring"
        print(season)

if m1 > 6 and  m1 <= 9:
    if m1 == 9  and d1 >= 21:
        season = "fall"
        print(season)
    else:
        season = "summer"
        print(season)

if m1 > 9 and  m1 <= 12:
    if m1 == 12  and d1 >= 21:
        season = "winter"
        print(season)
    else:
        season = "fall"
        print(season)       