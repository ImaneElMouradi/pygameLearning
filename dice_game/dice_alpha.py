import random

player = random.randint(1,6)
ai = random.randint(1,6)

if player > ai :
	print("You win")  # notice indentation
else:
	print("You lose")