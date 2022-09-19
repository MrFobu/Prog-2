def calculate(*args):
    sum = 0
    for x in args:
        sum += x
    print(sum)

def food(s,vegan = False):
    if (vegan == False):
        print(s)
    else:
        print("soja" + s)

calculate(12,5,6,7)
calculate(5,2,1)

food("mjölk")
food("mjölk", True)