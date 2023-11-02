print("███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██████╗ ███████╗██████╗ ")
print("██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██╔══██╗██╔════╝██╔══██╗")
print("█████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██████╔╝█████╗  ██████╔╝")
print("██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██╔══██╗██╔══╝  ██╔══██╗")
print("███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║  ██║███████╗██║  ██║")
print("╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")

print('_.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"')

name = input("Please enter your name here:\n")
print(f'Welcome explorer {name}!')

startGame = input("Ready to go on an historic adventure? 'yes' or 'no'\n")
if startGame == "yes":
    print("Amazing! Looking forward to go down the adventure path with you!")
    print("In this adventure game you will have the opportunity to go back!")
    world = input("Visit the 'Vikings' or the ancient 'Roman Empire'?\n")
elif startGame == "no":
    print("Too bad, you're missing out! Refresh page to restart!")
    quit()
else:
    print("Invalid response, try answering 'yes' or 'no'")

print('_.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"')

if world == "vikings":
    print("You see yourself transported to the far north of Europe.")
    print("It's green and lucious during a beautiful spring day.")
    print("In one direction you see a boat but the other direction is a farm.")
    landingVikings = input("Take the 'boat' or go to the 'farm'?\n")