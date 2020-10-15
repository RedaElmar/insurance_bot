## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

import requests
import speech_recognition as sr     # import the library
import subprocess
from gtts import gTTS
import json




"""
data = json.dumps({"sender": "Rasa","message": "salut"})
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
res = res.json()
val = res[0]['text']

print(val)
"""

bot_message = ""
message=""


r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": "Salut","Sender": "rasa" })



bot_messages =[]
for i in r.json(): #it gives error here
    bot_messages += [i['text'],]
    #print(f"{bot_message}")
for bot_message in bot_messages:
    myobj = gTTS(text=bot_message,lang="fr")
    myobj.save("welcome.mp3")
    # Playing the converted file
    subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])
def listentouser():
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        r.adjust_for_ambient_noise(source,duration = 3)
        print("En Ecoute  :")
        audio = r.listen(source)  # listen to the source
        try:
            messagev = r.recognize_google(audio, language="fr-FR") # use recognizer to convert our audio into text part.
            print("Vous : {}".format(messagev))

        except:
            print("Veuillez réessayer")  # In case of voice not recognized  clearly
            messagev=listentouser()
    return messagev
def talktouser(messagev):
    r = requests.post('http://127.0.0.1:5005/webhooks/rest/webhook', json={"message": messagev})
    if r.status_code==200:
        print("Bot says, ---------------------------------------------------------")
        bot_messages =[]
        for i in r.json():
            bot_messages += [i['text'],]
        for bot_message in bot_messages:
            myobj = gTTS(text=bot_message,lang="fr")
            myobj.save("welcome.mp3")
            subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])
        return True

if "puis-je avoir votre nom ? Cela nous aide \u00e0 faire connaissance ." in bot_messages :
    talktouser(input("votre nom ici :"))
while 1:
    message=listentouser()
    talktouser(message)
