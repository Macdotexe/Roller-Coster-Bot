
name = str()

person = str()

can_enter = bool()

height = int()

age = int()

while True:
    print("\n" * 100)
    name = str(input("What is your name? (type q to quit) \n"))
    #ask name

    if name == "q":
        exit()
        #check if we should quit

    print("Hello " + name + "! Welcome to the world fastest roller coster! Lets start your registiration, i will ask a few questions and you will answer! \n\n\n")
    #greet user

    height = int(input("What is your height? \n"))
    #ask height and assign to height

    age = int(input("How old are you? \n"))
    #ask age and assign it to age

    if age < 10 or height < 140:
        print("sorry you are not able to ride:(")
        can_enter = False
        input()
    elif age >= 10 and height >= 140:
        print("Ok " + name + ", have fun!")
        can_enter = True
        input()
        #caculate if able to ride and set can_enter accordingly

    person = "Name: " + name + """
    Height: """ + str(height) + """
    Age: """ + str(age) + """
    
    
    """
    #assign all info to person

    file = open("People.txt", "a")
    file.write(str(person))
    file.close()
    #write info to People.txt
        
