line = int(input())
ans = ( 35 + ((line-1) *5))
ans2= ( 80  + ((line-10) *8))
if line <= 1:
    print(35)
elif 1 <= line < 10 or line == 10:
    print(ans)  
elif line > 10:
    print(ans2)
   