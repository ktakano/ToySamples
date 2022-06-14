from gtts import gTTS
import os
import playsound

tts = gTTS(text='Hello, my name is John.', lang='en')
tts.save("hello.mp3")

playsound.playsound('hello.mp3')