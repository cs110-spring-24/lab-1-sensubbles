import random
cpu = random.randint(1, 3)
points = 0
player = input("rock, paper, or scissors: ")
if player == "rock":
	print("you chose rock, good luck!")
	if cpu == 1:
		print("you're against rock, it's a tie!")
	elif cpu == 2:
		print("you're against paper, you lose...")
	else:
		print("you're against scissors, you win!")
		points= points + 1
		print("you have", points, "win(s)")

if player == "paper":
	print("you chose paper, good luck!")
	if cpu == 1:
		print("you're against rock, you win!")
		points= points + 1
		print("you have", points, "win(s)")
	elif cpu == 2:
		print("you're against paper, it's a tie!")
	else:
		print("you're against scissors, you lose...")
if player == "scissors":
	print("you chose scissors, good luck!")
	if cpu == 1:
		print("you're against rock, you lose...")
	elif cpu == 2:
		print("you're against paper, you win!")
		points= points + 1
		print("you have", points, "win(s)")
	else:
		print("you're against scissors, it's a tie!")