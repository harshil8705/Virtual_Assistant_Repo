import speech_recognition as sr
import pyttsx3
import webbrowser
from openai import OpenAI
import pyjokes
import datetime


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 145)


def process_command(command):

    command = command.lower().strip()

    if any(phrase in command for phrase in ["open google", "go to google"]):
        webbrowser.open("https://google.com")
        
    elif any(phrase in command for phrase in ["open youtube", "go to youtube"]):
        webbrowser.open("https://youtube.com")
        
    elif any(phrase in command for phrase in ["open open ai", "go to open ai", "open chat gpt", "go to chat gpt"]):
        webbrowser.open("https://openai.com/chatgpt/")
    
    elif any(phrase in command for phrase in ["open gemini", "open google gemini", "open gemini google", "go to gemini", "go to google gemini", "go to gemini google"]):
        webbrowser.open("https://gemini.google.com/app")
    
    elif any(phrase in command for phrase in ["open whatsapp", "go to whatsapp"]):
        webbrowser.open("https://web.whatsapp.com/")
    
    elif any(phrase in command for phrase in ["open facebook", "go to facebook"]):
        webbrowser.open("https://www.facebook.com/")
    
    elif any(phrase in command for phrase in ["open linkedin", "go to linkedin"]):
        webbrowser.open("https://in.linkedin.com/")
    
    elif any(phrase in command for phrase in ["open instagram", "go to instagram"]):
        webbrowser.open("https://www.instagram.com/")
    
    elif any(phrase in command for phrase in ["open snapchat", "go to snapchat"]):
        webbrowser.open("https://www.snapchat.com/")
    
    elif any(phrase in command for phrase in ["open spotify", "go to spotify"]):
        webbrowser.open("https://open.spotify.com/")
    
    elif command.startswith("play "):
        song = command.replace("play ", "").strip()
        search_query = f"https://www.google.com/search?q=play+{song}"
        webbrowser.open(search_query)
        engine.say(f"teleporting to the google for playing {song}.")
        engine.runAndWait()
        
    elif command.startswith("stop"):
        exit(1)
    elif ("joke" in command):
        joke = pyjokes.get_joke("en", category =  "neutral")
        engine.say(joke)
        engine.runAndWait()
    elif any (phrase in command for phrase in ["what is date", "tell me current date", "what is the date today","tell me the current date", "what is date today"]):
        current_datetime = datetime.datetime.now()
        print(f"The current date is : {current_datetime.date()}")
        engine.say(f"The current date is : {current_datetime.date()}")
        engine.runAndWait()
        
    elif any (phrase in command for phrase in ["what is time", "tell me current time", "what is the time now",  "tell me the current time", "what is time now"]):
        current_datetime = datetime.datetime.now()
        print(f"The current time is : {current_datetime.time()}")
        engine.say(f"The current time is : {current_datetime.time()}")
        engine.runAndWait()
        
    else:
        client = OpenAI()

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a Helpfull Personal Assistant for Desktop Users and you will Help desktop users solving their tasks."},
                {
                    "role": "user",
                    "content": command
                }
            ]
        )
        engine.say(completion.choices[0].message)
        engine.runAndWait()

def main():
    engine.say("Initializing Infotech.")
    engine.runAndWait()
    while True:
        try:
            with sr.Microphone() as source:
                sr.Recognizer().adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
                print("Listning...")
                audio = sr.Recognizer().listen(source)
                print("Recognizing...")
                text = sr.Recognizer().recognize_google(audio)
                print(f"You said : {text}")
                if text.lower() == 'infotech':
                    engine.say("Yes I am Listning...")
                    engine.runAndWait()
                    print("Infotech active...")
                    print("Listining...")
                    audio = sr.Recognizer().listen(source)
                    print("Recognizing...")
                    command = sr.Recognizer().recognize_google(audio)
                    print(f"You said : {command}")
                    process_command(command)
        except Exception as e:
            print(f"Please give me the Command : {e}")


if __name__ == '__main__':
    main()