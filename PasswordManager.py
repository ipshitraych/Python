import random

let = "abcdefghijklmnopqrstuv"
num = "1234567890"
spe = "!@#$%^&*()_+-"
ser = ""
session = True

def make():
    par1 = random.sample(let, k = 5)

    for x in random.sample(par1, k = 3):
        par1[par1.index(x)] = x.upper()

    par2 = random.sample(num, k = 5)

    par3 = random.sample(spe, k = 5)

    password = par1 + par2 + par3
    random.shuffle(password)
    print("Your password is " + "".join(password))

    return "".join(password)

while session:

    prompt = input("\nGenerate a password. (1)\nStore a password (2)\nSearch (3)\nClose (4)\n")

    if prompt == "1":
        res = make()
        while True:
            user = input("\nStore? (Y/N): ")
            if user.upper() == "Y" or user.upper() == "N":
                break   
            else:
                pass
            print("Invalid input")     

        if user.upper() == "Y":

            website = input("\nEnter the name of the website: ")
            email = input("Enter your email address: ")
            com = "Website: " + website + " | Email: " + email + " | Password: " + res
            passfile = open("passwords.txt", "a")
            passfile.write("\n" + com)
            passfile.close()
            print("\nDone")

    elif prompt == "2":

        website = input("\nEnter the name of the website: ")
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        com = "Website: " + website + " | Email: " + email + " | Password: " + password
        passfile = open("passwords.txt", "a")
        passfile.write("\n" + com)
        passfile.close()
        print("\nDone")

    elif prompt == "3":

        try:
            crit = input("\nEnter search criteria: ")
            passfile = open("passwords.txt", "r")
            for y in passfile.readlines():
                if crit in y:
                    print(y)
                    ser = ser + y
            passfile.close()
            if ser == "":
                print("No matches")
        except FileNotFoundError:
            print("File does not exist")
            pass   

    elif prompt == "4":
        
        session = False

    else:
        print("Invalid option")
