import subprocess
from time import sleep
from os import system, getuid, path
import requests
from subprocess import check_output
from main.style import *

RC, GC, YC, CC, DF = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

def verCheck():
	system('clear')
	print(f'''
            
            {RC}╭━━━━╮{GC}╱╱╱╱{RC}╭╮{GC}╱╱╱╱╱{RC}╭━━━╮
            {RC}┃╭╮╭╮┃{GC}╱╱╱╱{RC}┃┃{GC}╱╱╱╱╱{RC}┃╭━╮┃
            ╰╯┃┃┣┻━┳━━┫┃{GC}╱╱╱╱╱{RC}┃╰━╯┃
            {GC}╱╱{RC}┃┃┃╭╮┃╭╮┃┃{GC}╱{RC}╭━━╮┃╭╮╭╯
            {GC}╱╱{RC}┃┃┃╰╯┃╰╯┃╰╮╰━━╯┃┃┃╰╮
            {GC}╱╱{RC}╰╯╰━━┻━━┻━╯{GC}╱╱╱╱{RC}╰╯╰━╯{DF}''')
	vers()
	print(f"  {YC}Check For Update.........!{DF}")
	ver_url = "https://raw.githubusercontent.com/Sir-God/Tool-R/master/version.txt"
	ver_rqst = requests.get(ver_url)
	ver_sc = ver_rqst.status_code
	if ver_sc == 200:
		with open('version.txt') as t:
			ver_current = t.read()
			ver_current = ver_current.strip()
			github_ver = ver_rqst.text
			github_ver = github_ver.strip()
		if ver_current == github_ver:
			print(f"  {GC}[Up To Date] {CC} v. {YC}{github_ver}{DF}")
			sleep(5)
		else:
			print(f"  {YC}[+] There is a new Version Available..!{DF}\n")
			print(f"  {RC} Current V - {YC}{ver_current}{DF}")
			print(f"  {GC} New Available V - {YC}{github_ver}{DF}")
			print(f"  {YC} Updating To The Lattest Version Please Wait....! {DF}")
			system("git clean -d -f > /dev/null && git pull -f > /dev/null")
			with open('version.txt') as t:
				ver_current = t.read()
				ver_current = ver_current.strip()
			print(f"  {GC}Version Status After Update{DF}\n")
			print(f"  {YC}Current Version v - {GC}{ver_current}{DF}")
			print(f"  {GC} Available Version v - {GC}{github_ver}{DF}")
			sleep(5)
			system('clear')
	else:
		print(f"  {RC}Failed To Get Update")
