import socket
from colorama import init, Fore
from main.style import *

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def portSc():
	banner()
	def is_port_open(host, port):
		s = socket.socket()
		try:
			s.connect((host, port))
		except:
			return False
		else:
			return True
		host = input(f"  {GREEN}Enter the host:{RESET}")
		for port in range(1, 1025):
			if is_port_open(host, port):
				print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
		else:
			print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")