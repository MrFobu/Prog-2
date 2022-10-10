import classes

fish = classes.Salmon()
fish.max_depth = 2000
fish.speed = 29
shark = classes.Shark()
shark.max_depth = 2000

def catch(fish,shark):
    if (fish.speed < 30):
        if (fish.max_depth >= shark.max_depth):
            print("true")
        else:
            print("false")
    else:
        print("false")


catch(fish,shark)