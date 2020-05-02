from os import system
from main.style import *
from tool.tts import *
from tool.ports import *

RC, GC, YC, CC, DF = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

def menu1():
	system('clear')
	print(f'''
            
            {RC}╭━━━━╮{GC}╱╱╱╱{RC}╭╮{GC}╱╱╱╱╱{RC}╭━━━╮
            {RC}┃╭╮╭╮┃{GC}╱╱╱╱{RC}┃┃{GC}╱╱╱╱╱{RC}┃╭━╮┃
            ╰╯┃┃┣┻━┳━━┫┃{GC}╱╱╱╱╱{RC}┃╰━╯┃
            {GC}╱╱{RC}┃┃┃╭╮┃╭╮┃┃{GC}╱{RC}╭━━╮┃╭╮╭╯
            {GC}╱╱{RC}┃┃┃╰╯┃╰╯┃╰╮╰━━╯┃┃┃╰╮
            {GC}╱╱{RC}╰╯╰━━┻━━┻━╯{GC}╱╱╱╱{RC}╰╯╰━╯{DF}''')
	vers()
	print(f"                   {YC}Main Menu{DF}\n")
	print(f"  {GC}[{YC}1{GC}] {RC}Text To Speech         {GC}[{YC}2{GC}] {RC}Port Scanner{DF}\n")
	print(f"                 {GC}[{YC}+{GC}] {RC}Credit")
	print(f"                  {GC}[{YC}0{GC}] {RC}Exit")
	
	option = input(f" {YC}>>> {DF}")
	if option == "1":
		textspeech()
	elif option == "2":
		portSc()
	elif option == "0":
		system("clear")
	else:
		print(f"           {YC}Please Enter Right Input {DF}")
		sleep(8)
		menu1()
		exit()
