try:
	import os
	import requests
	from os import system
	system("title " + "Soud Was Here - @8Y - Soud#5866")
	import colorama
	from colorama import Fore
	colorama.init(autoreset=True)

except Exception as m:
    print("Something Went Wrong\n")
    print(m)
    input()
    exit()
logo = f"""
{Fore.CYAN}         _______   __ 
{Fore.CYAN}   ____ |  _  \ \ / /
{Fore.CYAN}  / __ \ \ V / \ V /
{Fore.CYAN} / / _` |/ _ \  \ /
{Fore.CYAN}| | (_| | |_| | | |
{Fore.CYAN} \ \__,_\_____/ \_/
{Fore.CYAN}  \____/
"""
print(logo)
print(f"{Fore.RED}This Is Free Tool By Soud Alanzi And Not For Sale\n\n{Fore.RESET}{Fore.GREEN}Instagram: @8Y + @_agf\nDiscord: Soud#5866\n")
target = input("Enter Target User/Email : ")
mode = int(input("1) Database - 2) Common\n>> "))
if mode == 1:
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/hotmail.txt"
    req = requests.get(url)
    save = open("Database-Passworder.txt", "a")
    for i in req.text.splitlines():
        print(f"{target}:{i}")
        save.write(f"{target}:{i}\n")

elif mode == 2:
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt"
    req = requests.get(url)
    save = open("Common-Passworder.txt", "a")
    for i in req.text.splitlines():
        print(f"{target}:{i}")
        save.write(f"{target}:{i}\n")

else:
    print("Wrong Mode !")
    input()
    exit()
input("Press Enter To Exit...")
