import main
quit = ('quit','q')
start = ('start','s')
choice = ''
while choice not in quit:
	print("\n\t\t\t---------------WELCOME---------------\n")
	print("\tAmidst bubbling potions and enchanting spells, a mystery occurs at your school;\n\tit's your duty to solve the puzzles and recover what has gone missing.")
	choice = input("\n\tWould you like to begin?\n\t> Start (s)\n\t> Quit (q)\n").lower()
	if choice in start:
		print("Good luck!\n---\n")
		main.gameplay()
	elif choice in quit:
		print("See you soon.")
	else:
		print("There's only two choices, buddy. Ahem. Let's restart.")