import os

while (True):

	print("Subfinder [1]")
	print("Amass [2]")
	print("Nmap [3]")
	print("BurpSuite [4]")

	choice = input(" = ")

	if choice == '1':
		print("\n")
		os.system('python3 subfinder_script.py')

	elif choice =='2':
		print("\n")
		os.system('python3 amass_script.py')
	break
