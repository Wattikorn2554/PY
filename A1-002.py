c = int(input())
ch = 0                    
 
ch = c % 10
c =  c // 10
print("10 =", c)

c = ch // 5
ch = ch % 5
print("5 =", c)

c = ch // 2
ch = ch % 2
print("2 =", c)

c = ch // 1
ch = ch % 1
print("1 =", c)