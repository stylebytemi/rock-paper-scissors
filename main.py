import random

name = input('What is your name? \n')
print("Welcome" + ' ' + name + ' ' + "to ZURI Rock-Paper-Scissors Game")
print("\n")

print("Take note of the symbols below")
print(" R = Rock \n", "P = Paper \n", "S = Scissors \n")
print("\n")

while True:
    choices = ["R", "P", "S"]

    CPU = random.choice(choices)
   
    Player = input( name + " " + "choose  between R , P, or S?:").upper()
    
   
    if Player not in choices: 
        print('Error, input again')

    # if Player == CPU:
    #     if count < 3: 
    #         print("Player " "(" + Player  + ")" " : CPU " + "(" + CPU  + ")")
    #         print("It's a tie, play again")
    #         count = count+1
    #     else:
    #         print("Player " "(" + Player  + ")" " : CPU " + "(" + CPU  + ")")
    #         print("you have exceeded your 3 tie attempts")
    #         break

    if Player == CPU:
        print("Player " "(" + Player  + ")" " : CPU " + "(" + CPU  + ")")
        print("It's a tie, play again")

    elif Player == "R":
        if CPU == "S":
            print("Player " "(" + Player  + ")" " : CPU " + "(" + CPU  + ")")
            print(name + " " + "wins 🏆")
            break
        if CPU == "P":
            print("Player " "(" + Player  + ")" " : CPU " + "(" + CPU  + ")")
            print("CPU wins 🏆")
            break

    elif Player == "P":
        if CPU == "R":
            print("Player " "(" + Player  + ")" " : CPU " + "(" + CPU  + ")")
            print(name + " " + "wins 🏆")
            break
        if CPU == "S":
            print("Player " "(" + Player  + ")" " : CPU " + "(" + CPU  + ")")
            print("CPU wins 🏆")
            break

    elif Player == "S":
        if CPU == "P":
            print("Player " "(" + Player  + ")" " : CPU " + "(" + CPU  + ")")
            print(name + " " + "wins 🏆")
            break
        if CPU == "R":
            print("Player " "(" + Player  + ")" " : CPU " + "(" + CPU  + ")")
            print("CPU wins 🏆")
            break
    