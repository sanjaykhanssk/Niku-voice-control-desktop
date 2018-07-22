# from voxpopuli import Voice
# # really slow fice with high pitch
# voice = Voice(lang="en",pitch=99,)
# voice.say("openning browser....")

import pyttsx3
engine = pyttsx3.init()

engine.say("opening browser ")

engine.runAndWait()