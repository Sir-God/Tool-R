import gtts
import os
import sys
from os import system
from time import sleep
from main.style import *

RC, GC, YC, CC, DF = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

def textspeech():
	banner()
	ttst = input("input text for create them mp3: ")
	ttsn = input("Enter name for output mp3 with .mp3: ")

	tts = gtts.gTTS(ttst, lang='en')

	tts.save(ttsn)
	os.system('play-audio' + ' ' + ttsn)
	print('audio file save in current directory as ',ttsn)
