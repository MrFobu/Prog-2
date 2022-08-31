#1, Gör ett program som skriver ut alla tal under 1000 some är jämt delbara med 7.
"""
x = 0
while x < 1000:
    x += 1
    if x % 7 === 0:
        print(x)
"""
#2, Gör ett program som räknar antalet siffror i en godtycklig inmatad text sträng.

text = input("Write something! :")
count = 0
for x in text:
    try:
        int(x)
        count +=1
    except:
        continue
print(count)