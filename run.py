print("███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██████╗ ███████╗██████╗ ")
print("██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██╔══██╗██╔════╝██╔══██╗")
print("█████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██████╔╝█████╗  ██████╔╝")
print("██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██╔══██╗██╔══╝  ██╔══██╗")
print("███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║  ██║███████╗██║  ██║")
print("╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")

print('_.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"')

name = input("Please enter your name here: ")
print(f'Welcome explorer {name}!')

startGame = input("Are you ready to go on an historic adventure?")
if startGame == "yes":
    print("Amazing! Looking forward to go down the adventure path with you!")
    print("In this adventure game you will have the opportunity to go back!")
    world = input("Visit the 'Vikings' or the ancient 'Roman Empire'?")
elif startGame == "no":
    print("Too bad, you're missing out! Refresh page to restart!")
    quit()
else:
    print("Invalid response, try answering 'yes' or 'no'")