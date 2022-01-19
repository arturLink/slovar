from moduleFAIL import *
rusW=[]
engW=[]
rusW=failist_lugemine("Russian.txt",rusW)
engW=failist_lugemine("English.txt",engW)
while 1:
	print("This is both Russian-English dictionary and English-Russian dictionary")
	print("You may enter numbers to navigate in the menu")
	print("1 - for using Russian-English dictionary")
	print("2 - for using English-Russian dictionary")
	print("3 - to add your own word with your own translation")
	print("4 - to exit the dictionary")
	choice=int(input("Enter number: "))
	if choice == 1:
		print(rusW)
		word=str(input("Enter wanted word: "))
		
	elif choice == 2:
		print(engW)
		word=str(input("Enter wanted word: "))
	elif choice == 3:
		print("Do you wish to enter word in 'rus' or 'eng' ")
		c=str(input())
		if c=="rus":
			word=str(input("Enter word: "))
			uus_sona(word,rusW)# razobratsja
			trans=str(input("Enter translation: "))
			uus_sona(trans,engW)
		elif c=="eng":
			word=str(input("Enter word: "))
			uus_sona(word,engW)
			trans=str(input("Enter translation: "))
			uus_sona(trans,rusW)
	elif choice == 4:
		print("")