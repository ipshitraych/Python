import random

pscore = 0
bscore = 0
play = 0
game = True

pchoice = {"ROCK": 1,"PAPER": 2,"SCISSORS": 3}
bchoice = {1: "ROCK", 2: "PAPER", 3: "SCISSORS"}

print("Rock, paper, scissors")
rounds = int(input("Choose the number of rounds: "))

while game:

    pinput = input("\nThrow: ")
    pla = pchoice[pinput.upper()]

    bot = random.choice(range(1, 3))
    print("I choose" ,bchoice[bot])

    con = bot - pla
    if con == -1 or con == 2:
        print("Round won")
        pscore += 1
    elif con == 1 or con == -2:
        print("Round lost")
        bscore +=1
    else:
        print("Round drawn")

    play += 1
    
    if rounds/2 < bscore :
        game = False
        print("\nBOT wins the game")
    elif rounds/2 < pscore:
        game = False
        print("\nPLAYER wins the game")

    if rounds == play:
        game = False
        if pscore > bscore:
            print("\nPLAYER wins the game")
        elif bscore > pscore:
            print("\nBOT wins the game")
        elif pscore - bscore == 0:
            print("\nThe game ends in a draw")
