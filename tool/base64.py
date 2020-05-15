import base64
from main.style import *

RC, GC, YC, CC, DF = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[1;37m'


def enco():
	system('clear')
	print(f'''
            
            {RC}╭━━━━╮{GC}╱╱╱╱{RC}╭╮{GC}╱╱╱╱╱{RC}╭━━━╮
            {RC}┃╭╮╭╮┃{GC}╱╱╱╱{RC}┃┃{GC}╱╱╱╱╱{RC}┃╭━╮┃
            ╰╯┃┃┣┻━┳━━┫┃{GC}╱╱╱╱╱{RC}┃╰━╯┃
            {GC}╱╱{RC}┃┃┃╭╮┃╭╮┃┃{GC}╱{RC}╭━━╮┃╭╮╭╯
            {GC}╱╱{RC}┃┃┃╰╯┃╰╯┃╰╮╰━━╯┃┃┃╰╮
            {GC}╱╱{RC}╰╯╰━━┻━━┻━╯{GC}╱╱╱╱{RC}╰╯╰━╯{DF}''')
	vers()
	print(f"                {YC}Encode Base64{DF}")
	print(f"  {GC}Input Text Message Which You Need To Encode in Base64{DF}")
	message = input(f"  {YC}Input Text : {DF}")
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')

	print(f"  {YC}Encoded Text is {DF}: {RC}{base64_message}{DF}")
	exit()

def deco():
	system('clear')
	print(f'''
            
            {RC}╭━━━━╮{GC}╱╱╱╱{RC}╭╮{GC}╱╱╱╱╱{RC}╭━━━╮
            {RC}┃╭╮╭╮┃{GC}╱╱╱╱{RC}┃┃{GC}╱╱╱╱╱{RC}┃╭━╮┃
            ╰╯┃┃┣┻━┳━━┫┃{GC}╱╱╱╱╱{RC}┃╰━╯┃
            {GC}╱╱{RC}┃┃┃╭╮┃╭╮┃┃{GC}╱{RC}╭━━╮┃╭╮╭╯
            {GC}╱╱{RC}┃┃┃╰╯┃╰╯┃╰╮╰━━╯┃┃┃╰╮
            {GC}╱╱{RC}╰╯╰━━┻━━┻━╯{GC}╱╱╱╱{RC}╰╯╰━╯{DF}''')
	vers()
	print(f"                {YC}Decode Base64{DF}")
	print(f"  {GC}Input Encoded Base64 text for decode them")
	base64_message = input(f"  {YC}Input Encoded Text : {DF}")
	base64_bytes = base64_message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	message = message_bytes.decode('ascii')
	
	print(f"  {YC}Decoded Text is {DF}: {GC}{message}{DF}")
	exit()
