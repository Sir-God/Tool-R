import gtts
import os
import sys
from os import system
from time import sleep
from main.style import *

RC, GC, YC, CC, DF = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

def textspeech():
	system('clear')
	print(f'''
            
            {RC}╭━━━━╮{GC}╱╱╱╱{RC}╭╮{GC}╱╱╱╱╱{RC}╭━━━╮
            {RC}┃╭╮╭╮┃{GC}╱╱╱╱{RC}┃┃{GC}╱╱╱╱╱{RC}┃╭━╮┃
            ╰╯┃┃┣┻━┳━━┫┃{GC}╱╱╱╱╱{RC}┃╰━╯┃
            {GC}╱╱{RC}┃┃┃╭╮┃╭╮┃┃{GC}╱{RC}╭━━╮┃╭╮╭╯
            {GC}╱╱{RC}┃┃┃╰╯┃╰╯┃╰╮╰━━╯┃┃┃╰╮
            {GC}╱╱{RC}╰╯╰━━┻━━┻━╯{GC}╱╱╱╱{RC}╰╯╰━╯{DF}''')
	vers()
	ttst = input(f"{GC}input text for create Text to speech mp3 file \n  {YC}>>>{DF} ")
	ttsn = input(f"\n{GC}Enter name for output mp3 with .mp3 \n   {YC}>>>{DF} ")

	tts = gtts.gTTS(ttst, lang='en')

	tts.save(ttsn)
	os.system('play-audio' + ' ' + ttsn)
	print(f'{RC}audio file save in current directory as{DF} ',ttsn)
	sleep(5)
