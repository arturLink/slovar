from moduleFAIL import *
rusW=[]
engW=[]
rusW=failist_lugemine("Russian.txt",rusW)
engW=failist_lugemine("English.txt",engW)
while 1:
	print("This is both Russian-English dictionary and English-Russian dictionary")
	print("You may enter numbers to navigate in the menu")
	print("1 - to translate a word from Russian to English or otherwise")
	print("2 - to see all the available words")
	print("3 - to add your own word with your own translation")
	print("4 - to test your knowledge")
	print("5 - to exit the dictionary")
	choice=int(input("Enter number: "))
	if choice == 1:
		tolkimine(rusW,engW)
	elif choice == 2:
		print("Russian words - ",rusW)
		print("English words - ",engW)
	elif choice == 3:
		print("Do you wish to enter word in 'rus' or 'eng' ")
		c=str(input())
		if c=="rus":
			word=str(input("Enter word: "))
			uus_sona(word,rusW)
			trans=(input("Enter translation: "))
			uus_sona(trans,engW)
		elif c=="eng":
			word=str(input("Enter word: "))
			uus_sona(word,engW)
			trans=str(input("Enter translation: "))
			uus_sona(trans,rusW)
	elif choice == 4:
		print("Do you wish to translate from English to Russian or the other way around?")
		print("1 to translate from English, 2 to translate from Russian")
		choice=int(input())
		while choice == 1:
			word=random.choice(engW)
			print(word)
			answer=input("Translation in Russian: ")
			a=cntr_trnsl(answer,rusW)
			print(a)
			a=str(input("Do you wish to continue? 'yes' or 'no': "))
			if a == "yes":
				print("New word then")
			elif a == "no":
				break
		while choice == 2:
			word=random.choice(rusW)
			print(word)
			answer=input("Translation in English: ")
			a=cntr_trnsl(answer,engW)
			print(a)
			a=str(input("Do you wish to continue? 'yes' or 'no': "))
			if a == "yes":
				print("New word then")
			elif a == "no":
				break
	elif choice == 5:
		exit(0)