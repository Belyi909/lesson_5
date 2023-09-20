a = input("")
count = 0
x = "a", "e", "i", "o", "u", "y"
for letter in a:
    if letter in x:
        count += 1
print(count)
count = 0
for letter in a:
    if letter not in x:
        count += 1
print(count)