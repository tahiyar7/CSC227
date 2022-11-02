from multiprocessing.sharedctypes import RawValue
import os
import platform
import webbrowser
url = "https://marketing-matrix.weebly.com/"
url = "https://ignitedhorizon.weebly.com/"

global interest
interest = print("Here are soem ideas on Businesss projects!")

def studentmanagement():

	print("\n Hey Students! Welcome to Idea Generation Page!\n")
	print("What kinda project are you looking for?")
	print("1: Business Strategy")
	print("2: Or if you want to share any ideas with us please type 4 and proceed!")
	print("3: Seach anything here!\n")

	try:
		x = int(input(" Please type your response with 1, 2 and 3 Thanks! :  "))
	except ValueError:
		exit("\n Please type correctly!")
	else:
		print("\n")

	if(x==1):
		webbrowser.open(url)
	
	elif(x==2):
		global idealist
		idealist = []

		def ideas():
			print("\nIdea Generated!!! Added!\n")


		try:
			x = str(input("Type *share*!"))
		except ValueError:
			exit("\n This is not an Idea")
		else:
			print("\n")

		if(x=='share'):
			ideanew = input("Share your ideas with! ")
			if(ideanew in idealist):
				print("\nPlease get a new idea! {} You can find ideas in the marketing websites!".format(ideanew))
			else:
				idealist.append(ideanew)
				print("\n++ Idea Generated!! {} Thank You!! ++\n".format(ideanew))
				for students in idealist:
					print("++ {} ++".format(students))

		ideas()

		def continueAgain():
			runningagain = input("\nWant to continue the process yes/no?: ")
			if(runningagain.lower() == 'yes'):
				if(platform.system() == "Windows"):
					print(os.system('cls'))
				else:
					print(os.system('clear'))
				ideas()
				continueAgain()
			else:
				quit(print('Have a good one! Ideas Submitted!'))

		continueAgain()

	elif(x==3):
		new=2
		tabUrl=("http://google.com/search?q=")
		term= input('Enter your search: ')
		webbrowser.open(tabUrl+term,new=new)
		

	elif(x < 1 or x > 5):
		print("Please Enter Valid Choice")

studentmanagement()

def continueAgain():
	runningagain = input("\nWant to continue the process yes/no?: ")
	if(runningagain.lower() == 'yes'):
		if(platform.system() == "Windows"):
			print(os.system('cls'))
		else:
			print(os.system('clear'))
		studentmanagement()
		continueAgain()
	else:
		
		quit(print('Have a good one! Thanks for checking our websites!'))

continueAgain()
