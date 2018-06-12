vowels = ['a', 'e', 'i', 'o', 'u']
i = input("Enter a phrase: ")
count = 0
for letter in i:
    if letter in vowels:
        count += 1
print(count)

