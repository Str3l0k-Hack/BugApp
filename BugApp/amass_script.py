import os

print('----------------------------------------Amass----------------------------------------')

subdom = input('Input a Subdomain = ')
custcoms = input('Any Custom Commands? (Leave blank for default) = ')
textfileques = input('Would you like to output result to a txt? y OR n = ')

if textfileques == 'y' or textfileques == 'Y':

	txtname = input('What would you like the txt name to be? = ')
	os.system('amass enum -d '+subdom+''+custcoms+' -o ' +txtname)
else:
	os.system('amass enum -d '+subdom+' '+custcoms)
