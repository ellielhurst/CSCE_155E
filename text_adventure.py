#created by Ellie :)

import colorama	#import feature to add colored text
from colorama import Fore #import command to actually use colored text
colorama.init(autoreset=True) #color reverts to normal after every use of the command

pocket = set()	#start with empty pockets
#using set instead of list so player can't add multiple of 1 thing to the array

#if input('pocket'):
#	print(pocket)

def class_room_function(): #function describing classroom

	while(True): #loop gpes on until player has two items in their pocket
		if (len(pocket) == 2): #this line activates once there is two items in you pocket.
			print(Fore.CYAN + '\nPerfect! Now all you need is a calculator, you decide to check out the teachers lounge.') #dialoge before moving to next part
			teachers_lounge_function() #calls teachers lounge funct to progress storyline
			break #once you have the two items you need the game progresses to the next room
		print('\nLooking around the classroom you see other \'desks\', a wall lined with \'cubbies\', and a \'closet\' in the back.')	#describing scene and options
		choice = input('Where do you search: ') #player inputs a choice from above
		if(choice == 'desks'): #entering options for stuff in desk
			print('\nYou rummage around some of the desks.') #describing scene
			print('In one desk, amongst a mess of old assignments, you find a \'wallet\', an \'empty can\', and a \'pencil\'\n')
			while(True): #this loop runs until player chooses 'go back' option
				if(len(pocket) == 2): #loop will break once you have the two things you can get from the classroom funciton
					break
				items= input('What do you take(type: \'go back\' to leave desk): ') #player input, different dialogue pops up per each item selected
				if(items == 'empty can'): 
					print(Fore.CYAN + '\nThat\'s someones trash, whats wrong with you, yuck.\n')
				elif(items == 'wallet'): 
					print(Fore.CYAN + '\nAre you kiding? Don\'t steal someones wallet.\n')
				elif(items == 'pencil'):
					pocket.add('pencil') #adding pencil to pocket
					print(Fore.CYAN + '\nNice! Exactly what you need to ace your test!')
					print(Fore.RED + '\n**pencil added to your pocket. \nCurrent items in your pocket' , pocket , '\n')	#showing whats currently in your pocket
				elif(items == 'go back'): #option to leave desk area
					break
				else:
					print(Fore.CYAN + '\nHuh? That\'s not something in the desk.\n') #message if player doesn't choose a valid item

		elif(choice == 'cubbies'): #entering option for cubbies
			print('\nYou rummage around some of the cubbies.') #describing scene
			print('In one cubby, you find an \'eraser\', a few \'highlighters\', and a nice pair of \'headphones\'\n')
			while(True):
				if(len(pocket) == 2): #loop will break once you have the two things you can get from the classroom funciton
					break
				items= input('What do you take(type: \'go back\' to leave cubbies): ') #player input options
				if(items == 'eraser'):
					pocket.add('eraser')  #add eraser to pocket 
					print(Fore.CYAN + '\nScore! Mistakes don\'t got nothing on you now!\n')
					print(Fore.RED + '**eraser added to your pocket. \nCurrent items in your pocket.' , pocket , '\n') #show player whast currently in list
				elif (items == 'highlighters'):
					print(Fore.CYAN + '\nDude, how is a highlighter supposed to help you on a math test? Keep looking.\n')
				elif(items == 'headphones'): 
					print(Fore.CYAN + '\nThose are not yours!! You can\'t take them! Do you wanna go to jail!? Geez.\n')
				elif(items == 'go back'): #option to leave cubby area
					break
				else:
					print(Fore.CYAN + '\nHuh? That\'s not something in the cubby.\n')	
	
		elif(choice == 'closet'):
			print('\nYou open the closet door and peer inside')
			print('You see a mop bucket and some other cleanign supplies')
			print('None of this is gonna help you on your test.')
			while(True):
				items= input('\nType: \'go back\' to leave closet): ')
				if(items == 'go back'): #option to leave closet area
					break
				else:
					print(Fore.CYAN + '\nThere\'s nothing useful here for you.\n')	
		else:
			print(Fore.CYAN + '\nWhat? You can search the \'desks\', \'cubbies\', or \'closet\'.') #if player enters invalid choice this prompts them with the valid choices again

def teachers_lounge_function():

	while(True):
		if(len(pocket) == 3): #activates once you have all three items in your pocket
				break #breaks this while loop so end game can prompt
		print('\nLooking around the teachers lounge you see a large \'cabinet\' and a \'fridge\'.\n') #describing scene
		choice = input('Where do you search: ')  #player can choose cabinet or fridge to search
		if (choice == 'cabinet'):
			print('\nYou open up the cabinet and to your luck you find a bin overflowing with spare calculators.')
			while(True):
				if(len(pocket) == 3): #activates once you have all three items in your pocket
					break #breaks this while loop so end game can prompt
				op = input('\n\'take one\' or \'go back\': ')
				if op == ('take one'):
					print(Fore.CYAN + '\nYou grab the calculator, promising to yourself to return it later.')
					pocket.add('calculator') #adding calculater to pocket list
					print(Fore.RED + '\n**calculator added to your pocket. \nCurrent items in your' , pocket , '\n') #letting player know calc has been added
				elif op == ('go back'):
					break
				else:
					print(Fore.CYAN + '\nHuh? You can either \'take one\' or \'go back\'.')
		elif(choice == 'fridge'):
			print('\nYou peek inside the fridge and see a tupperware filled with \'leftovers\' and a few  \'apples\'.')
			while(True):
				op = input('\n\'What do you take (type \'go back\' to leave fridge): ')
				if (op == 'leftovers'):
					print(Fore.CYAN + '\nWhy are you trying to take someones leftovers? Put that back!')
				elif(op == 'apples'):
					print(Fore.CYAN + '\nPlease don\'t steal some poor teachers apples, that\'s so rude.')
				elif(op == 'go back'):
					break
				else:
					print(Fore.CYAN + '\nThat\'s not an option, try again.')
		else:
			print(Fore.CYAN + '\nWhat? That\'s not something you can search.') #if player enters invalid choice this prompts them with the valid choices again

print(Fore.MAGENTA + '\n\n\n*~~~BEGIN ADVENTURE!!~~~*\n') #text adventure begins!!

#ascii art of pencil and math signs

print(Fore.GREEN + """

  ________________________________________________               +        +   +                     +
 /\______________________________________________/`-.            +         + +
<()>____________________________________________<    ##      +++++++++	    +	     ++++++++    +++++++	
 \/______________________________________________\,-'            +         + +
                                                                 +        +   +                     +

		            """)

#setting the scene
print('You are sitting in your high school english class, listening to your teacher wrap up today\'s lesson.')
print('As the bell rings you suddenly remember that you have a math exam next period.\n\nYou are woefully unprepared.\n')
print('To be able to take the exam you must find a pencil, an eraser, and a calculator before the exam begins.\n')
print()

#add option for neither choice

while(True):
	if(len(pocket) == 3):
		print('Awesome! You\'ve collected everything you need to ace that math test!') 
		print('Good luck!!')
		print(Fore.MAGENTA + '\n\n*~~~THANKS FOR PLAYING!!~~~*\n\n')	#end game!!!!!!!!!!!!!
		break
	choice = input('Type \'start\' to begin your adventure: ') #first input
	if(choice == 'start'):	#input to begin game
		class_room_function() #calling classroom function
	else:
		print(Fore.CYAN + '\nCan you follow instructions?\n') #if invalid choice
		