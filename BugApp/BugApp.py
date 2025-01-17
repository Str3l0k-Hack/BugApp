import os
from colorama import Fore, Back, Style


while (True):
	os.system('clear')


	print("\n")
	print("	 ▄▄▄▄    █    ██   ▄████     ▄▄▄       ██▓███   ██▓███ ") 
	print("	▓█████▄  ██  ▓██▒ ██▒ ▀█▒   ▒████▄    ▓██░  ██▒▓██░  ██▒")
	print("	▒██▒ ▄██▓██  ▒██░▒██░▄▄▄░   ▒██  ▀█▄  ▓██░ ██▓▒▓██░ ██▓▒")
	print("	▒██░█▀  ▓▓█  ░██░░▓█  ██▓   ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒██▄█▓▒ ▒")
	print("	░▓█  ▀█▓▒▒█████▓ ░▒▓███▀▒    ▓█   ▓██▒▒██▒ ░  ░▒██▒ ░  ░")
	print("	░▒▓███▀▒░▒▓▒ ▒ ▒  ░▒   ▒     ▒▒   ▓▒█░▒▓▒░ ░  ░▒▓▒░ ░  ░")
	print("	▒░▒   ░ ░░▒░ ░ ░   ░   ░      ▒   ▒▒ ░░▒ ░     ░▒ ░")
	print("	 ░    ░  ░░░ ░ ░ ░ ░   ░      ░   ▒   ░░       ░")
	print("	 ░         ░           ░")

	print(Fore.GREEN + Style.BRIGHT +"\n    		  Bug Bounty Scouting Tool\n")
	print(Style.RESET_ALL)

	print("		        Subfinder [1]")
	print("		        Amass [2]")
	print("			Nmap [3]")
	print("			BurpSuite [4]")
	print("\n		Documentation for all tools [5]")
	choice = input(" 		= ")

	if choice == '1':
		print("\n")
		os.system('clear')
		os.system('python3 subfinder_script.py')

	elif choice =='2':
		print("\n")
		os.system('clear')
		os.system('python3 amass_script.py')

	elif choice =='3':
		print("\n")
		os.system('clear')
		os.system('python3 nmap_script.py')

	elif choice =='4':
		print("\n")
		os.system('clear')
		os.system('python3 burp_script.py')

	elif choice =='5':
		print("\n")
		os.system('clear')
		os.system('python3 doc_script.py')

	break
