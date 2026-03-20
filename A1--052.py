money = int(input())
count = 0



if 100 <= money <= 20000 and money % 100 == 0:
     count = money // 1000
     if count > 0:
         print("1000 =", count)
         money = money % 1000
          
          
     count = money // 500
     if count > 0:       
         print("500 =", count)
         money = money % 500
         
     count = money // 100      
     if count > 0: 
         print("100 =", count)
         money = money % 100
                      
else:
    print("ERROR")      
    

      