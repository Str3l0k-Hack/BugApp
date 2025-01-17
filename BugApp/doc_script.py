import os
import webbrowser

print('\n----------------------------------------Documentation----------------------------------------')

print("Which would you like to see the documentation for:")
print("Subfinder [1]")
print("Amass [2]")
print("Nmap [3]")
print("BurpSuite [4]")

choice = input(" = ")

print("\n")

urlsub = "https://docs.projectdiscovery.io/introduction"
urlamass = "https://github.com/owasp-amass/amass/wiki/User-Guide"
urlmap = "https://nmap.org/book/man.html"
urlburpe = "https://portswigger.net/burp/documentation/desktop"

if choice == '1':
	webbrowser.open(urlsub)
elif choice == '2':
	webbrowser.open(urlamass)
elif choice == '3':
	webbrowser.open(urlmap)
elif choice == '4':
	webbrowser.open(urlburpe)
