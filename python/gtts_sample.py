from gtts import gTTS
import os
import playsound

tts = gTTS(text='what do you think this boy is doing', lang='en')
tts.save("kono.mp3")

playsound.playsound('kono.mp3')