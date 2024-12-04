import os

while (True):

	print("\nWelcome to 'BugApp', An App for automating Recon\n")
	print("Subfinder [1]")
	print("Amass [2]")
	print("Nmap [3]")
	print("BurpSuite [4]")
	print("\nDocumentation for all tools [5]")
	choice = input(" = ")

	if choice == '1':
		print("\n")
		os.system('python3 subfinder_script.py')

	elif choice =='2':
		print("\n")
		os.system('python3 amass_script.py')

	elif choice =='3':
		print("\n")
		os.system('python3 nmap_script.py')

	elif choice =='4':
		print("\n")
		os.system('python3 burp_script.py')

	elif choice =='5':
		print("\n")
		os.system('python3 doc_script.py')

	break
