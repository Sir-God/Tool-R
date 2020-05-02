import socket
from colorama import init, Fore
from main.style import *

RC, GC, YC, CC, DF = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def is_port_open(host, port):
	s = socket.socket()
	try:
		s.connect((host, port))
		s.settimeout(0.2)
	except:
		return False
	else:
		return True
	
def portSc():
	system('clear')
	print(f'''
            
            {RC}╭━━━━╮{GC}╱╱╱╱{RC}╭╮{GC}╱╱╱╱╱{RC}╭━━━╮
            {RC}┃╭╮╭╮┃{GC}╱╱╱╱{RC}┃┃{GC}╱╱╱╱╱{RC}┃╭━╮┃
            ╰╯┃┃┣┻━┳━━┫┃{GC}╱╱╱╱╱{RC}┃╰━╯┃
            {GC}╱╱{RC}┃┃┃╭╮┃╭╮┃┃{GC}╱{RC}╭━━╮┃╭╮╭╯
            {GC}╱╱{RC}┃┃┃╰╯┃╰╯┃╰╮╰━━╯┃┃┃╰╮
            {GC}╱╱{RC}╰╯╰━━┻━━┻━╯{GC}╱╱╱╱{RC}╰╯╰━╯{DF}''')
	vers()
	print(f"                {GREEN}PORT SCANNER{RESET}\n\n")
	host = input(f"  {GREEN}Enter the host:{RESET} ")
	print(f"\n          {GRAY}now select Range For Ports{RESET}\n")
	port1 = input(' input Starting Port : ')
	port2 = input(' input end port : ')
	port1 = int(port1)
	port2 = int(port2)
	for port in range(port1, port2):
		if is_port_open(host, port):
			print(f"  {GREEN}[+] {host}:{port} is open      {RESET}")
		else:
			print(f"  {GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")