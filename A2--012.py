n = list(map(int, input().split()))

carrot,cabbage,tomato = n[0],n[1],n[2]

pcarrot=10
pcabbage=20
ptomato=30


total = (carrot*pcarrot) + (cabbage*pcabbage) +( tomato*ptomato)
print(total)