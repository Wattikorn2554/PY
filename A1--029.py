vowels="aeiou"
animal = input()
count = 0

for letter in animal:
    if letter in vowels:
        count += 1
print(count)

