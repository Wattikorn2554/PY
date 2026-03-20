num  = int(input())
scores = []

for _ in range(num):
    score = int(input())
    scores.append(score)
if num > 0:
    max_score = max(scores)
    count_top = scores.count(max_score)
    print(max_score)
    print(count_top)
    
    

11