import random
import time

def dice():
    player = random.randint(1,6)
    print("You rolled " + str(player) )

    ai = random.randint(1,6)
    print("The computer rolls...." )
    time.sleep(2)
    print("The computer has rolled a " + str(ai) )

    if player > ai :
       	print("You win")  # notice indentation
    elif player == ai:
    	print("Game Tie.")
    else:
        print("You lose")

    print("Quit? Y/N")
    quit = input()
    print(quit)

    if quit == "Y" or quit == "y":
    	exit()
    elif quit == "N" or quit == "n":
    	pass
    else:
    	print("I didn't understand. Let's play again.")


#main Loop
while True:
	#print("Press return to roll your die.")
	#roll = input()
	dice()
