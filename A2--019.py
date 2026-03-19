text = input()
text_up = text.upper()
max_U = 0

for i in range(len(text)) :
    if text[i] == 'B' :
        current_U = 0
        
        for j in range( i + 1, len(text_up)) :
            if text_up[j] == 'U':
                current_U += 1
            else:
                break
        
        max_U = max(max_U, current_U)
        
if max_U >= 2:
    print(f'Yes {max_U}')
elif 'B' in text_up :
    where_B = text_up.find('B')
    result = text[:where_B + 1] + ( 'U' * (len(text) - where_B - 1))
    
    print(result)
else:
    word = 'BUU' * 3
    print(word[:len(text)])
        