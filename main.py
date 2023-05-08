#agh. figure out uhhhhh... like using objects 
#put items in each room
def gameplay():
	print("---WELCOME---\n")
	print("\tAmidst bubbling potions and enchanting spells, a mystery occurs at your school;\n\tit's your duty to solve the puzzles and recover what has gone missing.")
	run.py()
rooms = {"Library", "Hallway", "Classroom", "Greenhouse"}
location = ""
try:
	while location == rooms[0]:
		print(f{room_descriptions[0]})
		print("A girl runs up to you, startling you so hard that you almost drop your book.\n")
		qna = int(input('''"Hey, you're the student council president, right?"\n\t> Yeah, what's up? (1)\n\t> Why are you asking if you already know… (2)\n'''))
		friendship = 0
		try:
		qna = int(qna)
			if qna != 1 or qna != 2:
				print("Sorry, that wasn’t a valid option.\n")
		except:
			if qna == 1:
				print('''\t> "Perfect! The head librarian has a bit of a... problem we need to fix."''')
		else:
			if qna == 2:
				print('''She frowns. "Just formalities, I guess."\n "The head librarian has a problem, and she said I needed to find you." (-1 Friendship Points)\n''')
			friendship -= 1
		print("Friendship Meter: [{"*"*{friendship}}]")
		print('''"Apparently, one of the books from the forbidden section of the library has gone missing."\n"Not sure why we have a 'forbidden' section here to begin with."''')
		if friendship < 0:
			print('''She sighs. "I guess we'll have to find it together."''')
		else:
			print('''"Looks like we'll be partners in crime today!"\n''')
		print("Your colored pencil (weird that you only have one) is sitting on a desk.")
		game.input()





room_description = {"The library is expansive, with the smell of cinnamon and the fluttering of pages in the air.", 
"It's bustling in the hallway. You can't help but bump into passerbys.", 
"The decor in the potion-brewing classroom is eclectic.\nThere is a permanent glow of dust in the air from the amount of failed potions by students.",
"Navigating through lush greenery, you spot the plant you've been searching for."}

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
	actions = ("quit", "save", "load", "get", "use")

def input():
	response = ("What would you like to do?")
	response = None
	while response not in actions:
		print(f"Choices:\n{actions}")
		response = input(prompt).lower()
	return response
player = Player()
def main(player):
	choice = None
	while choice != "quit":
		if choice == "quit":
			print("Come back soon! We have a book to find.")
		elif choice == "save":
			save()
		elif choice == "load":
			load()
		elif choice == "get":
			room.get_item(player)
		elif choice == "use":
			room.use_item(player)