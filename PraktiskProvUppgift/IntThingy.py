ammount = 0
numbers = []

def start():
    while True:
        print("\n[1] Enter number\n[2] List numbers\n")
        choice = input("What would you like to do? ")
        if (choice == "1"):
            inputNumber()
        elif (choice == "2"):
            show()
        else:
            print('\nError: Input has to be either "1" or "2"')
            continue

def inputNumber():
    while True:    
        try:
            ammount = int(input("\nHow many numbers would you like to enter? :"))
            break
        except:
            print("\nError: input has to be a number!")
            continue
    while len(numbers) < ammount:
        try:
            number = int(input("Enter a number :"))
            numbers.append(number)
        except:
            print("Error: Input has to be a number!")
            continue
def show():
    numbers.sort(reverse=True)
    print(numbers)

start()