import time
class Student():
    def __init__(self, name, age, passed):
        self.name = name
        self.age = age
        if passed.casefold() == "yes":
            self.passed = True
            self.mood = "Happy"
        else:
            self.passed = False
            self.mood = "Sad"

students = [Student("kim",17,"yes"),Student("Peter",16,"no")]

while True:
    print("Welcome to the student database, what would you like to do?")
    print("[1] Add new student\n[2] Wiev students")
    selection = input("Select :")
    if selection == "1":
        print("Adding new student.")
        name = input("Enter name :")
        while True:
            age = input("Enter age :")
            try:
                int(age)
                break
            except:
                print("Error: Input must be a number.")
                continue
        while True:
            passed = input("Has the student passed? [yes/no]:")
            if passed.casefold() == "yes" or passed.casefold() == "no":
                break
            else:
                print('Error: Input has to be either "yes" or "no"')
                continue
        student = Student(name, age, passed)
        students.append(student)
        print("\nStudent was succesfully  added.")
        time.sleep(2)
    elif selection == "2":
        if len(students) <= 0:
            print("\nThere are currently no students.")
            time.sleep(1)
        else:
            for x in students:
                print(f"\nStudent: {x.name}\nAge: {x.age}\nPassed: {x.passed}\nMood: {x.mood}\n")
            input("Press enter to go back to start.")
    else:
        print("Something went wrong, try again.")
        continue
