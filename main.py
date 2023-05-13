def gameplay():
	rooms = {"library", "hallway", "greenhouse"}
	location = ""
	location == "library"
	end = False
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
		qna = int(input("\n\t> I only have one color, Einstein. It's gonna turn out bad. (1)\n\t> YAYYYYY! (2)\n"))
		if qna == 1:
			print('''[Haruna]: "You're such a downer. *sigh* Just try and use the colored pencil."\n''')
			friendship -= 1
			friendship = int(friendship)
			enter = input(f"Friendship Level: [{friendship}]\n\tPress enter to continue.")
			choice()
		elif qna == 2:
			print('''[Haruna]: "YAYYYYY!"''')
			print('''[Haruna]: "Let's use the colored pencil!"\n''')
			friendship += 1
			friendship = int(friendship)
			enter = input(f"Friendship Level: [{friendship}]\n\tPress enter to continue.")
			choice()
		print("You do the color-by-number completely in green.")
		new_item = "picture"
		inventory.append(new_item)
		enter = input("\n\tNew item [picture] has been added to inventory.\n")
		print('''[Haruna]: "Alright. Seems like we're done in here."\n''')
		print("You and Haruna walk into the hallway.\n------\n")
		SorL = input("Would you like to save (s) or load (l) a game?\nOr, would you like to continue (c)?\n").lower
		if SorL == "s":
			save()
		elif SorL == "l":
			load()
		else:
			location = "hallway"
			print(f"------\n\n{room_descriptions[1]}\n")
			option = int(input("Would you like to politely ask people to move (1) or brute force your way through (2)?\n"))
			if option == 2:
				print(f"\nMasul Academy of Sorcery has not seen someone as determined as you, {name}.\nHats off to you.")
				print("\n\tYou bump into a student with shifting eyes and fidgeting fingers.")
				print('''[Haruna]: "Hey, watch it-!"\n''')
				print("It seems they dropped something.")
				inventory.append("key")
				examine()
			elif option == 1:
				print("\t> E-excuse me! Can I get through...?\n")
				print("Students in the hall give you the stink eye.")
				print('''[Haruna]: "Yikes. Not a power move."\n''')
				print("\tDespite that, she laughs.\n")
				friendship += 1
				friendship = int(friendship)
				enter = input(f"Friendship Level: [{friendship}]\n\tPress enter to continue.\n")
				print('''[Haruna]: "Still, we need a way to get through this."\n''')
				qna = input("Alright, do you have it in you to push through the crowd? (y) (n)\n")
				if qna == "y":
					print("There's the fighting spirit!")
					print(f"Masul Academy of Sorcery has not seen someone as determined as you, {name}.\nHats off to you.")
					print("\n\tYou bump into a student with shifting eyes and fidgeting fingers.")
					print('''[Haruna]: "Hey, watch it-!"\n''')
					print("It seems they dropped something.")
					inventory.append("key")
					examine()
				elif qna == "n":
					print("\nI... why not? You could use magic to blow them away for all we care.")
					print('''Haruna sighs.\n\n[Haruna]: "Look, I'll just push thr-"\n\tA student with shifting eyes and fidgeting fingers bumps into you.\n\tSeems they dropped something.''')
					inventory.append("key")
					examine()
			if "key" in inventory:
				enter = input("\n\tNew item [key] has been added to inventory.\n")
				print('''[Haruna]: "Alright. Seems like we're done in here."\n''')
				enter = input("But you're a little stumped on where to go next.\n")
				print(f'''[Haruna]: "{name}! Check this out! The key has something engraved in it."\n''')
				enter= input("\nThe key says:\n\t'GR  NH  S'\nYou're puzzled.\n")
				print('''[Haruna]: "Okay... Grnhs.. that means nothing to me."\nShe pauses.\n[Haruna]: "Maybe- maybe this has something to do with the drawing! The plant!"''')
				puzzle = input('''[Haruna]: "What do you think the key is for?"\n''')
				if puzzle in ("greenhouse","green","Greenhouse","Green"):
					print('''She claps.\n[Haruna]: "You're a genius! To the greenhouse we go!"\n''')
				else:
					print('''[Haruna]: "Gruuunn...hoos... that's not right..."\n[Haruna]: "Grenhas..? That feels closer.."\n''')
					puzzle = input('''[Haruna]: "What do you think the key is for?"\n''').lower
					if puzzle in ("greenhouse","green","Greenhouse","Green"):
						print('''She claps.\n[Haruna]: "You're a genius! To the greenhouse we go!"\n''')
					else:
						print('''[Haruna]: "Okay, honestly, I figured it out. It's greenhouse."\n''')
						print("It's okay to be a bit embarrassed.\nLet's continue.\n")
				print("You and Haruna head to the greenhouse.\n------\n")
				SorL = input("Would you like to save (s) or load (l) a game?\nOr, would you like to continue (c)?\n").lower
				if SorL == "s":
					save()
				elif SorL == "l":
					load()
				else:
					print("------\nThe greenhouse looms ahead of you.\n")
					enter = input('''[Haruna]: "This feels like the final boss..."\nHaruna is great at foreshadowing."\n''')
					print("\t> I'm gonna use the key...")
					choice()
					qna = int(input("Will you go in first (1) or let Haruna tough it out and make her go first (2)?\n"))
					if qna == 1:
						print("\t> Okay, follow me.\n")
						print(f'''Her eyes light up.\n[Haruna]: "You know what, {name}, you're pretty cool!"\nA single tear rolls down her face (not really).\n''')
						friendship += 3
						friendship = int(friendship)
						enter = input(f"Friendship Level: [{friendship}]\n\tPress enter to continue.\n")
					elif qna == 2:
						print("\t> Sucks to suck.\nYou make her walk in first.")
						enter = input("I feel like you really tanked any chance of friendship here.\n")
						friendship -= 3
						friendship = int(friendship)
						enter = input(f"Friendship Level: [{friendship}]\n\tPress enter to continue.\n")
					location = "greenhouse"
					print(f"------\nYou enter.\n\n{room_descriptions[2]}\n")
					print('''[Haruna]: *gasp* "There's the astricase wiper!"\n''')
					enter = input("\t> Asteraceae viper.\n")
					print('''[Haruna]: "We are on the cusp of solving a mystery and maybe fighting a magical carnivorous plant. \nAre specifics important?"''')
					print("She makes a good point.\n")
					enter = input('''[Haruna]: "Not gonna lie right now. I am way too scared. Here- take my wand."\n''')
					print("\t------ MINI GAME ------\nDefeat the evil plant!\nWhat spell will you use?\n")
					option = int(input("\tSodaeous Cascata - this just sprays Coca-Cola. (1)\n\tLvl. 100 Full Force Impacteous - makes your opponent feel like they've been lightly slapped (2)\n\tTuno Autus - makes all your words sound autotuned (3)\n"))
					if option == 1:
						print("You use [Sodaeous Cascata]! It's highly effective! The plant opens its mouth to drink the soda!\n\t----------------------\n\nGood news- this makes the asteraceae viper throw up what it was hiding!\n")
						enter = input('''[Haruna]: "Wow! Yuck!" She says with a smile on her face.\nHaruna picks up what the plant regurgitated.\n''')
						enter = input(f'''[Haruna]: "No way...! {name}!!!"\nShe holds up... the missing book!''')
						if friendship > 3:
							print("\nYou two high five.\n")
						else:
							enter = input("\nShe almost holds up her hand to high five you, but she drops her arm.\n")
						print('''Dont forget, there's bad news-\n[Haruna]: "Oh..."\n[Haruna]: "It... the plant isn't dead right?"''')
						print("You look at the plant. It is definitely dead.")
						end = True
					elif option == 2:
						print("You use [Lvl. 100 Full Force Impacteous]!\nThe plant stares angrily and only looks more offended when you cast the spell and it is slightly hit.\n")
						print('''[Haruna]: "Ohhh... wow, that was lame. Maybe try the cola spell."''')
						option = int(input("\tSodaeous Cascata - this just sprays Coca-Cola. (1)\n\tLvl. 100 Full Force Impacteous - makes your opponent feel like they've been lightly slapped (2)\n\tTuno Autus - makes all your words sound autotuned (3)\n"))
						if option == 1:
							print("You use [Sodaeous Cascata]! It's highly effective! The plant opens its mouth to drink the soda!\n\t----------------------\n\nGood news- this makes the asteraceae viper throw up what it was hiding!\n")
							enter = input('''[Haruna]: "Wow! Yuck!" She says with a smile on her face.\nHaruna picks up what the plant regurgitated.\n''')
							print(f'''[Haruna]: "No way...! {name}!!!"\nShe holds up... the missing book!''')
							if friendship > 3:
								print("\nYou two high five.\n")
							else:
								print("\nShe almost holds up her hand to high five you, but she drops her arm.\n")
							print('''Dont forget, there's bad news-\n[Haruna]: "Oh..."\n[Haruna]: "It... the plant isn't dead right?"''')
							print("You look at the plant. It is definitely dead.")
							end = True
					elif option == 3:
						print("You use [Tuno Autus]!\n\t> Take this, beast!\nYou announce with an unnatural vibrato. The plant looks unimpressed, somehow.\n")
						print('''[Haruna]: "You've got some pipes! But it seems like that only disappointed the plant. Maybe try the cola spell."\n''')
						option = int(input("\tSodaeous Cascata - this just sprays Coca-Cola. (1)\n\tLvl. 100 Full Force Impacteous - makes your opponent feel like they've been lightly slapped (2)\n\tTuno Autus - makes all your words sound autotuned (3)\n"))
						if option == 1:
							print("You use [Sodaeous Cascata]! It's highly effective! The plant opens its mouth to drink the soda!\n\t----------------------\n\nGood news- this makes the asteraceae viper throw up what it was hiding!\n")
							enter = input('''[Haruna]: "Wow! Yuck!" She says with a smile on her face.\nHaruna picks up what the plant regurgitated.\n''')
							print(f'''[Haruna]: "No way...! {name}!!!"\nShe holds up... the missing book!''')
							if friendship > 3:
								print("\nYou two high five.\n")
							else:
								print("\nShe almost holds up her hand to high five you, but she drops her arm.\n")
							print('''Dont forget, there's bad news-\n[Haruna]: "Oh..."\n[Haruna]: "It... the plant isn't dead right?"''')
							print("You look at the plant. It is definitely dead.")
							end = True
	if end == True:
		print("\n------\n")
		enter = input("You and Haruna return the book to the head librarian, recalling all the fascinating details.")
		print("\n\t> And then we killed the asteraceae viper-\n")
		print('''The librarian stops dead in her tracks.\n[Head Librarian]: "You... what?"\n''')
		enter = input("Now, you and Haruna exchange glances.\n")
		enter = input('''[Head Librarian]: "How could you-" She sputters.\n[Head Librarian]: "You killed the- I just- Detention for the both of you!"\n''')
		if friendship > 5:
			enter = input(f"\tFriendship Level: [{friendship}]")
			print(f'''She bursts into laughter.\n[Haruna]: "Well, if I'm in detention, I'd want it to be with you, {name}."''')
			enter = input("\n------\n")
			print("Congrats! You found the missing book AND you made a new friend today!\n")
			print("Sucks that you got detention, but you also got to go into combat with a magical plant,\nso- it was a successful day nonetheless.")
			print("\n\t\t\t---------------END---------------\n")
			exit()
		else:
			enter = input(f"Friendship Level: [{friendship}]\n")
			print(f'''She smiles.\n[Haruna]: "Destorying school property then getting detention together,"\n[Haruna]: "I guess we have a chance of being close someday."''')
			enter = input("\n------\n")
			print("Congrats! You found the missing book! And although your first impression with Haruna wasn't great,\nmaybe you can try to be nicer later on.\n")
			print("Sucks that you got detention, but you also got to go into combat with a magical plant,\nso- it was a successful day nonetheless.")
			print("\n\t\t\t---------------END---------------\n")
			exit()


	elif "colored pencil" not in inventory:
		print('''[Haruna]: "That colored pencil looks miiiighty interesting..."''')
		choice()

def examine():
	look = input("\nWould you like to examine the room?\n\t> Yes\n\t> No\n")
	while "colored pencil" not in inventory:
		if look in ("Y","Yes","y","yes"):
			print("Your colored pencil (weird that you only have one) is sitting on a desk.")
			choice()
		else:
			yikes = input("Okay... um.")
			yikes = input("Nice weather we're having here.")
			yikes = input("Alright let's get back to the game.")
			examine()
	if "colored pencil" in inventory and "key" in inventory:
		if look in ("Y","Yes","y","yes"):
			print("The comically suspicious student dropped a key in your brief encounter.")
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
	print(f"Inventory: {inventory}")
	use_item = input("What item would you like to use?\n")
	if use_item in inventory:
		while use_item == "colored pencil":
			enter = input(f'''\n[Haruna]: "Oh! It worked!"''')
			enter = input(f'''[Haruna]: "That's a sick drawing of a..."\nShe stares.\n[Haruna]:"What exactly is that..."''')
			print(f"\n\t> Pretty sure it's a Asteraceae Viper.\nShe stares blankly again.\n")
			qna = int(input("\t> I pay attention in Botany! Maybe you should too. (1)\n\t> Scary plant go chomp chomp. (2)\n"))
			if qna == 1:
				print(f'''[Haruna]: "I *do* pay attention. It's that one carnivorous plant... I was just testing you..."\nHaruna looks sulky.''')
				enter = input(f"Press enter to continue.\n")
			else:
				print('''Haruna laughs.\n[Haruna]: "Using scientific terms, I see."\n[Haruna]: "Hey, maybe this could be a clue!"''')
				print("\nYou wonder why the librarian would even give you a clue if\nshe's the one who's looking for the missing book.")
				enter = input(f"\nPress enter to continue.\n")
			text = "You do the color-by-number completely in green."
			return text
		while use_item == "key":
			print("\nThe lock clicks.\n")
			text = '''[Haruna]: "This is stupid but I'm kind of scared."'''
			return text
	else:
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
		else:
			print("That's not an item that can be added to your inventory!")
	elif response == "u":
		use()
	elif response == "i":
		print(f"Inventory: {inventory}")
	while response not in actions:
		print(f"Choices:\n{actions}\n")
		choice()

room_descriptions = ["The library is expansive, with the smell of cinnamon and the fluttering of pages in the air.", 
"It's bustling in the hallway. You can't help but bump into passerbys.",
"Navigating through lush greenery, you spot the plant you've been searching for."]
inventory = []
room_items = {"colored pencil", "key", "soda", "code"}