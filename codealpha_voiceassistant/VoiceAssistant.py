# Import necessary libraries
import speech_recognition as sr  # For converting speech to text
import pyttsx3  # For text-to-speech (speaking out loud)
import datetime  # To get the current time
import webbrowser  # To open websites
import wikipedia  # To fetch summaries from Wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speaking speed (words per minute)

# Function to speak a given text
def speak(text):
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Process and speak the queued text

# Function to greet the user based on the current time
def greet():
    hour = datetime.datetime.now().hour  # Get current hour (0–23)
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you?")  # Introduce assistant

# Function to capture and recognize voice input
def take_command():
    recognizer = sr.Recognizer()  # Create recognizer object
    with sr.Microphone() as source:  # Use the microphone as input source
        print("Listening...")
        recognizer.pause_threshold = 1  # Pause before considering sentence complete
        audio = recognizer.listen(source)  # Listen for audio input

    try:
        print("Recognizing...")
        # Use Google’s speech recognition to convert audio to text
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")  # Print recognized command
    except Exception as e:
        print("Sorry, could not understand. Please say that again.")
        return ""  # Return empty string if recognition failed

    return command.lower()  # Return the command in lowercase

# Function to process the recognized voice command
def process_command(command):
    if "wikipedia" in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "")  # Remove 'wikipedia' keyword
        result = wikipedia.summary(query, sentences=2)  # Get summary (2 sentences)
        speak("According to Wikipedia")
        print(result)
        speak(result)
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")  # Open YouTube
        speak("Opening YouTube")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")  # Open Google
        speak("Opening Google")
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")  # Get current time
        speak(f"The time is {time}")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()  # Exit the program
    else:
        speak("Sorry, I didn't understand that command.")  # Handle unknown commands

# Entry point of the program
if __name__ == "__main__":
    greet()  # Greet the user

    # Infinite loop to continuously listen and respond
    while True:
        command = take_command()  # Take voice command
        if command:  # If a valid command is received
            process_command(command)  # Process the command
