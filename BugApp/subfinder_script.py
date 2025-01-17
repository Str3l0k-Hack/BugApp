import os

print("\n")
print("----------------------------------------SubFinder----------------------------------------")

txtfilechoice = '0'
domain = input("Input Domain = ")
txtfilechoice = input("Would you like to input to text file? Y or N =  ")	
custcoms = input('Any Custom Commands? (Leave blank for default) = ')

if txtfilechoice == "Y" or txtfilechoice == "y":

	txtname = input("Input TXT Name = ")

	os.system('touch ' + txtname)
	os.system('subfinder -d ' + domain + custcoms + '| httpx-toolkit -o "'+txtname+'" -title')
else:
	os.system('subfinder -d ' + domain + custcoms + '| httpx-toolkit -title')
