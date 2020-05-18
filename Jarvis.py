import webbrowser as wb
import speech_recognition as sr
from time import ctime
import time
from gtts import gTTS
import pygame
import geopy
import requests
import json

def speak(audioString):
    global x
    
    if len(audioString) == 0:
        return
    
    tts = gTTS(text = audioString, lang = 'en-in', lang_check = False)
    tts.save("voice%s.mp3"%(x))
    pygame.init()
    pygame.display.set_mode((1, 1))
    pygame.mixer.music.load("voice%s.mp3" % (x))
    pygame.mixer.music.play(0)
    x += 1
    clock = pygame.time.Clock()
    clock.tick(10)
    
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)

def recognizeSpeech():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Speak...")
        audio = r.listen(source)
        print("heard...waiting for google to recogize audio")
    
    data = ""
    
    try:
        data = r.recognize_google(audio)
        print("You said : " + data )
    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        data = "!@#$%"
    
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        data = "!@#$%"
    
    return data

def cordinates(address, type):
    locator = geopy.Nominatim(user_agent="myGeocoder")
    loc = locator.geocode(address)
    
    if type  == "from":
        return "lat=" + str(loc.latitude) + "&lng=" + str(loc.longitude)
    
    return "drop_lat=" + str(loc.latitude) + "&drop_lng=" + str(loc.longitude)

def weather(city):  
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=e51e70301cecc37ca497866f433b8538&q=" + city) 
    x = response.json() 
    
    if x["cod"] != "404":  
        temp = "%0.1f"%(x["main"]["temp"] - 273.15)
        
        if x["main"]["temp"] - 273.15 == int(x["main"]["temp"] - 273.15):
            temp = str(int(x["main"]["temp"] - 273.15))
        
        print(" Temperature (in degree Celcius) = " + temp + "\n Atmospheric pressure (in atm unit) = " + "%0.3f"%(x["main"]["pressure"] / 1013.25) + "\n Humidity (in percentage) = " + str(x["main"]["humidity"]) + "\n Description = " + str(x["weather"][0]["description"])) 
        speak(" Temperature " + temp + " degree Celcius. \n atmospheric pressure " + "%0.3f"%(x["main"]["pressure"] / 1013.25) + " atmosphere  \n humidity " + str(x["main"]["humidity"]) + "% \n The weather is " + str(x["weather"][0]["description"])) 
        speak(name + "! Please hold on! , we are re-directing you to new tab for detailed view of weather of " + x["name"])
        wb.open_new_tab("https://openweathermap.org/city/" + str(x["id"]))
    
    else: 
        speak("Sorry! City Not Found ") 

def jarvis(data, name):
    data = data.lower()
    
    if "how are you" in data:
        speak(name + "!, I am fine ")

    elif "what time is it" in data:
        speak(ctime()[11:19])

    elif "where is" in data:
        data = data.split(" ")
        location = "+".join(data[2:])
        speak("Hold on " + name + ", I will show you where " + " ".join(data[2:]) + " is.")
        wb.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")

    elif "book ola" in data or "book cab" in data:
        Ola = data.split(" ")
        speak("Hold on " + name + ". Re-directing you to the booking page for the rest details.")
        source = " ".join(Ola[Ola.index("from") + 1: Ola.index("to")]) 
        destination = " ".join(Ola[Ola.index("to") + 1:])
        wb.open_new_tab("http://book.olacabs.com/?" + cordinates(source, "from") + "&utm_source=12343&" + cordinates(destination, "to") + "&dsw=yes")
    
    elif "check weather" in data:
        data = data.split(" ")
        city = "+".join(data[data.index("of") + 1 :])
        weather(city)

    elif "!@#$%" in data:
        speak(",,,,,,,Sorry " + name + "I did not get what you said !")

    elif "do nothing" in data:
        speak("Okay " + name + "! As you wish.")
    
    else :
        a = data.split(" ")
        
        if "search" in a:
            a.remove("search")
        
        if "google" in a:
            s= a.index("google") - 1
            
            if a[s] == "on":
                a.pop(s)
            
            a.remove("google")
        
        query = "+".join(a)
        speak("These are the search results from the google.")
        print("http://gogle.com/#q="+query)
        wb.open_new_tab("http://gogle.com/#q="+query)


x=1
print("Starting Program..")
speak("Hi! This is JARVIS 1.0!  Please tell me your name")
name = recognizeSpeech()
speak("Hi! " + name + "! What a nice name you have. Now Tell me, what can I do for you?")
recognizedText = recognizeSpeech() 
jarvis(recognizedText, name) 
speak("Turning off the program.")
print("Run complete")

