fname = input()
lname = input()
age   = input()

if len(fname) > 5 and len(lname) > 5:  
    print(f"{fname[0:2]}{lname[-1]}{age[-1]}")
else:
    print(f"{fname[0:1]}{age}{lname[-1]}")
  