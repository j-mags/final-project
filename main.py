#agh. figure out uhhhhh... like using objects 
#put items in each room
def gameplay():
	rooms = {"Library", "Hallway", "Classroom", "Greenhouse"}
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
		print('''She frowns. "Just formalities, I guess."\n"The head librarian has a problem, and she said I needed to find you." (-1 Friendship Points)\n''')
		friendship -= 1
		enter = input("Friendship Level: [-1]\n\tPress enter to continue.")
	print('''\n\n[Haruna]: "Apparently, one of the books from the forbidden section of the library has gone missing.\nNot sure why we have a 'forbidden' section here to begin with..."''')
	if friendship < 0:
		print('''\nShe sighs. "I guess we'll have to find it together."''')
	else:
		print('''[Haruna]: "Looks like we'll be partners in crime today!"\n''')
		friendship += 1
		enter = input("Friendship Level: [1]")
	examine()
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
def choice():
	actions = ("quit", "save", "load", "get", "use")
	reponse = ""
	response = ("What would you like to do?\n")
	while response not in actions:
		print(f"Choices:\n{actions}\n")
		response = input(response).lower()
	return response

room_descriptions = ["The library is expansive, with the smell of cinnamon and the fluttering of pages in the air.", 
"It's bustling in the hallway. You can't help but bump into passerbys.", 
"The decor in the potion-brewing classroom is eclectic.\nThere is a permanent glow of dust in the air from the amount of failed potions by students.",
"Navigating through lush greenery, you spot the plant you've been searching for."]

class Room():
	def __init__(self):
		self.room_items = {"colored pencil", "key", "soda", "code"}
	def get_item(self, player):
		if self.room_items:
			item_grab = input("What item would you like to put in your inventory?").lower()
			if pick in self.room_items:
				print(f"You pick up {item_grab}. That'll come in handy.")
				player.inventory.append(item_grab)
				self.room_items.remove(item_grab)
			else:
				print(f'''"I don't think that's in this room?" She wanders around.''')
		else:
			print('''"Pretty sure this place is empty."''')
#loop for movement
#add objects
#make inventory