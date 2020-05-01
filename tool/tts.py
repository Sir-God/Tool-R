import gtts
import os
import sys
from os import system
from time import sleep
from main.style import *

def textspeech():
	test_w = 'For Now This Script Only Support English Language But We Are Working On this Script'
	print(test_w)
	sleep(7)
	system('clear')
	ttst = input("input text for create them mp3: ")
	ttsn = input("Enter name for output mp3 with .mp3: ")

	tts = gtts.gTTS(ttst, lang='en')

	tts.save(ttsn)
	os.system('play-audio' + ' ' + ttsn)
