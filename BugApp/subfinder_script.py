import os

print("\n")
print("----------------------------------------SubFinder----------------------------------------")

txtfilechoice = '0'

domain = input("Input Domain = ")
txtfilechoice = input("Would you like to input to text file? Y or N =  ")	

if txtfilechoice == "Y":

	txtname = input("Input TXT Name = ")

	os.system('touch ' + txtname)
	os.system('subfinder -d ' + domain + '| httpx-toolkit -o "'+txtname+'" -title')
else:
	os.system('subfinder -d ' + domain + '| httpx-toolkit -title')
