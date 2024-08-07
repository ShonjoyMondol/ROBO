import re
import pyttsx3
import requests
import json
import speech_recognition as sr
from datetime import datetime
import pytz

# Initialize the TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

# Your Google Gemini API key
GOOGLE_GEMINI_API_KEY = "Your Google Gemini API key"   # Change and replace to your api key except the code will doesn't work
GOOGLE_GEMINI_MAX_TOKENS = 60
GOOGLE_GEMINI_MODEL = "gemini-1.5-flash"

# Time zone for Bangladesh
BANGLADESH_TIMEZONE = pytz.timezone('Asia/Dhaka')

# Assistant's details
ASSISTANT_NAME = "Robo"
ASSISTANT_CREATOR = "Almighty"
ASSISTANT_GENDER = "male"
ASSISTANT_BIRTH_DATE = datetime(2024, 7, 10, tzinfo=pytz.UTC)  # Using UTC as the timezone

def speak(text):
    """Converts text to speech and outputs through speakers, filtering out unwanted characters."""
    # Remove unwanted characters like *, **, ***
    filtered_text = re.sub(r'[*]+', '', text)
    engine.say(filtered_text)
    engine.runAndWait()

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        transcript = recognizer.recognize_google(audio).lower()
        print(f"You said: {transcript}")
        return transcript
    except sr.RequestError:
        print("API unavailable")
        speak("Sorry, the speech recognition service is unavailable.")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")

def get_information_from_google_gemini(query):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GOOGLE_GEMINI_MODEL}:generateContent?key={GOOGLE_GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [{"parts": [{"text": query}]}],
        "generationConfig": {"maxOutputTokens": GOOGLE_GEMINI_MAX_TOKENS}
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        if "candidates" in data and data["candidates"]:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "No relevant information found."
    else:
        print(f"Failed to fetch information: {response.status_code}")
        speak("I'm sorry, I couldn't find the information you requested.")
        return None

def get_current_time():
    """Returns the current time in Bangladesh in a 12-hour format."""
    current_time = datetime.now(BANGLADESH_TIMEZONE)
    return current_time.strftime("%I:%M %p")

def get_current_date():
    """Returns the current date in Bangladesh."""
    current_date = datetime.now(BANGLADESH_TIMEZONE)
    return current_date.strftime("%B %d, %Y")

def calculate_age():
    """Calculates the age of the assistant from the birth date."""
    today = datetime.now(BANGLADESH_TIMEZONE)
    age = today - ASSISTANT_BIRTH_DATE
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    return years, months, days

def main():
    print("System ready. Say the wake word to start...")

    # Continuous listening for the wake word and commands
    while True:
        command = recognize_speech_from_mic()
        if command:
            if command.startswith(ASSISTANT_NAME.lower()) or command.startswith(f"hey {ASSISTANT_NAME.lower()}"):
                # Extract the part of the command after the wake word
                command = command.replace(ASSISTANT_NAME.lower(), '').replace(f"hey {ASSISTANT_NAME.lower()}", '').strip()

                if not command:
                    # If the command is empty after removing the wake word, respond with "How can I help you?"
                    speak("How can I help you?")
                elif 'stop' in command or 'exit' in command:
                    speak("Goodbye!")
                    break
                elif 'time' in command:
                    current_time = get_current_time()
                    speak(f"The current time in Bangladesh is {current_time}.")
                elif 'date' in command:
                    current_date = get_current_date()
                    speak(f"Today's date is {current_date}.")
                elif 'what is your name' in command or 'who are you' in command:
                    speak(f"My name is {ASSISTANT_NAME}. I am a {ASSISTANT_GENDER} Humanoid Robot.")
                elif 'created' in command or 'create' in command or 'creates' in command or 'made' in command or 'mades' in command or 'maded' in command or 'make' in command or 'maked' in command or 'makes' in command or 'invent' in command or 'invented' in command or 'inventor' in command or 'invents' in command and 'you' in command or 'your' in command:
                    speak(f"{ASSISTANT_CREATOR} is my Creator.")
                elif 'how old are you' in command or 'what is your age' in command or 'how old you are' in command:
                    years, months, days = calculate_age()
                    speak(f"I am {years} years, {months} months, and {days} days old.")
                else:
                    result = get_information_from_google_gemini(command)
                    if result:
                        print(f"Search result: {result}")
                        speak(result)
                    else:
                        speak("I couldn't find any information.")
            else:
                print("Wake word not detected in command.")
        else:
            print("No command detected")

if __name__ == "__main__":
    main()
