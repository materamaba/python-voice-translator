import pyttsx3
import speech_recognition as sr
from translate import Translator
import sys
import time

r = sr.Recognizer()

translator_en = Translator(to_lang="en")
translator_pl = Translator(to_lang="pl")


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    print(text)
    engine.runAndWait()
    engine.stop()


def listen(lang):
    with sr.Microphone() as source:
        print("Nagrywam...")
        audio = r.listen(source)
    return r.recognize_google(audio, language=lang)


mic_list = sr.Microphone.list_microphone_names()
if not mic_list:
    speak("Nie wykryto żadnego mikrofonu. Sprawdź podłączenie.")
    sys.exit(0)


with sr.Microphone() as source:
    print("Kalibracja mikrofonu...")
    r.adjust_for_ambient_noise(source, duration=1)


speak("Wybierz język źródłowy. Powiedz: Polski lub Angielski")

jezyk = 0

try:
    text = listen("pl-PL")

    if text.upper() == "POLSKI":
        jezyk = "pl-PL"
        speak("Wybrano język polski")

    elif text.upper() == "ANGIELSKI":
        jezyk = "en-US"
        speak("Wybrano język angielski")

    else:
        speak("Nieprawidłowy język")
        sys.exit(0)

except:
    speak("Nie rozumiem.")
    sys.exit(0)

while True:   
    speak("Co chcesz zrobić?")
    speak('Powiedz "przetłumacz" aby coś przetłumaczyć.')
    speak('Powiedz "zmień język" aby zmienić język.')
    speak('Powiedz "koniec" aby zakończyć program.')

    time.sleep(1)

    try:
        instrukcja = listen("pl-PL")

        if instrukcja.upper() == "PRZETŁUMACZ":
            try:
                speak("Jakie słowo chcesz przetłumaczyć")
                slowo = listen(jezyk)

                if jezyk == "pl-PL":
                    przetlumaczone = translator_en.translate(slowo)
                    speak(slowo + " po angielsku to " + przetlumaczone)
                else:
                    przetlumaczone = translator_pl.translate(slowo)
                    speak(slowo + " po polsku to " + przetlumaczone)

            except:
                speak("Nie rozumiem.")

        if instrukcja.upper() == "ZMIEŃ JĘZYK":
            if jezyk == "pl-PL":
                jezyk = "en-US"
                speak("Wybrano język angielski")
            else:
                jezyk = "pl-PL"
                speak("Wybrano język polski")

        if instrukcja.upper() == "KONIEC":
            speak("bywaj")
            break

    except:
        speak("Nie rozumiem.")
        break