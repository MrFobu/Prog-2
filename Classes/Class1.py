#vowel counter

input = input("Enter a word or sentence :")
vowels = ["a","e","u","i","o"]
count = 0
for x in input:
    for y in vowels:
        if x.lower() == y:
            count +=1

print(count)

