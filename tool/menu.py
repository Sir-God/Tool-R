from os import system
from main.style import *
from tool.tts import *

RC, GC, YC, CC, DF = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

def menu1():
	banner()
	print(f"                   {YC}Main Menu{DF}\n")
	print(f"  {GC}[{YC}1{GC}] {RC}Text To Speech\n")
	print(f"                 {GC}[{YC}+{GC}] {RC}Credit")
	print(f"                  {GC}[{YC}0{GC}] {RC}Exit")
	
	option = input(f" {YC}>>> {DF}")
	if option == "1":
		textspeech()
	elif option == "0":
		system("clear")
		exit()
