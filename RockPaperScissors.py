import random

res = 0
pscore = 0
cscore = 0
play = 0
game = True
prompt = True

pchoice = {"ROCK": 1,"PAPER": 2,"SCISSORS": 3}
cchoice = {1: "ROCK", 2: "PAPER", 3: "SCISSORS"}

print("Rock, paper, scissors")

while prompt:

    rounds = int(input("Choose the number of rounds: "))

    while game:

        pinput = input("\nThrow: ")
        pla = pchoice[pinput.upper()]

        bot = random.choice(range(1, 3))
        print("I choose" ,cchoice[bot])

        con = bot - pla
        if con == -1 or con == 2:
            print("Round won")
            pscore += 1
        elif con == 1 or con == -2:
            print("Round lost")
            cscore +=1
        else:
            print("Round drawn")

        play += 1
        
        if rounds/2 < cscore :
            game = False
            res = -1
        elif rounds/2 < pscore:
            game = False
            res = 1

        if rounds == play:
            game = False
            if pscore > cscore:
                res = 1
            elif cscore > pscore:
                res = -1    
            elif pscore - cscore == 0:
                res = 0
                
    if res == 1:
        print("\nPLAYER wins the game")
    elif res == 0:
        print("\nThe game ends in a draw")
    else:
        print("\nCOMP wins the game")

    choice = input("\nAnother game? (Y/N) ")
    if choice == "N":
        prompt = False
    else:
        game = True
        play = 0 
