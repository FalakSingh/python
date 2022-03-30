

from re import I
import playsound
from gtts import gTTS  
import os
import speech_recognition as sr

greetings = "Hello Sir What can i do for you?"
 
def speak(stuff):
    filename = "audio.mp3"
    engine = gTTS(text=stuff, lang="en", slow=False)
    engine.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            # listener.dynamic_energy_threshold = False
            # listener.adjust_for_ambient_noise(source, duration=0.2)
            print("[+] Listening...")
            voice = listener.listen(source)
            print("recognizing")
            initial_audio = listener.recognize_google(voice)
            initial_audio = initial_audio.lower()
            print(initial_audio)
            return initial_audio
    except Exception as error:
        print(error)


import pyaudio
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(info['index'], info['name'])

# print(sr.Microphone.list_microphone_names())
# speak(greetings)
# mic_list = sr.Microphone.list_microphone_names()
  
# #the following loop aims to set the device ID of the mic that
# #we specifically want to use to avoid ambiguity.
# for i, microphone_name in enumerate(mic_list):
#     if microphone_name == mic_name:
#         device_id = i

# while True:
    # listen()
    # print(speech_input)
    # try:
    #     if "alexa" in speech_input:
    #         speech_input = speech_input.replace("alexa","")
    #         speak(speech_input)
    # except TypeError:
    #     continue    
