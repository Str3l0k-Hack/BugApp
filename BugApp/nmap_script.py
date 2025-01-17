import os

print('----------------------------------------Nmap----------------------------------------')

subdom = input('Input a Link = ')
custcoms = input('Any Custom Commands? (Leave blank for default) = ')
textfileques = input('Would you like to output result to a txt? y OR n = ')
if textfileques == 'y' or textfileques == 'Y':

	txtname = input('What would you like the txt name to be? = ')
	os.system('nmap -oN "' +txtname+'" '+custcoms+' '+subdom)
else:
	os.system('nmap '+custcoms+' '+subdom)

