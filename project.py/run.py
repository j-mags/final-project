import game
quit = ('quit','q')
start = ('start','s')
choice = ''
while choice not in quit:
	choice = input("Would you like to begin?\n").lower()
	print("Start (s)\nQuit (q)")
		if choice in start:
			print("Good luck!")
			project.game()
		elif choice in quit:
			print("See you soon.")