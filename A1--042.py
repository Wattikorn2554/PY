N = int(input())
A = int(input())
totaltime = N * A

if totaltime ==0:
    print("No teaching")
else:
    hours = totaltime // 60
    minutes = totaltime % 60
if totaltime == 0:
    print("No teaching")
elif hours > 0 and minutes > 0:
    print(f"{hours}hours{minutes}minutes")
elif hours >0:
    print(f"{hours}hours")
else:
    print(f"{minutes}minutes")