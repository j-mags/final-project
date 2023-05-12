#agh. figure out uhhhhh... like using objects 
#put items in each room
import Rooms
def gameplay():
	rooms = {"library", "hallway", "greenhouse"}
	location = ""
	location == "library"
	print(f"{room_descriptions[0]}")
	print("A girl runs up to you, startling you so hard that you almost drop your book.\n")
	print('''[?]: "Hey, you!"''')
	name = input('''[?]: "Um... you, uh.."\n[?]: "I'm sorry- what was your name again?"\n''')
	print(f"\t> It's {name}.\n")
	print(f'''[?]: "Right! Nice to meet you, {name}! I'm Haruna."\n[Haruna]: "Names aside, you're the student council president, right?"''')
	qna = int(input('''\n\t> Yeah, what's up? (1)\n\t> Why are you asking if you already know… (2)\n'''))
	friendship = 0
	if qna == 1:
		print('''\t[Haruna]: "Perfect! The head librarian has a bit of a... problem we need to fix."''')
	elif qna == 2:
		print('''She frowns. "Just formalities, I guess."\n[Haruna]: "The head librarian has a problem, and she said I needed to find you." (-1 Friendship Points)\n''')
		friendship -= 1
		enter = input("Friendship Level: [-1]\n\tPress enter to continue.")
	print('''\n\n[Haruna]: "Apparently, one of the books from the forbidden section of the library has gone missing.\nNot sure why we have a 'forbidden' section here to begin with..."''')
	if friendship < 0:
		print('''\nShe sighs. "I guess we'll have to find it together."''')
	else:
		print('''[Haruna]: "Looks like we'll be partners in crime today!"\n''')
		friendship += 1
		enter = input("Friendship Level: [1]\n\tPress enter to continue.")
	examine()
	if "colored pencil" in inventory:
		print('''[Haruna]: "Hey, I actually have this color-by-number from the librarian!"\n''')
		qna = input("\n\t> I only have one color, Einstein. It's gonna turn out bad. (1)\n\t> YAYYYYY! (2)\n")
		if qna == 1:
			print('''[Haruna]: "You're such a downer. *sigh* Just try it."\n''')
			friendship -= 1
			friendship = int(friendship)
			enter = input(f"Friendship Level: [{friendship}]\n\tPress enter to continue.")
		elif qna == 2:
			print('''[Haruna]: "YAYYYYY!"\n''')
			friendship += 1
			friendship = int(friendship)
			enter = input(f"Friendship Level: [{friendship}]\n\tPress enter to continue.")
		print("You do the color-by-number completely in green.")
		new_item = "picture"
		inventory.append(new_item)
		enter = input("\n\tNew item [picture] has been added to inventory.")
		print('''[Haruna]: "Alright. Seems like we're done in here."\n''')
		print("You and Haruna walk into the hallway.\n")
		SorL = input("Would you like to save (s) or load (l) a game?\n").lower
		if SorL == "s":
			save()
		elif SorL == "l":
			load()
		location = "hallway"
		print(f"{room_descriptions[0]}")

def examine():
	look = input("\nWould you like to examine the room?\n\t> Yes\n\t> No\n")
	if look in ("Y","Yes","y","yes"):
		print("Your colored pencil (weird that you only have one) is sitting on a desk.")
		choice()
	else:
		yikes = input("Okay... um.")
		yikes = input("Nice weather we're having here.")
		yikes = input("Alright let's get back to the game.")
		examine()
def save(self):
	with shelve.open("game.bin") as s:
		s.close()
def load(self):
	s = shelve.open("game.bin")
	game_load = s.get()
	return game_load
def quit():
	quit_or_stay = input("Are you sure you want to quit? (y) or (n)\n")
	if quit_or_stay == "n":
		print('''[Haruna]: "Oh, I'm so glad you didn't decide to quit! Let's keep going."''')
		choice()
	else:
		print('''[Haruna]: "Alright... I guess I'll do this on my own."\n''')
		print("---------------------------------------")
		exit()
def use():
	use_item = input("What item would you like to use?\n")
	print(f"Inventory: {inventory}")
	if use_item in inventory:
		while use_item == "colored pencil":
			if location == "library":
				usable = True
				enter = input(f'''[Haruna]: "Oh! It worked!"''')
				enter = input(f'''[Haruna]: "That's a sick drawing of a..."\nShe stares.\n"{name}, what exactly is that..."''')
				print(f"\n\t> Pretty sure it's a Asteraceae Viper.\nShe stares blankly again.")
				qna = input("\t> I pay attention in Botany! Maybe you should too. (1)\n\t> Scary plant go chomp chomp. (2)")
				if qna == 1:
					print(f'''[Haruna]: "I *do* pay attention. It's that one carnivorous plant... I was just testing you..."\nHaruna looks sulky.''')
					friendship -= 1
					friendship = int(friendship)
					enter = input(f"Friendship Level: [{friendship}]\n\tPress enter to continue.")
				else:
					print('''Haruna laughs.\n[Haruna]: "Using scientific terms, I see."''')
					friendship += 1
					friendship = int(friendship)
					enter = input(f"Friendship Level: [{friendship}]\n\tPress enter to continue.")
			else:
				usable = False 
				print('''There's a smile on Haruna's face.\n[Haruna]: "What exactly are you trying to do...?"\n[Haruna]: "Let's try something different."''')

def choice():
	actions = ("q", "s", "l", "g", "u")
	reponse = ""
	print(f"\nChoices:\n\t> Quit (q)\n\t> Save (s)\n\t> Load (l)\n\t> Get (g)\n\t> Use (u)\n\t> Inventory (i)\n")
	response = input("What would you like to do?\n")
	if response == "q":
		quit()
	elif response == "s":
		save()
	elif response == "l":
		load()
	elif response == "g":
		grab = input("What item would you like to add to your inventory?\n")
		if grab in room_items:
			print(f"You pick up the {grab}. That'll come in handy.\n")
			inventory.append(grab)
			room_items.remove(grab)
	elif response == "u":
		use()
	elif response == "i":
		print(f"Inventory: {inventory}")
	while response not in actions:
		print(f"Choices:\n{actions}\n")
		choice()

room_descriptions = ["The library is expansive, with the smell of cinnamon and the fluttering of pages in the air.", 
"It's bustling in the hallway. You can't help but bump into passerbys.", 
"The decor in the potion-brewing classroom is eclectic.\nThere is a permanent glow of dust in the air from the amount of failed potions by students.",
"Navigating through lush greenery, you spot the plant you've been searching for."]
inventory = []
room_items = {"colored pencil", "key", "soda", "code"}
#loop for movement
#add objects
#make inventory